from __future__ import annotations

from copy import deepcopy
from typing import Any


# ============================================================
# Mappings officiels existants
# ============================================================

from app.apdp_form_mapping import FORMULAIRE_UNIQUE_MAPPING
from app.apdp_annexe1_mapping import ANNEXE_1_SOUS_TRAITANCE_MAPPING
from app.apdp_annexe2_mapping import ANNEXE_2_COMMUNICATION_MAPPING
from app.apdp_annexe3_mapping import ANNEXE_3_INTERCONNEXION_MAPPING
from app.apdp_annexe4_mapping import APDP_ANNEXE4_MAPPING
from app.apdp_capteurs_mapping import APDP_CAPTEURS_MAPPING
from app.apdp_site_web_mapping import APDP_SITE_WEB_MAPPING
from app.apdp_engagement_conformite_mapping import (
    APDP_ENGAGEMENT_CONFORMITE_MAPPING,
)


# ============================================================
# Référentiel des mappings
#
# IMPORTANT :
# Ce dictionnaire ne contient que des références vers les
# mappings existants. Ils ne sont jamais modifiés ici.
# ============================================================

MAPPINGS: dict[str, dict[str, Any]] = {
    "formulaire_unique": FORMULAIRE_UNIQUE_MAPPING,
    "annexe_1_sous_traitance": ANNEXE_1_SOUS_TRAITANCE_MAPPING,
    "annexe_2_communication": ANNEXE_2_COMMUNICATION_MAPPING,
    "annexe_3_interconnexion": ANNEXE_3_INTERCONNEXION_MAPPING,
    "annexe_4_transfert": APDP_ANNEXE4_MAPPING,
    "formulaire_capteurs": APDP_CAPTEURS_MAPPING,
    "formulaire_site_web": APDP_SITE_WEB_MAPPING,
    "engagement_conformite": APDP_ENGAGEMENT_CONFORMITE_MAPPING,
}


# ============================================================
# Utilitaires
# ============================================================

_SKIP_KEYS = {
    "type",
    "label",
    "title",
    "titre",
    "description",
    "instruction",
    "instructions",
    "editable",
    "official_layout",
    "texte_officiel",
    "official_fixed_text",
    "readonly",
    "read_only",
}


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_rect(value: Any) -> bool:
    """
    Reconnaît une position sous forme :
        [x, y, width, height]
        (x, y, width, height)
    """
    return (
        isinstance(value, (list, tuple))
        and len(value) == 4
        and all(_is_number(v) for v in value)
    )


def _rect_from_value(value: Any) -> tuple[float, float, float, float] | None:
    """
    Convertit les principales représentations de coordonnées
    rencontrées dans les mappings existants.
    """

    if _is_rect(value):
        x, y, width, height = value
        return float(x), float(y), float(width), float(height)

    if isinstance(value, dict):
        # Format :
        # {"x": ..., "y": ..., "width": ..., "height": ...}
        if all(k in value for k in ("x", "y", "width", "height")):
            return (
                float(value["x"]),
                float(value["y"]),
                float(value["width"]),
                float(value["height"]),
            )

        # Format :
        # {"left": ..., "bottom": ..., "width": ..., "height": ...}
        if all(k in value for k in ("left", "bottom", "width", "height")):
            return (
                float(value["left"]),
                float(value["bottom"]),
                float(value["width"]),
                float(value["height"]),
            )

        # Format :
        # {"rect": [x, y, w, h]}
        if "rect" in value:
            rect = _rect_from_value(value["rect"])
            if rect is not None:
                return rect

        # Format :
        # {"position": [x, y, w, h]}
        if "position" in value:
            rect = _rect_from_value(value["position"])
            if rect is not None:
                return rect

    return None


def _position_from_zone(zone: Any) -> tuple[float, float, float, float] | None:
    """
    Recherche récursive d'une zone rectangulaire.

    Supporte notamment :
      - rect
      - position
      - x/y/width/height
      - zone
    """

    rect = _rect_from_value(zone)

    if rect is not None:
        return rect

    if not isinstance(zone, dict):
        return None

    for key in ("rect", "position", "zone"):
        if key in zone:
            rect = _rect_from_value(zone[key])
            if rect is not None:
                return rect

            if isinstance(zone[key], dict):
                rect = _position_from_zone(zone[key])
                if rect is not None:
                    return rect

    return None


