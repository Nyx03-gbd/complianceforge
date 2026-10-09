from __future__ import annotations

from typing import Any


IGNORED_TYPES = {
    "official_fixed_text",
    "texte_officiel",
    "checklist_officielle",
}


def label_from_key(key: str) -> str:
    labels = {
        "npi_rccm": "NPI / RCCM",
        "nom_prenoms_raison_sociale": "Nom / prénoms / raison sociale",
        "nom_prenom": "Nom et prénom",
        "nom_prenoms": "Nom et prénoms",
        "carre_lot": "Carré / lot",
        "adresse_postale": "Adresse postale",
        "adresse_electronique": "Adresse électronique",
        "contact_telephonique": "Contact téléphonique",
        "donnees_personnelles": "Données personnelles concernées",
        "origine_donnees": "Origine des données",
        "nombre_personnes": "Nombre de personnes concernées",
        "finalite": "Finalité du traitement",
        "finalite_traitement": "Finalité du traitement",
        "fondement_juridique": "Fondement juridique",
        "duree_conservation": "Durée de conservation",
        "date_mise_en_oeuvre": "Date de mise en œuvre",
        "pays_transfert": "Pays de transfert",
        "donnees_objet_transfert": "Données objet du transfert",
        "finalite_transfert": "Finalité du transfert",
    }

    if key in labels:
        return labels[key]

    return key.replace("_", " ").strip().capitalize()


def _choice_values(node: dict[str, Any]) -> list[str]:
    """
    Retourne uniquement les vrais choix d'un checkbox_group.

    Règles :
    - un enfant de type checkbox est un choix ;
    - un enfant avec une géométrie directe x/y/width/height
      représente une case à cocher ;
    - un enfant avec rect/position représente également un choix ;
    - les champs text/multiline/textarea ne sont PAS des choix ;
    - les listes de choix explicites sont conservées.
    """

    result = []

    for key, value in node.items():

        if key in {
            "type",
            "label",
            "title",
            "titre",
            "description",
            "choices",
        }:
            continue

        if not isinstance(value, dict):
            if isinstance(value, list):
                result.append(str(key))
            continue

        value_type = value.get("type")

        # --------------------------------------------------------
        # Vrai checkbox / radio
        # --------------------------------------------------------
        if value_type in {
            "checkbox",
            "radio",
            "choice",
            "option",
        }:
            result.append(str(key))
            continue

        # --------------------------------------------------------
        # Coordonnées directes :
        # typiquement les cases Oui / Non des formulaires APDP.
        # --------------------------------------------------------
        if all(
            coordinate in value
            for coordinate in (
                "x",
                "y",
                "width",
                "height",
            )
        ):
            try:
                width = float(value["width"])
                height = float(value["height"])

                # Les cases à cocher APDP sont de petites zones
                # (environ 10-13 x 7-10).
                #
                # Les zones de texte possèdent généralement une
                # largeur/hauteur beaucoup plus importantes.
                if width <= 20 and height <= 20:
                    result.append(str(key))

                continue

            except (TypeError, ValueError):
                pass

        # --------------------------------------------------------
        # Rectangle explicite
        # --------------------------------------------------------
        if "rect" in value:
            result.append(str(key))
            continue

        # --------------------------------------------------------
        # Position explicite
        # --------------------------------------------------------
        if "position" in value:
            result.append(str(key))
            continue

        # --------------------------------------------------------
        # Les champs textuels ne sont JAMAIS des choix.
        # Exemple important :
        # base_communication.justification
        # --------------------------------------------------------
        if value_type in {
            "text",
            "multiline",
            "multiline_text",
            "textarea",
            "same_area",
            "official_fixed_text",
            "texte_officiel",
        }:
            continue

    choices = node.get("choices")

    if isinstance(choices, dict):
        result = list(choices.keys())

    elif isinstance(choices, list):
        result = [
            str(item)
            for item in choices
            if not isinstance(item, dict)
        ]

    return result


def _is_yes_no(values: list[str]) -> bool:
    normalized = {v.lower() for v in values}
    return normalized == {"oui", "non"}


