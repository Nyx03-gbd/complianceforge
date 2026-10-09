"""
Mapping officiel — Annexe 1 APDP : SOUS-TRAITANCE.

IMPORTANT :
- Le PDF officiel APDP est la source de vérité.
- Le PDF original n'est jamais modifié.
- Les coordonnées correspondent au système de coordonnées PDF.
- Les cadres englobants et éléments graphiques ne sont pas utilisés
  comme champs de saisie.
"""

ANNEXE_1_SOUS_TRAITANCE_MAPPING = {

    1: {

        # ============================================================
        # INTERVENANTS AU TRAITEMENT
        # ============================================================

        "intervenants": {
            "type": "table",
            "columns": {
                "denomination": {
                    "x": 103.08,
                    "y": 556.80,
                    "width": 95.44,
                    "height": 22.60,
                },
                "contacts": {
                    "x": 198.78,
                    "y": 556.80,
                    "width": 104.44,
                    "height": 22.60,
                },
                "representant": {
                    "x": 303.46,
                    "y": 556.80,
                    "width": 99.89,
                    "height": 22.60,
                },
                "role": {
                    "x": 403.60,
                    "y": 556.80,
                    "width": 130.59,
                    "height": 22.60,
                },
            },

            "rows": [
                {
                    "denomination": (103.08, 556.80, 95.44, 22.60),
                    "contacts": (198.78, 556.80, 104.44, 22.60),
                    "representant": (303.46, 556.80, 99.89, 22.60),
                    "role": (403.60, 556.80, 130.59, 22.60),
                },
                {
                    "denomination": (103.08, 533.95, 95.44, 22.60),
                    "contacts": (198.78, 533.95, 104.44, 22.60),
                    "representant": (303.46, 533.95, 99.89, 22.60),
                    "role": (403.60, 533.95, 130.59, 22.60),
                },
            ],
        },

        # ============================================================
        # DONNEES AUXQUELLES L'INTERVENANT A ACCES
        # ============================================================

        "donnees_acces_intervenant": {
            "type": "table",

            "denomination": {
                "x": 103.08,
                "y": 442.55,
                "width": 95.44,
                "height": 22.60,
            },

            "donnees_personnelles_accedees": {
                "x": 198.78,
                "y": 442.55,
                "width": 204.57,
                "height": 22.60,
            },

            "duree": {
                "x": 403.60,
                "y": 442.55,
                "width": 130.59,
                "height": 22.60,
            },
        },

        # ============================================================
        # OPERATIONS EFFECTUEES / UTILISATIONS
        # ============================================================

        "operations_sous_traitant": {
            "type": "multiline",
            "x": 103.08,
            "y": 374.00,
            "width": 431.11,
            "height": 22.60,
        },

        # ============================================================
        # CONTRAT DE CONFIDENTIALITE ET GARANTIES
        # ============================================================

        "contrat_confidentialite": {
            "type": "table",

            "denomination": {
                "x": 103.08,
                "y": 305.45,
                "width": 95.44,
                "height": 22.60,
            },

            "date_contrat": {
                "x": 198.78,
                "y": 305.45,
                "width": 104.44,
                "height": 22.60,
            },

            "garanties_offertes": {
                "x": 303.46,
                "y": 305.45,
                "width": 230.73,
                "height": 22.60,
            },
        },

        # ============================================================
        # INFORMATION DES PERSONNES
        # ============================================================

        "personnes_informees": {
            "type": "checkbox_group",

            "non": {
                "x": 105.82,
                "y": 83.77,
                "width": 11.10,
                "height": 9.90,
            },

            "oui": {
                "x": 105.82,
                "y": 95.77,
                "width": 11.10,
                "height": 9.90,
            },

            "comment": {
                "x": 103.08,
                "y": 110.00,
                "width": 431.11,
                "height": 31.64,
            },
        },

        # ============================================================
        # DEMARCHE DE MISE EN CONFORMITE AUPRES DE L'APDP
        # ============================================================

        "mise_en_conformite_apdp": {

            "non": {
                "x": 306.82,
                "y": 222.77,
                "width": 10.40,
                "height": 9.90,
            },

            "oui": {
                "x": 306.82,
                "y": 234.77,
                "width": 10.40,
                "height": 9.90,
            },

            "references": {
                "x": 303.82,
                "y": 217.67,
                "width": 230.38,
                "height": 43.41,
            },

            "garanties": {
                "responsabilite": {
                    "x": 306.82,
                    "y": 246.77,
                    "width": 10.40,
                    "height": 9.90,
                },
                "securite": {
                    "x": 424.05,
                    "y": 246.77,
                    "width": 10.40,
                    "height": 9.90,
                },
                "confidentialite": {
                    "x": 306.82,
                    "y": 234.77,
                    "width": 10.40,
                    "height": 9.90,
                },
                "droits_personnes": {
                    "x": 306.82,
                    "y": 222.77,
                    "width": 10.40,
                    "height": 9.90,
                },
            },
        },

        # ============================================================
        # ELEMENTS GRAPHIQUES A VERIFIER AVANT GENERATION
        # ============================================================

        "zones_graphiques": {
            "zone_35": (103.08, 173.78, 431.11, 43.64),
            "zone_37": (103.08, 110.00, 431.11, 31.64),
            "zone_39": (103.08, 78.44, 430.84, 31.31),
        },
    },

    2: {

        # ============================================================
        # SECURITE ORGANISEE PAR LE SOUS-TRAITANT
        # ============================================================

        "securite_sous_traitant": {
            "type": "checkbox_group",

            "communication_pssi": {
                "x": 105.82,
                "y": 747.76,
                "width": 11.10,
                "height": 9.90,
            },

            "audits_securite": {
                "x": 105.82,
                "y": 723.76,
                "width": 11.10,
                "height": 9.90,
            },

            "mesures_organisationnelles": {
                "x": 105.82,
                "y": 711.76,
                "width": 11.10,
                "height": 9.90,
            },

            "mesures_physiques": {
                "x": 105.82,
                "y": 699.76,
                "width": 11.10,
                "height": 9.90,
            },
        },

        # ============================================================
        # DECLARATION SUR L'HONNEUR
        # ============================================================

        "declaration_honneur": {

            "nom_prenom": {
                "x": 56.94,
                "y": 625.91,
                "width": 246.15,
                "height": 22.60,
            },

            "fonction": {
                "x": 303.59,
                "y": 625.91,
                "width": 99.64,
                "height": 22.60,
            },

            "date": {
                "x": 403.73,
                "y": 625.91,
                "width": 130.46,
                "height": 22.60,
            },
        },
    },
}