def _normalise_page_key(value: Any) -> str:
    return str(value)


def _value_is_present(value: Any) -> bool:
    if value is None:
        return False

    if isinstance(value, str):
        return bool(value.strip())

    if isinstance(value, (list, tuple, dict)):
        return bool(value)

    return True


def _safe_value(data: dict[str, Any], key: str) -> Any:
    """
    Lecture tolérante des clés.

    On ne fait aucune transformation du mapping.
    """
    if key in data:
        return data[key]

    return None


# ============================================================
# Construction des overlays
# ============================================================

def _base_overlay(
    rect: tuple[float, float, float, float],
    value: Any = None,
    *,
    overlay_type: str = "text",
    checked: bool = False,
    zone: dict[str, Any] | None = None,
) -> dict[str, Any]:
    x, y, width, height = rect

    overlay: dict[str, Any] = {
        "type": overlay_type,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
    }

    if overlay_type == "checkbox":
        overlay["checked"] = bool(checked)
    else:
        overlay["value"] = "" if value is None else str(value)

    if isinstance(zone, dict):
        for key in (
            "font_name",
            "font_size",
            "leading",
            "clear_before",
            "clear_zones",
        ):
            if key in zone:
                overlay[key] = deepcopy(zone[key])

    return overlay


def _make_text_overlay(
    zone: Any,
    value: Any,
) -> dict[str, Any] | None:

    if not _value_is_present(value):
        return None

    rect = _position_from_zone(zone)

    if rect is None:
        return None

    overlay_type = "text"

    if isinstance(zone, dict):
        zone_type = zone.get("type")

        if zone_type in {
            "multiline",
            "multiline_text",
        }:
            overlay_type = "multiline"

    return _base_overlay(
        rect,
        value,
        overlay_type=overlay_type,
        zone=zone if isinstance(zone, dict) else None,
    )


def _make_checkbox_overlay(
    zone: Any,
    checked: bool,
) -> dict[str, Any] | None:

    rect = _position_from_zone(zone)

    if rect is None:
        return None

    return _base_overlay(
        rect,
        overlay_type="checkbox",
        checked=checked,
        zone=zone if isinstance(zone, dict) else None,
    )


# ============================================================
# Checkbox groups
# ============================================================

def _checkbox_option_rect(option: Any) -> tuple[float, float, float, float] | None:
    """
    Les mappings utilisent plusieurs formes :

        "oui": [x, y, w, h]

        "oui": {
            "position": [x, y, w, h]
        }

        "oui": {
            "rect": [x, y, w, h]
        }

        "oui": {
            "type": "checkbox",
            "position": [...]
        }
    """
    return _position_from_zone(option)