def _extract_node(key: str, node: Any) -> dict[str, Any] | None:

    if not isinstance(node, dict):
        return None

    node_type = node.get("type")

    if node_type in IGNORED_TYPES:
        return None

    # ------------------------------------------------------------------
    # Structures composites de l'Annexe 1
    # Ces blocs n'ont volontairement pas de "type" dans le mapping PDF.
    # Ils contiennent uniquement des coordonnées utilisées pour le rendu.
    # Le mapping officiel reste inchangé.
    # ------------------------------------------------------------------

    if key == "mise_en_conformite_apdp" and node_type is None:
        return {
            "key": key,
            "label": "Mise en conformité auprès de l'APDP",
            "type": "section",
            "children": [
                {
                    "key": "mise_en_conformite_apdp_statut",
                    "label": "Mise en conformité auprès de l'APDP",
                    "type": "radio",
                    "choices": [
                        {"value": "non", "label": "Non"},
                        {"value": "oui", "label": "Oui"},
                    ],
                    "pdf_mapping": {
                        "non": "mise_en_conformite_apdp.non",
                        "oui": "mise_en_conformite_apdp.oui",
                    },
                },
                {
                    "key": "mise_en_conformite_apdp_references",
                    "label": "Références",
                    "type": "textarea",
                    "pdf_mapping": {
                        "field": "mise_en_conformite_apdp.references",
                    },
                },
                {
                    "key": "mise_en_conformite_apdp_garanties",
                    "label": "Garanties offertes",
                    "type": "checkbox_group",
                    "choices": [
                        {
                            "value": "responsabilite",
                            "label": "Responsabilité",
                        },
                        {
                            "value": "securite",
                            "label": "Sécurité",
                        },
                        {
                            "value": "confidentialite",
                            "label": "Confidentialité",
                        },
                        {
                            "value": "droits_personnes",
                            "label": "Droits des personnes",
                        },
                    ],
                    "pdf_mapping": {
                        "responsabilite":
                            "mise_en_conformite_apdp.garanties.responsabilite",
                        "securite":
                            "mise_en_conformite_apdp.garanties.securite",
                        "confidentialite":
                            "mise_en_conformite_apdp.garanties.confidentialite",
                        "droits_personnes":
                            "mise_en_conformite_apdp.garanties.droits_personnes",
                    },
                },
            ],
        }

    if key == "declaration_honneur" and node_type is None:
        return {
            "key": key,
            "label": "Déclaration sur l'honneur",
            "type": "declaration",
            "fields": [
                {
                    "key": "nom_prenom",
                    "label": "Nom et prénom",
                    "type": "text",
                },
                {
                    "key": "fonction",
                    "label": "Fonction",
                    "type": "text",
                },
                {
                    "key": "date",
                    "label": "Date",
                    "type": "text",
                },
            ],
        }

    if node_type == "checkbox":
        return {
            "key": key,
            "label": label_from_key(key),
            "type": "checkbox",
        }

    if node_type == "checkbox_group":

        # ------------------------------------------------------------
        # Annexe 1 — Information des personnes impliquées
        #
        # Le mapping officiel contient :
        #   non / oui / comment
        # Les coordonnées PDF sont conservées dans le mapping.
        # L'interface doit présenter Oui/Non + commentaire.
        # ------------------------------------------------------------
        if key == "personnes_informees":

            return {
                "key": key,
                "label": "Information des personnes impliquées",
                "type": "section",
                "children": [
                    {
                        "key": "personnes_informees_statut",
                        "label": "Les personnes impliquées sont-elles informées ?",
                        "type": "radio",
                        "choices": [
                            {"value": "non", "label": "Non"},
                            {"value": "oui", "label": "Oui"},
                        ],
                    },
                    {
                        "key": "personnes_informees_comment",
                        "label": "Comment",
                        "type": "textarea",
                    },
                ],
            }

        # ------------------------------------------------------------
        # Annexe 1 — Sécurité organisée par le sous-traitant
        #
        # Les quatre entrées du mapping sont des cases indépendantes.
        # ------------------------------------------------------------
        if key == "securite_sous_traitant":

            return {
                "key": key,
                "label": "Sécurité organisée par le sous-traitant",
                "type": "checkbox_group",
                "choices": [
                    {
                        "value": "communication_pssi",
                        "label": "Communication de la PSSI",
                    },
                    {
                        "value": "audits_securite",
                        "label": "Audits de sécurité",
                    },
                    {
                        "value": "mesures_organisationnelles",
                        "label": "Mesures organisationnelles",
                    },
                    {
                        "value": "mesures_physiques",
                        "label": "Mesures physiques",
                    },
                ],
            }

        choices = _choice_values(node)

        return {
            "key": key,
            "label": label_from_key(key),
            "type": "radio" if _is_yes_no(choices) else "checkbox_group",
            "choices": [
                {
                    "value": choice,
                    "label": label_from_key(choice),
                }
                for choice in choices
            ],
        }

    if node_type in {"text"}:
        return {
            "key": key,
            "label": label_from_key(key),
            "type": "text",
        }

    if node_type in {"multiline", "multiline_text"}:
        return {
            "key": key,
            "label": label_from_key(key),
            "type": "textarea",
        }

    if node_type == "table":
        columns = node.get("columns") or node.get("colonnes")

        # Certains tableaux du mapping officiel utilisent une structure
        # "colonnes directes" au lieu de node["columns"].
        # Exemple Annexe 1 :
        # {
        #   "type": "table",
        #   "denomination": {...},
        #   "date_contrat": {...},
        #   ...
        # }
        if columns is None:
            excluded_table_keys = {
                "type",
                "rows",
                "columns",
                "colonnes",
            }

            direct_columns = {}

            for column_key, column_value in node.items():
                if column_key in excluded_table_keys:
                    continue

                if isinstance(column_value, dict):
                    # Une colonne est identifiée par ses coordonnées PDF.
                    if any(
                        coord in column_value
                        for coord in ("x", "y", "width", "height")
                    ):
                        direct_columns[column_key] = column_value

            columns = direct_columns

        if isinstance(columns, dict):
            column_names = list(columns.keys())
        elif isinstance(columns, list):
            column_names = list(columns)
        else:
            column_names = []

        return {
            "key": key,
            "label": label_from_key(key),
            "type": "table",
            "columns": [
                {
                    "key": column,
                    "label": label_from_key(column),
                }
                for column in column_names
            ],
        }

    if node_type == "declaration":
        fields = node.get("champs", {})

        return {
            "key": key,
            "label": "Déclaration sur l'honneur",
            "type": "declaration",
            "text": node.get("texte", ""),
            "fields": [
                {
                    "key": field_key,
                    "label": label_from_key(field_key),
                    "type": "text",
                }
                for field_key in fields
                if isinstance(fields, dict)
            ],
        }

    # Section : on descend dans les enfants.
    children = []

    for child_key, child_value in node.items():

        if child_key in {
            "type",
            "rect",
            "position",
            "x",
            "y",
            "width",
            "height",
            "zone",
            "instruction",
            "editable",
            "text",
            "choices",
            "colonnes",
            "lignes",
            "champs",
        }:
            continue

        child = _extract_node(str(child_key), child_value)

        if child:
            children.append(child)

    if children:
        return {
            "key": key,
            "label": label_from_key(key),
            "type": "section",
            "children": children,
        }

    return None


