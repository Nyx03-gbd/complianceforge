"""
Mapping du document officiel APDP :
REGISTRE DES ACTIVITES DE TRAITEMENT

Source :
    templates/apdp/registre_activites_traitement.pdf

Document officiel : 4 pages.

IMPORTANT :
- Le PDF APDP original ne doit jamais être modifié.
- La structure officielle des tableaux est conservée.
- Les rubriques et intitulés officiels sont conservés.
- Les coordonnées correspondent au PDF source.
"""

APDP_REGISTRE_ACTIVITES_MAPPING = {
    "document": "registre_activites_traitement.pdf",
    "titre": "REGISTRE DES ACTIVITES DE TRAITEMENT",
    "pages": 4,
    "official_layout": True,
    "editable": False,

    # ==========================================================
    # PAGE 1
    # ==========================================================
    "page_1": {

        "identification_traitement": {
            "fiche": {
                "type": "text",
                "rect": [122.76, 54.73, 594.12, 9.24],
            },
        },

        "organisme": {
            "denomination": {
                "type": "text",
                "rect": [122.76, 385.09, 126.96, 21.24],
            },
            "ifu": {
                "type": "text",
                "rect": [249.60, 385.09, 467.28, 21.24],
            },
            "rccm": {
                "type": "text",
                "rect": [122.76, 406.21, 594.12, 27.00],
            },
            "telephone": {
                "type": "text",
                "rect": [122.76, 433.09, 594.12, 22.92],
            },
            "email": {
                "type": "text",
                "rect": [122.76, 455.89, 594.12, 9.72],
            },
        },

        "responsable_structure": {
            "nom_prenoms": {
                "type": "text",
                "rect": [122.76, 309.37, 594.12, 44.28],
            },
            "fonction": {
                "type": "text",
                "rect": [122.76, 353.53, 594.12, 22.08],
            },
            "adresse": {
                "type": "text",
                "rect": [122.76, 375.49, 594.12, 9.72],
            },
            "telephone": {
                "type": "text",
                "rect": [122.76, 385.09, 126.96, 21.24],
            },
            "email": {
                "type": "text",
                "rect": [249.60, 385.09, 467.28, 21.24],
            },
        },

        "delegue_protection_donnees": {
            "nom_prenoms": {
                "type": "text",
                "rect": [122.76, 465.49, 126.96, 20.76],
            },
            "fonction": {
                "type": "text",
                "rect": [249.60, 465.49, 467.28, 20.76],
            },
            "statut": {
                "type": "text",
                "rect": [122.76, 486.13, 126.96, 34.68],
            },
            "adresse": {
                "type": "text",
                "rect": [249.60, 486.13, 467.28, 34.68],
            },
            "telephone": {
                "type": "text",
                "rect": [122.76, 503.17, 594.12, 17.28],
            },
            "email": {
                "type": "text",
                "rect": [122.76, 520.45, 594.12, 0.60],
            },
        },

        "activite": {
            "code_activite": {
                "type": "text",
                "rect": [122.76, 465.49, 126.96, 20.76],
            },
            "denomination_description": {
                "type": "multiline",
                "rect": [249.60, 465.49, 467.28, 34.68],
            },
            "date_creation": {
                "type": "text",
                "rect": [122.76, 503.17, 594.12, 17.28],
            },
            "rccm": {
                "type": "text",
                "rect": [122.76, 520.45, 594.12, 0.60],
            },
            "references_decision_apdp": {
                "type": "text",
                "rect": [122.76, 54.73, 594.12, 9.24],
            },
            "validite": {
                "type": "text",
                "rect": [122.76, 63.85, 594.12, 54.36],
            },
        },
    },

    # ==========================================================
    # PAGE 2
    # ==========================================================
    "page_2": {

        "principes_traitement": {

            "finalites": {
                "type": "multiline",
                "rect": [122.76, 54.73, 126.96, 51.48],
            },

            "categories_personnes": {
                "type": "multiline",
                "rect": [249.60, 54.73, 467.28, 51.48],
            },

            "fondement_juridique": {
                "type": "multiline",
                "rect": [122.76, 115.69, 594.12, 17.40],
            },

            "modalites_consentement": {
                "type": "multiline",
                "rect": [122.76, 142.57, 198.00, 29.28],
            },

            "droits_personnes": {
                "type": "multiline",
                "rect": [320.64, 142.57, 123.00, 29.28],
            },

            "disponibilite": {
                "type": "text",
                "rect": [443.52, 142.57, 273.36, 29.28],
            },

            "modalites_exercice_droits": {
                "type": "multiline",
                "rect": [122.76, 192.25, 594.12, 81.48],
            },

            "service": {
                "type": "text",
                "rect": [122.76, 300.49, 256.92, 16.56],
            },

            "delai_reponse": {
                "type": "text",
                "rect": [379.56, 300.49, 337.32, 16.56],
            },

            "recours": {
                "type": "text",
                "rect": [122.76, 316.93, 126.96, 30.72],
            },
        },

        "donnees_traitees": {

            "classifications": {
                "type": "table",
                "rect": [122.76, 347.53, 594.12, 172.92],

                "columns": {
                    "types_categories": [122.76, 347.53, 126.96, 172.92],
                    "donnees_simples": [249.60, 347.53, 130.08, 172.92],
                    "donnees_sensibles": [379.56, 347.53, 173.40, 172.92],
                    "regimes_speciaux": [552.84, 347.53, 164.04, 172.92],
                },
            },

            "identification": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "vie_personnelle": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "vie_professionnelle": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "donnees_economiques_financieres": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "donnees_sociales": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "donnees_localisation": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "internet_navigation": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },

            "donnees_connectivite": {
                "type": "checkbox_or_text",
                "rect": [122.76, 347.53, 126.96, 172.92],
            },
        },
    },

    # ==========================================================
    # PAGE 3
    # ==========================================================
    "page_3": {

        "cibles_personnes_concernees": {
            "type": "multiline",
            "rect": [122.76, 98.41, 594.12, 75.36],
        },

        "duree_conservation": {
            "type": "table",
            "rect": [122.76, 233.17, 594.12, 34.68],

            "columns": {
                "duree": [122.76, 233.17, 126.96, 34.68],
                "donnees_simples": [249.60, 233.17, 130.08, 34.68],
                "donnees_sensibles": [379.56, 233.17, 173.40, 34.68],
                "regimes_speciaux": [552.84, 233.17, 164.04, 34.68],
            },
        },

        "dispositions_legales": {
            "type": "text",
            "rect": [122.76, 267.73, 594.12, 9.72],
        },

        "dispositions_conventionnelles": {
            "type": "text",
            "rect": [122.76, 277.33, 594.12, 26.76],
        },

        "personnes_acces_traitement": {
            "type": "table",
            "rect": [122.76, 313.57, 594.12, 25.80],

            "columns": {
                "nom_prenoms_denomination": [122.76, 313.57, 126.96, 25.80],
                "fonction": [249.60, 313.57, 130.08, 25.80],
                "nature_juridique_rapport": [379.56, 313.57, 173.40, 25.80],
                "contacts_adresses": [552.84, 313.57, 164.04, 25.80],
            },
        },

        "communication_donnees_benin": {

            "nom_prenom_denomination": {
                "type": "multiline",
                "rect": [122.76, 54.73, 126.96, 16.92],
            },

            "contacts_adresses": {
                "type": "multiline",
                "rect": [249.60, 54.73, 130.08, 16.92],
            },

            "accord_communication": {
                "type": "multiline",
                "rect": [379.56, 54.73, 173.40, 16.92],
            },

            "texte_legal_reglementaire": {
                "type": "multiline",
                "rect": [552.84, 54.73, 164.04, 16.92],
            },

            "finalite_communication": {
                "type": "multiline",
                "rect": [122.76, 81.13, 594.12, 17.40],
            },

            "reference_contrat_confidentialite": {
                "type": "text",
                "rect": [122.76, 98.41, 594.12, 75.36],
            },
        },
    },

    # ==========================================================
    # PAGE 4
    # ==========================================================
    "page_4": {

        "transfert_pays_tiers": {

            "donnees_transferees": {
                "type": "multiline",
                "rect": [122.76, 54.73, 126.96, 26.52],
            },

            "destination": {
                "type": "multiline",
                "rect": [249.60, 54.73, 130.08, 25.92],
            },

            "support_juridique": {
                "type": "multiline",
                "rect": [379.56, 54.73, 173.40, 26.52],
            },

            "identification_destinataire": {
                "type": "multiline",
                "rect": [122.76, 116.53, 126.96, 28.56],
            },

            "modalites_techniques_transfert": {
                "type": "multiline",
                "rect": [249.60, 116.53, 130.08, 28.56],
            },

            "finalite_donnees_transferees": {
                "type": "multiline",
                "rect": [379.56, 116.53, 173.40, 28.56],
            },
        },

        "securite": {

            "mesures_tracabilite": {
                "type": "multiline",
                "rect": [122.76, 216.01, 126.96, 162.84],
            },

            "procedures_environnementales": {
                "type": "multiline",
                "rect": [122.76, 144.97, 594.12, 53.88],
            },

            "controle_acces_utilisateurs": {
                "type": "multiline",
                "rect": [249.36, 216.37, 0.60, 162.84],
            },

            "protection_logiciels": {
                "type": "multiline",
                "rect": [379.32, 216.37, 0.60, 162.84],
            },

            "sauvegarde_donnees": {
                "type": "multiline",
                "rect": [503.28, 216.37, 0.60, 162.84],
            },

            "chiffrement_donnees": {
                "type": "multiline",
                "rect": [608.64, 216.37, 0.60, 162.84],
            },

            "controle_sous_traitants": {
                "type": "multiline",
                "rect": [661.56, 216.37, 0.60, 162.84],
            },

            "autres_mesures": {
                "type": "multiline",
                "rect": [122.76, 249.61, 594.12, 139.32],
            },

            "antivirus_parefeu_mises_a_jour_tests": {
                "type": "multiline",
                "rect": [443.28, 216.37, 60.60, 162.84],
            },

            "mesures_protection_logiciels": {
                "type": "multiline",
                "rect": [379.32, 216.37, 124.00, 162.84],
            },

            "description_mesures": {
                "type": "multiline",
                "rect": [122.76, 249.61, 594.12, 139.32],
            },
        },
    },

    # ==========================================================
    # PRESERVATION DU DOCUMENT OFFICIEL
    # ==========================================================
    "regle_preservation": {
        "source_of_truth": "PDF APDP officiel",
        "preserve_official_structure": True,
        "preserve_official_tables": True,
        "preserve_official_text": True,
        "preserve_pagination": True,
        "preserve_header": True,
        "preserve_footer": True,
        "do_not_simplify": True,
        "do_not_invent_missing_fields": True,
        "source_pdf_must_not_be_modified": True,
    },
}