def _build_checkbox_group(
    field_name: str,
    mapping: dict[str, Any],
    data: dict[str, Any],
) -> list[dict[str, Any]]:

    overlays: list[dict[str, Any]] = []

    selected = data.get(field_name)

    # Cas :
    # "personnes_informees": "oui"
    #
    # Cas :
    # "personnes_informees": ["oui", "non"]
    #
    # Cas :
    # "personnes_informees": {"oui": true}
    if isinstance(selected, str):
        selected_values = {selected}
        selected_map = {selected: True}
    elif isinstance(selected, (list, tuple, set)):
        selected_values = {str(v) for v in selected}
        selected_map = {str(v): True for v in selected}
    elif isinstance(selected, dict):
        selected_values = {
            str(k)
            for k, v in selected.items()
            if bool(v)
        }
        selected_map = {
            str(k): bool(v)
            for k, v in selected.items()
        }
    elif isinstance(selected, bool):
        selected_values = {field_name} if selected else set()
        selected_map = {field_name: selected}
    else:
        selected_values = set()
        selected_map = {}

    for option_name, option_zone in mapping.items():

        if option_name in _SKIP_KEYS:
            continue

        if option_name in {
            "zone",
            "cases",
            "choices",
        }:
            continue

        # Un champ texte associé au checkbox_group
        # ne doit pas être traité comme une case.
        if isinstance(option_zone, dict):
            option_type = option_zone.get("type")

            if option_type in {
                "text",
                "multiline",
                "multiline_text",
                "same_area",
            }:
                continue

        rect = _checkbox_option_rect(option_zone)

        if rect is None:
            continue

        checked = (
            option_name in selected_values
            or bool(selected_map.get(option_name, False))
        )

        overlays.append(
            _base_overlay(
                rect,
                overlay_type="checkbox",
                checked=checked,
                zone=option_zone
                if isinstance(option_zone, dict)
                else None,
            )
        )

    # --------------------------------------------------------
    # Cas spécial :
    # checkbox_group avec "zone" + "cases"
    #
    # Exemple Annexe 4 :
    # operations_destinataire
    # support_transfert
    # --------------------------------------------------------

    if "cases" in mapping:
        cases = mapping.get("cases")

        if isinstance(cases, list):
            selected_cases = selected

            if isinstance(selected_cases, str):
                selected_cases = [selected_cases]

            if not isinstance(selected_cases, (list, tuple, set)):
                selected_cases = []

            selected_cases = {str(v) for v in selected_cases}

            for index, case_zone in enumerate(cases):

                rect = _checkbox_option_rect(case_zone)

                if rect is None:
                    continue

                # Si les cases sont nommées par leur position
                # dans la liste, on accepte également :
                # ["0", "1", ...]
                checked = (
                    str(index) in selected_cases
                    or (
                        isinstance(case_zone, dict)
                        and str(case_zone.get("name", "")) in selected_cases
                    )
                )

                overlays.append(
                    _base_overlay(
                        rect,
                        overlay_type="checkbox",
                        checked=checked,
                        zone=case_zone
                        if isinstance(case_zone, dict)
                        else None,
                    )
                )

    # --------------------------------------------------------
    # Champs texte associés au groupe
    # --------------------------------------------------------

    for option_name, option_zone in mapping.items():

        if option_name in _SKIP_KEYS:
            continue

        if option_name in {
            "zone",
            "cases",
            "choices",
        }:
            continue

        if not isinstance(option_zone, dict):
            continue

        option_type = option_zone.get("type")

        if option_type not in {
            "text",
            "multiline",
            "multiline_text",
            "same_area",
        }:
            continue

        value = data.get(option_name)

        if not _value_is_present(value):
            continue

        overlay = _make_text_overlay(option_zone, value)

        if overlay is not None:
            overlays.append(overlay)

    return overlays


# ============================================================
# Tables
# ============================================================

def _column_rect(column: Any) -> tuple[float, float, float, float] | None:
    return _position_from_zone(column)


def _build_table_from_columns(
    field_name: str,
    mapping: dict[str, Any],
    rows: Any,
) -> list[dict[str, Any]]:

    overlays: list[dict[str, Any]] = []

    if not isinstance(rows, list):
        return overlays

    columns = mapping.get("columns")
    if not isinstance(columns, dict):
        columns = mapping.get("colonnes")

    if not isinstance(columns, dict):
        return overlays

    column_names = list(columns.keys())

    for row_index, row in enumerate(rows):

        if not isinstance(row, dict):
            continue

        for column_index, column_name in enumerate(column_names):

            column_zone = columns.get(column_name)
            rect = _column_rect(column_zone)

            if rect is None:
                continue

            value = row.get(column_name)

            if not _value_is_present(value):
                continue

            # ------------------------------------------------
            # Si le mapping prévoit plusieurs lignes verticales,
            # on décale la cellule en fonction de la ligne.
            #
            # Le mapping existant reste maître de la géométrie.
            # ------------------------------------------------
            if isinstance(column_zone, dict):

                row_height = column_zone.get("row_height")

                if _is_number(row_height):
                    x, y, width, height = rect
                    rect = (
                        x,
                        y - float(row_index) * float(row_height),
                        width,
                        height,
                    )

            overlay = _make_text_overlay(
                {
                    "type": "text",
                    "rect": rect,
                },
                value,
            )

            if overlay is not None:
                overlays.append(overlay)

    return overlays