def build_form_schema(mapping: dict[str, Any]) -> dict[str, Any]:

    pages = []

    for page_key, page_value in mapping.items():

        if not isinstance(page_value, dict):
            continue

        key_string = str(page_key)

        if key_string == "document":
            continue

        if key_string.startswith("page_"):
            page_number = key_string.replace("page_", "")
        elif key_string.isdigit():
            page_number = key_string
        else:
            continue

        fields = []
        consumed = set()

        # ---------------------------------------------------------
        # Regroupement interface des paires *_oui / *_non
        # Le mapping PDF reste inchangé : les deux coordonnées
        # restent disponibles pour l'overlay.
        # ---------------------------------------------------------

        for key, value in page_value.items():

            key = str(key)

            if key in consumed:
                continue

            # -----------------------------------------------------
            # Secteur d'activité : un seul choix parmi trois
            # -----------------------------------------------------

            if key == "secteur_prive":
                sector_keys = [
                    "secteur_prive",
                    "secteur_public",
                    "secteur_institutions_etrangeres",
                ]

                if all(k in page_value for k in sector_keys):
                    fields.append({
                        "key": "secteur",
                        "label": "Secteur d'activité",
                        "type": "radio",
                        "choices": [
                            {
                                "value": "prive",
                                "label": "Privé",
                            },
                            {
                                "value": "public",
                                "label": "Public",
                            },
                            {
                                "value": "institutions_etrangeres",
                                "label": "Institutions étrangères",
                            },
                        ],
                        "pdf_mapping": {
                            "prive": "secteur_prive",
                            "public": "secteur_public",
                            "institutions_etrangeres": "secteur_institutions_etrangeres",
                        },
                    })

                    consumed.update(sector_keys)
                    continue

            if key.endswith("_oui"):
                base = key[:-4]
                non_key = base + "_non"

                if non_key in page_value:
                    oui_node = page_value.get(key)
                    non_node = page_value.get(non_key)

                    if (
                        isinstance(oui_node, dict)
                        and isinstance(non_node, dict)
                        and oui_node.get("type") == "checkbox_group"
                        and non_node.get("type") == "checkbox_group"
                    ):
                        fields.append({
                            "key": base,
                            "label": label_from_key(base),
                            "type": "radio",
                            "choices": [
                                {
                                    "value": "oui",
                                    "label": "Oui",
                                },
                                {
                                    "value": "non",
                                    "label": "Non",
                                },
                            ],
                            "pdf_mapping": {
                                "oui": key,
                                "non": non_key,
                            },
                        })

                        consumed.add(key)
                        consumed.add(non_key)
                        continue

            if key.endswith("_non"):
                base = key[:-4]
                oui_key = base + "_oui"

                if oui_key in page_value:
                    continue

            field = _extract_node(key, value)

            if field:
                fields.append(field)

        pages.append({
            "page": int(page_number) if page_number.isdigit() else page_number,
            "fields": fields,
        })

    pages.sort(
        key=lambda item: (
            0,
            int(item["page"])
        ) if str(item["page"]).isdigit() else (
            1,
            str(item["page"])
        )
    )

    return {
        "pages": pages,
    }
