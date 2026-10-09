from __future__ import annotations

from app.apdp_form_mapping import FORMULAIRE_UNIQUE_MAPPING


def build_formulaire_unique_overlays(
    data: dict,
) -> dict[int, list[dict]]:

    overlays: dict[int, list[dict]] = {}
    # Composition des personnes ayant accès aux données.
    # La civilité doit être fournie explicitement par les données.
    # Aucune civilité n'est déduite du nom.
    for i in range(1, 5):
        civilite = str(
            data.get(f"personne_acces_{i}_civilite", "")
        ).strip()

        nom = str(
            data.get(f"personne_acces_{i}_nom", "")
        ).strip()

        fonction = str(
            data.get(f"personne_acces_{i}_fonction", "")
        ).strip()

        if civilite not in {"Mme", "M."}:
            continue

        if nom and fonction:
            valeur = f"{nom} ({fonction})"
        elif nom:
            valeur = nom
        elif fonction:
            valeur = f"({fonction})"
        else:
            continue

        if civilite == "Mme":
            data[f"personne_acces_{i}_mme"] = valeur
        else:
            data[f"personne_acces_{i}_m"] = valeur

    for page_number, page_mapping in FORMULAIRE_UNIQUE_MAPPING.items():

        if not page_mapping:
            continue

        overlays[page_number] = []

        for field_name, zone in page_mapping.items():

            zone_type = zone["type"]
            # Les champs nom/fonction/civilité de la page 6
            # servent uniquement à construire les zones Mme/M.
            if page_number == 6 and (
                field_name.endswith("_nom")
                or field_name.endswith("_fonction")
                or field_name.endswith("_civilite")
            ):
                continue

            if zone_type == "checkbox":

                overlays[page_number].append({
                    "type": "checkbox",
                    "x": zone["x"],
                    "y": zone["y"],
                    "width": zone["width"],
                    "height": zone["height"],
                    "checked": bool(
                        data.get(
                            field_name,
                            False,
                        )
                    ),
                })

                continue

            value = data.get(field_name)

            if value is None:
                continue

            value = str(value).strip()

            if not value:
                continue

            overlays[page_number].append({
                "type": zone_type,
                "x": zone["x"],
                "y": zone["y"],
                "width": zone["width"],
                "height": zone["height"],
                "value": value,
                "font_name": "Helvetica",
                "font_size": zone.get("font_size", 8),
                "clear_before": zone.get(
                    "clear_before",
                    False,
                ),
                "clear_zones": zone.get(
                    "clear_zones",
                    [],
                ),
            })

    return overlays
