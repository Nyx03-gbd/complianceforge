from __future__ import annotations

from io import BytesIO
from pathlib import Path
import hashlib
import shutil

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

from app.apdp_documents import get_document
from app.services.text_fit import draw_field

BASE_DIR = Path(__file__).resolve().parents[2]

TEMPLATES_DIR = BASE_DIR / "templates" / "apdp"
GENERATED_DIR = BASE_DIR / "generated" / "apdp"


def get_template_path(document_id: str) -> Path:
    """
    Retourne le chemin du PDF APDP officiel.

    Le fichier source n'est jamais modifié.
    """
    document = get_document(document_id)

    template_path = BASE_DIR / document["source_file"]

    if not template_path.exists():
        raise FileNotFoundError(
            f"Template APDP introuvable : {template_path}"
        )

    return template_path


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()

    with file_path.open("rb") as fichier:
        for bloc in iter(
            lambda: fichier.read(1024 * 1024),
            b"",
        ):
            sha256.update(bloc)

    return sha256.hexdigest()


def copy_official_template(
    document_id: str,
    output_name: str,
) -> tuple[Path, str]:
    """
    Copie le PDF officiel sans aucune modification.
    """

    template_path = get_template_path(document_id)

    GENERATED_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = GENERATED_DIR / output_name

    shutil.copy2(
        template_path,
        output_path,
    )

    hash_integrite = calculate_sha256(
        output_path
    )

    return output_path, hash_integrite


def _draw_text(
    canvas_obj,
    text: str,
    x: float,
    y: float,
    width: float,
    height: float,
    font_name: str = "Helvetica",
    font_size: float = 8,
    min_font_size: float = 5,
    multiline: bool = False,
    padding: float = 1.5,
):
    """
    Dessine un texte dans une zone en utilisant le moteur text_fit.

    Le texte est ajusté automatiquement à la zone disponible.
    La police peut être réduite jusqu'à min_font_size.
    Une éventuelle troncature est signalée par FitResult.truncated.
    """

    if text is None:
        return None

    text = str(text).strip()

    if not text:
        return None

    result = draw_field(
        canvas_obj,
        text,
        x,
        y,
        width,
        height,
        font=font_name,
        max_size=font_size,
        min_size=min_font_size,
        multiline=multiline,
        padding=padding,
    )

    return result


def _draw_multiline_text(
    canvas_obj,
    text: str,
    x: float,
    y: float,
    width: float,
    height: float,
    font_name: str = "Helvetica",
    font_size: float = 8,
    min_font_size: float = 5,
    padding: float = 1.5,
):
    """
    Dessine un texte multilignes dans une zone en utilisant text_fit.
    """

    return _draw_text(
        canvas_obj,
        text,
        x,
        y,
        width,
        height,
        font_name=font_name,
        font_size=font_size,
        min_font_size=min_font_size,
        multiline=True,
        padding=padding,
    )

def _draw_checkbox(
    canvas_obj,
    x: float,
    y: float,
    width: float,
    height: float,
):
    """
    Coche une case déjà présente dans le PDF officiel.

    On ne dessine PAS la case :
    elle existe déjà dans le PDF APDP.

    On ajoute uniquement la marque.
    """

    canvas_obj.setFont(
        "Helvetica-Bold",
        min(width, height) * 0.85,
    )

    canvas_obj.drawString(
        x + width * 0.08,
        y + height * 0.02,
        "X",
    )

def _clear_zone(
    canvas_obj,
    x: float,
    y: float,
    width: float,
    height: float,
    padding: float = 2.0,
):
    """
    Masque uniquement l'intérieur de la zone de saisie.

    Les bordures et séparations du formulaire APDP
    restent visibles.
    """

    inner_width = max(
        0,
        width - (2 * padding),
    )

    inner_height = max(
        0,
        height - (2 * padding),
    )

    canvas_obj.saveState()

    canvas_obj.setFillColorRGB(
        1,
        1,
        1,
    )

    canvas_obj.rect(
        x + padding,
        y + padding,
        inner_width,
        inner_height,
        stroke=0,
        fill=1,
    )

    canvas_obj.restoreState()

