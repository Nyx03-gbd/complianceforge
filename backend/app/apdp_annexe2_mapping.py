"""
Mapping officiel — Annexe 2 APDP : COMMUNICATION.

IMPORTANT :
- Le PDF officiel APDP est la source de vérité.
- Le PDF original n'est jamais modifié.
- Les coordonnées servent uniquement à la superposition.
- Les rubriques officielles ne sont ni simplifiées ni renommées.
"""

ANNEXE_2_COMMUNICATION_MAPPING = {

    # ================================================================
    # PAGE 1
    # ================================================================

    1: {

        # ------------------------------------------------------------
        # DESTINATAIRES SITUES AU BENIN
        # ------------------------------------------------------------

        "destinataires_benin": {
            "type": "table",

            "columns": {
                "denomination": {
                    "x": 103.46,
                    "y": 557.18,
                    "width": 94.69,
                    "height": 21.85,
                },
                "contacts": {
                    "x": 199.15,
                    "y": 557.18,
                    "width": 103.69,
                    "height": 21.85,
                },
                "representant": {
                    "x": 303.84,
                    "y": 557.18,
                    "width": 99.14,
                    "height": 21.85,
                },
                "donnees_communiquees": {
                    "x": 403.98,
                    "y": 557.18,
                    "width": 129.84,
                    "height": 21.85,
                },
            },

            "rows": [
                {
                    "denomination": (103.46, 557.18, 94.69, 21.85),
                    "contacts": (199.15, 557.18, 103.69, 21.85),
                    "representant": (303.84, 557.18, 99.14, 21.85),
                    "donnees_communiquees": (403.98, 557.18, 129.84, 21.85),
                },
                {
                    "denomination": (103.46, 534.33, 94.69, 21.85),
                    "contacts": (199.15, 534.33, 103.69, 21.85),
                    "representant": (303.84, 534.33, 99.14, 21.85),
                    "donnees_communiquees": (403.98, 534.33, 129.84, 21.85),
                },
            ],
        },

        # ------------------------------------------------------------
        # DESTINATAIRES SITUES DANS UN PAYS DE LA CEDEAO
        # ------------------------------------------------------------

        "destinataires_cedeao": {
            "type": "table",

            "columns": {
                "denomination": {
                    "x": 103.46,
                    "y": 420.08,
                    "width": 94.69,
                    "height": 21.85,
                },
                "contacts": {
                    "x": 199.15,
                    "y": 420.08,
                    "width": 103.69,
                    "height": 21.85,
                },
                "representant": {
                    "x": 303.84,
                    "y": 420.08,
                    "width": 99.14,
                    "height": 21.85,
                },
                "donnees_communiquees": {
                    "x": 403.98,
                    "y": 420.08,
                    "width": 129.84,
                    "height": 21.85,
                },
            },

            "rows": [
                {
                    "denomination": (103.46, 420.08, 94.69, 21.85),
                    "contacts": (199.15, 420.08, 103.69, 21.85),
                    "representant": (303.84, 420.08, 99.14, 21.85),
                    "donnees_communiquees": (403.98, 420.08, 129.84, 21.85),
                },
                {
                    "denomination": (103.46, 442.93, 94.69, 21.85),
                    "contacts": (199.15, 442.93, 103.69, 21.85),
                    "representant": (303.84, 442.93, 99.14, 21.85),
                    "donnees_communiquees": (403.98, 442.93, 129.84, 21.85),
                },
            ],
        },

        # ------------------------------------------------------------
        # FINALITE DE LA COMMUNICATION
        # ------------------------------------------------------------

        "finalite_communication": {
            "type": "multiline",
            "x": 103.08,
            "y": 351.15,
            "width": 431.11,
            "height": 22.60,
        },

        # ------------------------------------------------------------
        # TEXTE LEGAL OU REGLEMENTAIRE
        # ------------------------------------------------------------

        "texte_legal_reglementaire": {
            "type": "multiline",
            "x": 103.08,
            "y": 296.41,
            "width": 431.11,
            "height": 31.64,
        },

        # ------------------------------------------------------------
        # CONSENTEMENT PREALABLE
        # ------------------------------------------------------------

        "consentement_prealable": {

            "type": "checkbox_group",

            "oui": {
                "x": 105.82,
                "y": 269.77,
                "width": 12.45,
                "height": 9.90,
            },

            "non": {
                "x": 105.82,
                "y": 281.77,
                "width": 12.45,
                "height": 9.90,
            },

            "texte_consentement": {
                "x": 103.08,
                "y": 264.52,
                "width": 430.84,
                "height": 31.55,
            },
        },

        # ------------------------------------------------------------
        # BASE JUSTIFIANT LA COMMUNICATION
        # ------------------------------------------------------------

        "base_communication": {
            "type": "checkbox_group",

            "responsabilite_obligation_legale": {
                "x": 201.82,
                "y": 214.77,
                "width": 12.45,
                "height": 9.90,
            },

            "mission_interet_public": {
                "x": 201.82,
                "y": 190.77,
                "width": 12.45,
                "height": 9.90,
            },

            "contrat_mesures_precontractuelles": {
                "x": 201.82,
                "y": 154.77,
                "width": 12.45,
                "height": 9.90,
            },

            "interets_fondamentaux_vie_privee": {
                "x": 201.82,
                "y": 118.77,
                "width": 12.45,
                "height": 9.90,
            },

            "autre_justification": {
                "x": 201.82,
                "y": 94.77,
                "width": 12.45,
                "height": 9.90,
            },

            "justification": {
                "type": "multiline",
                "x": 198.82,
                "y": 89.78,
                "width": 335.38,
                "height": 151.29,
            },
        },
    },

    # ================================================================
    # PAGE 2
    # ================================================================

    2: {

        # ------------------------------------------------------------
        # MODALITES DE LA COMMUNICATION
        # ------------------------------------------------------------

        "modalites_communication": {
            "type": "multiline",
            "x": 103.08,
            "y": 694.46,
            "width": 431.11,
            "height": 22.60,
        },

        # ------------------------------------------------------------
        # MESURES DE SECURITE
        # ------------------------------------------------------------

        "mesures_securite_communication": {
            "type": "multiline",
            "x": 103.08,
            "y": 639.72,
            "width": 431.11,
            "height": 22.60,
        },

        # ------------------------------------------------------------
        # INFORMATION PREALABLE SUR LA COMMUNICATION
        # ------------------------------------------------------------

        "information_prealable": {

            "oui_non": {
                "type": "checkbox_group",

                "oui": {
                    "x": 105.82,
                    "y": 557.76,
                    "width": 11.10,
                    "height": 9.90,
                },

                "non": {
                    "x": 257.96,
                    "y": 557.76,
                    "width": 11.10,
                    "height": 9.90,
                },
            },

            "contenu": {
                "type": "multiline",
                "x": 103.08,
                "y": 552.43,
                "width": 430.84,
                "height": 43.15,
            },

            "modalites": {
                "type": "checkbox_group",

                "affichage": {
                    "x": 105.82,
                    "y": 445.76,
                    "width": 12.45,
                    "height": 9.90,
                },

                "mentions_ecrites": {
                    "x": 249.95,
                    "y": 445.76,
                    "width": 12.45,
                    "height": 9.90,
                },

                "entretien": {
                    "x": 419.95,
                    "y": 445.76,
                    "width": 12.45,
                    "height": 9.90,
                },

                "autres": {
                    "x": 105.82,
                    "y": 433.76,
                    "width": 12.45,
                    "height": 9.90,
                },
            },

            "autres_modalites": {
                "type": "text",
                "x": 103.08,
                "y": 428.43,
                "width": 430.84,
                "height": 55.36,
            },

            "preuve": {
                "type": "checkbox_group",

                "cle_usb": {
                    "x": 105.82,
                    "y": 679.76,
                    "width": 12.45,
                    "height": 9.90,
                },

                "transmission_electronique": {
                    "x": 192.06,
                    "y": 679.76,
                    "width": 12.45,
                    "height": 9.90,
                },

                "autres": {
                    "x": 105.82,
                    "y": 667.76,
                    "width": 12.45,
                    "height": 9.90,
                },
            },
        },

        # ------------------------------------------------------------
        # METHODE D'OBTENTION DU CONSENTEMENT
        # ------------------------------------------------------------

        "methode_consentement": {
            "type": "checkbox_group",

            "ecrit": {
                "x": 201.82,
                "y": 734.76,
                "width": 12.45,
                "height": 9.90,
            },

            "oral": {
                "x": 289.28,
                "y": 734.76,
                "width": 12.45,
                "height": 9.90,
            },

            "acceptation_electronique": {
                "x": 375.52,
                "y": 734.76,
                "width": 12.45,
                "height": 9.90,
            },

            "autres": {
                "x": 201.82,
                "y": 722.76,
                "width": 12.45,
                "height": 9.90,
            },
        },

        # ------------------------------------------------------------
        # DECLARATION SUR L'HONNEUR
        # ------------------------------------------------------------

        "declaration_honneur": {
            "nom_prenom": {
                "x": 56.94,
                "y": 313.91,
                "width": 246.15,
                "height": 22.60,
            },

            "fonction": {
                "x": 303.59,
                "y": 313.91,
                "width": 99.64,
                "height": 22.60,
            },

            "date": {
                "x": 403.73,
                "y": 313.91,
                "width": 130.46,
                "height": 22.60,
            },
        },
    },
}
