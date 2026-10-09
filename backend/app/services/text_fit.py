"""
Ajustement de texte dans une zone rectangulaire d'un PDF officiel (overlay).

Principe : jamais de drawString() direct. On calcule d'abord ce qui tient dans
(width x height), en réduisant progressivement la police, puis en tronquant de
façon contrôlée en dernier recours. Le résultat indique si le texte a été tronqué
pour que l'appelant puisse le signaler (une troncature silencieuse sur un
formulaire réglementaire serait pire qu'un débordement visible).
"""
from dataclasses import dataclass
from reportlab.pdfbase.pdfmetrics import stringWidth

ELLIPSIS = "…"


@dataclass
class FitResult:
    lines: list
    font_size: float
    leading: float
    truncated: bool


def _break_long_word(word, font, size, max_width):
    """Coupe un mot plus large que la zone (ex : e-mail, URL, référence longue)."""
    parts, current = [], ""
    for ch in word:
        if stringWidth(current + ch, font, size) <= max_width:
            current += ch
        else:
            if current:
                parts.append(current)
            current = ch
    if current:
        parts.append(current)
    return parts


def wrap_text(text, font, size, max_width):
    lines = []
    for paragraph in str(text).split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if stringWidth(candidate, font, size) <= max_width:
                current = candidate
                continue
            if current:
                lines.append(current)
                current = ""
            if stringWidth(word, font, size) <= max_width:
                current = word
            else:
                chunks = _break_long_word(word, font, size, max_width)
                lines.extend(chunks[:-1])
                current = chunks[-1]
        lines.append(current)
    return lines


def _truncate_line(line, font, size, max_width):
    if stringWidth(line, font, size) <= max_width:
        return line
    while line and stringWidth(line + ELLIPSIS, font, size) > max_width:
        line = line[:-1]
    return (line.rstrip() + ELLIPSIS) if line else ELLIPSIS


def fit_text(text, width, height, font="Helvetica", max_size=8.0, min_size=5.0,
             multiline=True, leading_factor=1.15, step=0.5):
    text = "" if text is None else str(text)
    size = max_size
    while size >= min_size - 1e-9:
        leading = size * leading_factor
        if multiline:
            lines = wrap_text(text, font, size, width)
            if len(lines) * leading <= height:
                return FitResult(lines, size, leading, False)
        else:
            flat = " ".join(text.split())
            if stringWidth(flat, font, size) <= width and size <= height:
                return FitResult([flat], size, leading, False)
        size -= step

    # Dernier recours : taille minimale + troncature contrôlée.
    size = min_size
    leading = size * leading_factor
    if multiline:
        lines = wrap_text(text, font, size, width)
        max_lines = max(1, int(height // leading))
        kept = lines[:max_lines]
        kept[-1] = _truncate_line(kept[-1] + ELLIPSIS if len(lines) > max_lines else kept[-1],
                                  font, size, width)
        return FitResult(kept, size, leading, True)
    flat = " ".join(text.split())
    return FitResult([_truncate_line(flat, font, size, width)], size, leading, True)


def draw_field(c, text, x, y, width, height, font="Helvetica", max_size=8.0,
               min_size=5.0, multiline=True, padding=1.5):
    """Dessine `text` dans la zone dont le coin bas-gauche est (x, y) (repère ReportLab).
    Retourne le FitResult (à journaliser si truncated=True)."""
    inner_w, inner_h = width - 2 * padding, height - 2 * padding
    result = fit_text(text, inner_w, inner_h, font, max_size, min_size, multiline)
    c.setFont(font, result.font_size)
    if multiline:
        top = y + height - padding
        baseline = top - result.font_size
        for line in result.lines:
            c.drawString(x + padding, baseline, line)
            baseline -= result.leading
    else:
        # ligne unique centrée verticalement dans la zone
        baseline = y + (height - result.font_size) / 2 + result.font_size * 0.2
        c.drawString(x + padding, baseline, result.lines[0])
    return result