def render_apdp_pdf(
    document_id: str,
    page_overlays: dict[int, list[dict]],
    output_name: str,
) -> tuple[Path, str, str]:
    """
    Génère un PDF APDP rempli par superposition.

    page_overlays :
    {
        1: [
            {
                "type": "text",
                "x": 103.71,
                "y": 531.90,
                "width": 199.75,
                "height": 22.60,
                "value": "..."
            },
            {
                "type": "checkbox",
                "x": ...,
                "y": ...,
                "width": ...,
                "height": ...,
                "checked": True
            }
        ],
        2: [...]
    }

    Les pages sont numérotées à partir de 1.
    """

    template_path = get_template_path(
        document_id
    )

    source_hash = calculate_sha256(
        template_path
    )

    reader = PdfReader(
        str(template_path)
    )
    writer = PdfWriter()

    for page_index, page in enumerate(
        reader.pages,
        start=1,
    ):
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)

        packet = BytesIO()

        overlay = canvas.Canvas(
            packet,
            pagesize=(
                page_width,
                page_height,
            ),
        )
        zones = page_overlays.get(
            page_index,
            [],
        )

        # Une page sans overlay doit rester inchangée.
        # ReportLab peut produire un PDF sans page lorsqu'aucun
        # contenu n'est dessiné sur le canvas.
        if not zones:
            writer.add_page(page)
            continue

        for zone in zones:

            zone_type = zone.get(
                "type",
                "text",
            )

            x = float(zone["x"])
            y = float(zone["y"])
            width = float(zone["width"])
            height = float(zone["height"])

            for clear_zone in zone.get("clear_zones", []):
                _clear_zone(
                    overlay,
                    float(clear_zone["x"]),
                    float(clear_zone["y"]),
                    float(clear_zone["width"]),
                    float(clear_zone["height"]),
                    padding=0.5,
                )

            if zone.get("clear_before", False):
                _clear_zone(
                    overlay,
                    x,
                    y,
                    width,
                    height,
                )

            if zone_type == "text":
                _draw_text(
                    overlay,
                    zone.get("value", ""),
                    x,
                    y,
                    width,
                    height,
                    zone.get(
                        "font_name",
                        "Helvetica",
                    ),
                    float(
                        zone.get(
                            "font_size",
                            8,
                        )
                    ),
                )

            elif zone_type == "multiline":

                _draw_multiline_text(
                    overlay,
                    zone.get("value", ""),
                    x,
                    y,
                    width,
                    height,
                    zone.get(
                        "font_name",
                        "Helvetica",
                    ),
                    float(
                        zone.get(
                            "font_size",
                            8,
                        )
                    ),
                    float(
                        zone.get(
                            "leading",
                            9,
                        )
                    ),
                )

            elif zone_type == "checkbox":

                if zone.get(
                    "checked",
                    False,
                ):
                    _draw_checkbox(
                        overlay,
                        x,
                        y,
                        width,
                        height,
                    )

        overlay.save()

        packet.seek(0)

        overlay_reader = PdfReader(
            packet
        )

        # Si le canvas n'a produit aucune page exploitable,
        # conserver la page officielle sans overlay.
        if len(overlay_reader.pages) > 0:
            page.merge_page(
                overlay_reader.pages[0]
            )

        writer.add_page(page)

    if len(writer.pages) != len(reader.pages):
        raise RuntimeError(
            "Erreur d'intégrité : "
            "le nombre de pages a changé."
        )

    GENERATED_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        GENERATED_DIR /
        output_name
    )

    with output_path.open("wb") as fichier:
        writer.write(fichier)

    output_hash = calculate_sha256(
        output_path
    )

    return (
        output_path,
        source_hash,
        output_hash,
    )