def _build_table_from_rows(
    field_name: str,
    mapping: dict[str, Any],
    rows: Any,
) -> list[dict[str, Any]]:

    overlays: list[dict[str, Any]] = []

    if not isinstance(rows, list):
        return overlays

    for row_index, row in enumerate(rows):

        if not isinstance(row, dict):
            continue

        for column_name, cell_zone in row.items():

            if column_name in _SKIP_KEYS:
                continue

            value = None

            # Si les données utilisateur sont :
            #
            # "intervenants": [
            #   {
            #       "denomination": "...",
            #       ...
            #   }
            # ]
            #
            # le nom de la colonne est directement recherché.
            if isinstance(row, dict):
                value = row.get(column_name)

            # Dans certains mappings, row décrit plutôt
            # la géométrie et la valeur est portée par la donnée.
            if isinstance(cell_zone, (list, tuple, dict)):

                if isinstance(rows[row_index], dict):
                    value = rows[row_index].get(column_name)

            if not _value_is_present(value):
                continue

            rect = _position_from_zone(cell_zone)

            if rect is None:
                continue

            overlay = _make_text_overlay(
                {
                    "type": "text",
                    "rect": rect,
                },
                value,
            )

            if overlay is not None:
                overlays.append(overlay)

    return overlays


def _build_table(
    field_name: str,
    mapping: dict[str, Any],
    data: dict[str, Any],
) -> list[dict[str, Any]]:

    rows = data.get(field_name)

    if not isinstance(rows, list):
        return []

    # Structure :
    # type=table + columns
    if isinstance(mapping.get("columns"), dict):
        return _build_table_from_columns(
            field_name,
            mapping,
            rows,
        )

    if isinstance(mapping.get("colonnes"), dict):
        return _build_table_from_columns(
            field_name,
            mapping,
            rows,
        )

    # Structure type :
    # rows: [...]
    if isinstance(mapping.get("rows"), list):
        return _build_table_from_rows(
            field_name,
            mapping,
            rows,
        )

    # Structure directe :
    # denomination/date/... : rect
    overlays: list[dict[str, Any]] = []

    for row in rows:

        if not isinstance(row, dict):
            continue

        for key, value in row.items():

            zone = mapping.get(key)

            if zone is None:
                continue

            overlay = _make_text_overlay(zone, value)

            if overlay is not None:
                overlays.append(overlay)

    return overlays


# ============================================================
# Déclaration
# ============================================================

def _build_declaration(
    field_name: str,
    mapping: dict[str, Any],
    data: dict[str, Any],
) -> list[dict[str, Any]]:

    overlays: list[dict[str, Any]] = []

    declaration_data = data.get(field_name)

    if not isinstance(declaration_data, dict):
        declaration_data = data

    # --------------------------------------------------------
    # Champs nommés
    #
    # mapping:
    # champs:
    #   nom_prenom: ...
    #   fonction: ...
    #   date: ...
    # --------------------------------------------------------

    champs = mapping.get("champs")

    if isinstance(champs, dict):

        for field_name_in_declaration, field_zone in champs.items():

            value = declaration_data.get(field_name_in_declaration)

            if not _value_is_present(value):
                continue

            overlay = _make_text_overlay(
                field_zone,
                value,
            )

            if overlay is not None:
                overlays.append(overlay)

    # --------------------------------------------------------
    # zone de déclaration générale
    # --------------------------------------------------------

    zone = mapping.get("zone")

    if isinstance(zone, list):

        # Si la donnée contient plusieurs valeurs :
        #
        # "declaration_honneur": {
        #     "zone": ["texte", ...]
        # }
        #
        # on remplit séquentiellement les zones.
        values = declaration_data.get("zone_values")

        if isinstance(values, list):

            for zone_item, value in zip(zone, values):

                if not _value_is_present(value):
                    continue

                overlay = _make_text_overlay(
                    zone_item,
                    value,
                )

                if overlay is not None:
                    overlays.append(overlay)

    else:

        value = declaration_data.get("texte")

        if value is None:
            value = data.get("texte")

        if _value_is_present(value):

            overlay = _make_text_overlay(
                zone,
                value,
            )

            if overlay is not None:
                overlays.append(overlay)

    return overlays


# ============================================================
# Same area
# ============================================================

def _build_same_area(
    field_name: str,
    mapping: dict[str, Any],
    data: dict[str, Any],
) -> list[dict[str, Any]]:

    value = data.get(field_name)

    if not _value_is_present(value):
        return []

    rect = _position_from_zone(mapping)

    if rect is None:
        return []

    overlay = _make_text_overlay(
        {
            "type": "text",
            "rect": rect,
        },
        value,
    )

    return [overlay] if overlay is not None else []


# ============================================================
# Champ simple
# ============================================================

def _build_simple_field(
    field_name: str,
    mapping: dict[str, Any],
    data: dict[str, Any],
) -> list[dict[str, Any]]:

    value = data.get(field_name)

    if not _value_is_present(value):
        return []

    overlay = _make_text_overlay(
        mapping,
        value,
    )

    return [overlay] if overlay is not None else []


# ============================================================
# Traversée générique
# ============================================================

def _build_field(
    field_name: str,
    mapping: Any,
    data: dict[str, Any],
) -> list[dict[str, Any]]:

    if not isinstance(mapping, dict):
        return []

    mapping_type = mapping.get("type")

    # --------------------------------------------------------
    # Texte officiel / éléments non éditables
    # --------------------------------------------------------

    if mapping_type in {
        "official_fixed_text",
        "texte_officiel",
    }:
        return []

    if mapping.get("editable") is False:
        return []

    # --------------------------------------------------------
    # Textes
    # --------------------------------------------------------

    if mapping_type in {
        "text",
        "multiline",
        "multiline_text",
    }:
        return _build_simple_field(
            field_name,
            mapping,
            data,
        )

    # --------------------------------------------------------
    # Checkbox simple
    # --------------------------------------------------------

    if mapping_type == "checkbox":
        value = data.get(field_name)

        # Autorise :
        # true
        # "oui"
        # 1
        checked = bool(value)

        if isinstance(value, str):
            checked = value.lower() in {
                "true",
                "1",
                "yes",
                "oui",
                "checked",
                "on",
            }

        overlay = _make_checkbox_overlay(
            mapping,
            checked,
        )

        return [overlay] if overlay is not None else []

    # --------------------------------------------------------
    # Checkbox group
    # --------------------------------------------------------

    if mapping_type in {
        "checkbox_group",
        "checklist_officielle",
    }:
        if mapping_type == "checklist_officielle":
            return []

        return _build_checkbox_group(
            field_name,
            mapping,
            data,
        )

    # --------------------------------------------------------
    # Tables
    # --------------------------------------------------------

    if mapping_type == "table":
        return _build_table(
            field_name,
            mapping,
            data,
        )

    # --------------------------------------------------------
    # Déclaration
    # --------------------------------------------------------

    if mapping_type == "declaration":
        return _build_declaration(
            field_name,
            mapping,
            data,
        )

    # --------------------------------------------------------
    # Same area
    # --------------------------------------------------------

    if mapping_type == "same_area":
        return _build_same_area(
            field_name,
            mapping,
            data,
        )

    # --------------------------------------------------------
    # Section : certains mappings utilisent "section"
    # comme conteneur.
    # --------------------------------------------------------

    if mapping_type == "section":

        overlays: list[dict[str, Any]] = []

        for child_name, child_mapping in mapping.items():

            if child_name in _SKIP_KEYS:
                continue

            overlays.extend(
                _build_field(
                    child_name,
                    child_mapping,
                    data,
                )
            )

        return overlays

    # --------------------------------------------------------
    # Structure inconnue :
    #
    # On tente uniquement une descente récursive.
    # Aucune zone n'est inventée.
    # --------------------------------------------------------

    overlays: list[dict[str, Any]] = []

    for child_name, child_mapping in mapping.items():

        if child_name in _SKIP_KEYS:
            continue

        if not isinstance(child_mapping, dict):
            continue

        overlays.extend(
            _build_field(
                child_name,
                child_mapping,
                data,
            )
        )

    return overlays


# ============================================================
# Recherche des pages
# ============================================================

def _iter_pages(mapping: dict[str, Any]):
    """
    Retourne les pages des mappings APDP existants.

    Structures supportées :

        {
            "page_1": {...},
            "page_2": {...}
        }

    et :

        {
            1: {...},
            2: {...},
            3: {...}
        }

    Les métadonnées comme document/titre/pages/
    official_layout/editable sont ignorées.

    IMPORTANT :
    cette fonction ne modifie jamais le mapping.
    """

    for key, value in mapping.items():

        if not isinstance(value, dict):
            continue

        # Format page_1 / page_2 / page_3
        key_string = str(key)

        if key_string.startswith("page_"):
            suffix = key_string[5:]

            if suffix.isdigit():
                yield f"page_{suffix}", value

            continue

        # Format numérique : 1 / 2 / 3
        if isinstance(key, int):
            yield f"page_{key}", value

            continue

        # Sécurité supplémentaire si la clé arrive sous forme "1"
        if key_string.isdigit():
            yield f"page_{key_string}", value

# ============================================================
# API principale
# ============================================================

def build_apdp_overlays(
    document_id: str,
    data: dict[str, Any],
) -> dict[int, list[dict[str, Any]]]:

    if document_id not in MAPPINGS:
        raise ValueError(
            f"Aucun mapping générique disponible pour le document "
            f"'{document_id}'."
        )

    if not isinstance(data, dict):
        raise ValueError(
            "Le champ 'data' doit être un objet JSON."
        )

    mapping = MAPPINGS[document_id]

    if not isinstance(mapping, dict):
        raise ValueError(
            f"Le mapping du document '{document_id}' est invalide."
        )

    overlays_by_page: dict[int, list[dict[str, Any]]] = {}

    # --------------------------------------------------------
    # Parcours des pages uniquement.
    # --------------------------------------------------------

    for page_key, page_mapping in _iter_pages(mapping):

        try:
            page_number = int(
                page_key.replace("page_", "", 1)
            )
        except ValueError:
            continue

        page_overlays: list[dict[str, Any]] = []

        for field_name, field_mapping in page_mapping.items():

            if field_name in _SKIP_KEYS:
                continue

            if not isinstance(field_mapping, dict):
                continue

            page_overlays.extend(
                _build_field(
                    str(field_name),
                    field_mapping,
                    data,
                )
            )

        if page_overlays:
            overlays_by_page[page_number] = page_overlays

    return overlays_by_page


# ============================================================
# Vérification interne facultative
# ============================================================

def validate_mapping(document_id: str) -> dict[str, Any]:
    """
    Audit léger du mapping.

    Cette fonction ne modifie absolument rien.
    Elle permet de vérifier que le mapping contient bien
    des pages et de compter les champs éditables.
    """

    if document_id not in MAPPINGS:
        raise ValueError(
            f"Mapping inconnu : {document_id}"
        )

    mapping = MAPPINGS[document_id]

    pages = list(_iter_pages(mapping))

    field_count = 0

    for _, page_mapping in pages:
        for field_name, field_mapping in page_mapping.items():

            if field_name in _SKIP_KEYS:
                continue

            if not isinstance(field_mapping, dict):
                continue

            if field_mapping.get("editable") is False:
                continue

            field_count += 1

    return {
        "document_id": document_id,
        "pages": len(pages),
        "fields": field_count,
        "mapping_modified": False,
    }


def validate_all_mappings() -> list[dict[str, Any]]:
    """
    Vérification de tous les mappings utilisés par le builder.
    Aucun fichier n'est modifié.
    """

    return [
        validate_mapping(document_id)
        for document_id in MAPPINGS
    ]
