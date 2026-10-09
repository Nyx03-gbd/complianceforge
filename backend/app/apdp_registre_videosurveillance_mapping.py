"""
Mapping du document officiel APDP :
MODELE DE REGISTRE DES ACTIVITES DE VIDEOSURVEILLANCE

Source :
    templates/apdp/registre_videosurveillance.pdf

Document officiel : 5 pages.

IMPORTANT :
- Le PDF original APDP n'est jamais modifié.
- Les tableaux, rubriques et exemples officiels sont conservés.
- Les zones de saisie correspondent aux cellules du document officiel.
"""

APDP_REGISTRE_VIDEOSURVEILLANCE_MAPPING = {
    "document": "registre_videosurveillance.pdf",
    "titre": "FICHE N° 001 : VIDÉO SURVEILLANCE",
    "pages": 5,
    "official_layout": True,
    "editable": False,

    # ==========================================================
    # PAGE 1
    # ==========================================================
    "page_1": {

        "references_apdp": {
            "decision": {
                "type": "text",
                "rect": [56.4, 60.4, 821.0, 15.2],
            },
            "validite": {
                "type": "text",
                "rect": [56.4, 75.5, 821.0, 15.2],
            },
        },

        "organisme": {
            "denomination": {
                "type": "text",
                "rect": [56.4, 221.9, 128.0, 15.1],
            },
            "ifu": {
                "type": "text",
                "rect": [184.4, 221.9, 128.0, 15.1],
            },
            "rccm": {
                "type": "text",
                "rect": [312.1, 221.9, 155.2, 15.1],
            },
            "telephone": {
                "type": "text",
                "rect": [467.3, 221.9, 266.5, 15.1],
            },
            "email": {
                "type": "text",
                "rect": [733.8, 221.9, 143.2, 15.1],
            },
        },

        "responsable_structure": {
            "nom_prenoms": {
                "type": "text",
                "rect": [56.4, 297.3, 128.0, 15.1],
            },
            "fonction": {
                "type": "text",
                "rect": [184.4, 297.3, 128.0, 15.1],
            },
            "adresse": {
                "type": "text",
                "rect": [312.1, 297.3, 155.2, 15.1],
            },
            "telephone": {
                "type": "text",
                "rect": [467.3, 297.3, 266.5, 15.1],
            },
            "email": {
                "type": "text",
                "rect": [733.8, 297.3, 143.2, 15.1],
            },
        },

        "delegue_protection_donnees": {
            "nom_prenoms": {
                "type": "text",
                "rect": [56.4, 388.3, 128.0, 15.1],
            },
            "fonction": {
                "type": "text",
                "rect": [184.4, 388.3, 64.0, 15.1],
            },
            "statut": {
                "type": "text",
                "rect": [248.1, 388.3, 64.0, 15.1],
            },
            "adresse": {
                "type": "text",
                "rect": [312.1, 388.3, 155.2, 15.1],
            },
            "telephone": {
                "type": "text",
                "rect": [467.3, 388.3, 266.5, 15.1],
            },
            "email": {
                "type": "text",
                "rect": [733.8, 388.3, 143.2, 15.1],
            },
        },

        "sous_traitants": {
            "table": {
                "type": "table",
                "rect": [56.4, 493.8, 821.0, 60.0],
                "columns": {
                    "structure": [56.4, 493.8, 128.0, 60.0],
                    "ifu_rccm": [184.4, 493.8, 64.0, 60.0],
                    "nip": [248.1, 493.8, 64.0, 60.0],
                    "nom": [312.1, 493.8, 73.6, 60.0],
                    "prenoms": [385.7, 493.8, 81.6, 60.0],
                    "fonction": [467.3, 493.8, 266.5, 60.0],
                    "statut": [733.8, 493.8, 143.2, 60.0],
                    "adresse": [543.3, 493.8, 73.7, 60.0],
                    "telephone": [617.0, 493.8, 66.4, 60.0],
                    "email": [683.4, 493.8, 193.6, 60.0],
                },
            },
        },
    },

    # ==========================================================
    # PAGE 2
    # ==========================================================
    "page_2": {

        "activite": {
            "code_activite": {
                "type": "text",
                "rect": [56.4, 90.5, 128.2, 14.5],
            },
            "denomination": {
                "type": "text",
                "rect": [184.4, 90.5, 693.0, 14.5],
            },
            "date_creation": {
                "type": "text",
                "rect": [56.4, 105.6, 128.2, 14.4],
            },
            "finalites": {
                "type": "multiline",
                "rect": [184.4, 105.6, 693.0, 14.4],
            },
            "categories_personnes": {
                "type": "multiline",
                "rect": [56.4, 120.0, 128.2, 14.4],
            },
            "fondement_juridique": {
                "type": "multiline",
                "rect": [184.4, 120.0, 693.0, 14.4],
            },
        },

        "principes": {

            "modalites_consentement": {
                "type": "multiline",
                "rect": [56.4, 223.2, 192.2, 43.5],
            },

            "droits_personnes": {
                "type": "multiline",
                "rect": [248.4, 223.2, 137.8, 43.5],
            },

            "modalites_exercice": {
                "type": "table",
                "rect": [386.1, 223.2, 491.4, 43.5],
                "columns": {
                    "disponibilite": [386.1, 223.2, 81.6, 43.5],
                    "mode_forme": [467.7, 223.2, 75.7, 43.5],
                    "service": [683.4, 223.2, 50.4, 43.5],
                    "delai_reponse": [733.8, 223.2, 79.2, 43.5],
                    "recours": [813.0, 223.2, 64.4, 43.5],
                },
            },

            "modification_rectification": {
                "type": "text",
                "rect": [248.4, 266.7, 137.8, 14.5],
            },
        },

        "donnees_traitees": {
            "type": "multiline",
            "rect": [56.4, 339.1, 821.0, 76.2],
        },

        "lieu_traitement": {
            "type": "multiline",
            "rect": [467.7, 414.8, 409.8, 31.7],
        },

        "visionnage": {
            "surveillance_continue": {
                "type": "multiline",
                "rect": [56.4, 446.4, 821.0, 30.7],
            },

            "organisation_continue": {
                "type": "multiline",
                "rect": [56.4, 476.9, 487.4, 15.1],
            },

            "qui": {
                "type": "text",
                "rect": [248.4, 491.8, 295.0, 15.0],
            },

            "quand": {
                "type": "text",
                "rect": [248.4, 506.4, 295.0, 15.0],
            },

            "ou": {
                "type": "text",
                "rect": [248.4, 521.4, 295.0, 15.0],
            },

            "visionnage_distance": {
                "type": "multiline",
                "rect": [56.4, 551.6, 821.0, 29.5],
            },
        },
    },

    # ==========================================================
    # PAGE 3
    # ==========================================================
    "page_3": {

        "visionnage_distance": {
            "qui": {
                "type": "text",
                "rect": [56.4, 148.4, 560.6, 29.5],
            },
            "comment": {
                "type": "text",
                "rect": [56.4, 177.8, 560.6, 29.5],
            },
            "ou": {
                "type": "text",
                "rect": [56.4, 207.1, 560.6, 29.5],
            },
        },

        "sauvegarde": {

            "table": {
                "type": "table",
                "rect": [56.4, 207.1, 560.6, 230.7],

                "columns": {
                    "date": [56.4, 207.1, 64.1, 230.7],
                    "emplacement_camera": [120.4, 207.1, 192.2, 230.7],
                    "heure_debut": [312.4, 207.1, 73.3, 230.7],
                    "heure_fin": [385.7, 207.1, 81.6, 230.7],
                    "nip_signature": [467.3, 207.1, 76.1, 230.7],
                },

                "rows": {
                    "first_data_y": 272.2,
                    "row_height": 15.1,
                    "count": 11,
                },
            },
        },

        "suppression": {

            "table": {
                "type": "table",
                "rect": [617.3, 207.1, 260.2, 230.7],

                "columns": {
                    "date": [617.3, 207.1, 66.1, 230.7],
                    "heure": [683.4, 207.1, 50.4, 230.7],
                    "nip_signature": [733.8, 207.1, 79.2, 230.7],
                    "observation": [813.0, 207.1, 64.3, 230.7],
                },

                "rows": {
                    "first_data_y": 272.2,
                    "row_height": 15.1,
                    "count": 11,
                },
            },
        },

        "consultation_tiers": {
            "table_header": {
                "type": "official_fixed_structure",
                "rect": [56.4, 536.9, 821.0, 37.7],
            },

            "colonnes": {
                "emplacement_camera": [56.4, 536.9, 192.2, 37.7],
                "heure_debut_fin": [248.4, 536.9, 64.1, 37.7],
                "ref_autorisation": [312.4, 536.9, 73.3, 37.7],
                "date_heure_visualisation": [385.7, 536.9, 81.6, 37.7],
                "finalite_raison": [467.3, 536.9, 76.1, 37.7],
                "nip": [543.4, 536.9, 73.6, 37.7],
                "nom": [617.0, 536.9, 66.4, 37.7],
                "prenoms": [683.4, 536.9, 50.4, 37.7],
                "ref_piece_identite_copie": [733.8, 536.9, 143.2, 37.7],
            },

            "data_rows": {
                "first_data_y": 574.4,
                "row_height": 15.1,
                "count": 11,
            },
        },
    },

    # ==========================================================
    # PAGE 4
    # ==========================================================
    "page_4": {

        "consultation_tiers_continuation": {
            "table": {
                "type": "table",
                "rect": [56.4, 60.4, 821.0, 167.9],
                "columns": {
                    "emplacement_camera": [56.4, 60.4, 192.2, 167.9],
                    "heure_debut_fin": [248.4, 60.4, 64.1, 167.9],
                    "ref_autorisation": [312.4, 60.4, 73.3, 167.9],
                    "date_heure_visualisation": [385.7, 60.4, 81.6, 167.9],
                    "finalite_raison": [467.3, 60.4, 76.1, 167.9],
                    "nip": [543.4, 60.4, 73.6, 167.9],
                    "nom": [617.0, 60.4, 66.4, 167.9],
                    "prenoms": [683.4, 60.4, 50.4, 167.9],
                    "ref_piece_identite_copie": [733.8, 60.4, 143.2, 167.9],
                },

                "rows": {
                    "first_row_y": 60.4,
                    "row_height": 15.1,
                    "count": 11,
                },
            },
        },

        "securite": {

            "titre": {
                "type": "official_fixed_text",
                "rect": [56.4, 243.2, 821.0, 19.2],
            },

            "table": {
                "type": "table",
                "rect": [56.4, 292.5, 821.0, 301.1],
            },

            "controle_acces_utilisateurs": {
                "type": "text",
                "rect": [56.4, 292.5, 256.2, 54.0],
            },

            "reponse_controle_acces": {
                "type": "multiline",
                "rect": [617.3, 292.5, 260.0, 54.0],
            },

            "mesures_tracabilite": {
                "type": "text",
                "rect": [56.4, 346.5, 256.2, 54.0],
            },

            "reponse_tracabilite": {
                "type": "multiline",
                "rect": [617.3, 346.5, 260.0, 54.0],
            },

            "protection_logiciels": {
                "type": "text",
                "rect": [56.4, 400.5, 256.2, 54.0],
            },

            "reponse_protection_logiciels": {
                "type": "multiline",
                "rect": [617.3, 400.5, 260.0, 54.0],
            },

            "chiffrement_donnees": {
                "type": "text",
                "rect": [56.4, 454.5, 256.2, 75.0],
            },

            "reponse_chiffrement": {
                "type": "multiline",
                "rect": [617.3, 454.5, 260.0, 75.0],
            },

            "controle_sous_traitants": {
                "type": "text",
                "rect": [56.4, 529.5, 256.2, 64.1],
            },

            "reponse_controle_sous_traitants": {
                "type": "multiline",
                "rect": [617.3, 529.5, 260.0, 64.1],
            },

            "exemples_reponses": {
                "type": "official_fixed_text",
                "editable": False,
                "rect": [312.4, 292.5, 305.0, 301.1],
            },
        },
    },

    # ==========================================================
    # PAGE 5
    # ==========================================================
    "page_5": {

        "controle_sous_traitants_suite": {
            "type": "official_table_continuation",
            "rect": [56.4, 60.4, 561.0, 98.0],

            "mesure": {
                "type": "official_fixed_text",
                "rect": [56.4, 60.4, 256.2, 98.0],
            },

            "exemple_reponse": {
                "type": "official_fixed_text",
                "rect": [312.4, 60.4, 305.0, 98.0],
            },

            "reponse": {
                "type": "multiline",
                "rect": [617.3, 60.4, 260.0, 98.0],
            },
        },

        "autres": {
            "type": "multiline",
            "rect": [56.4, 143.0, 821.0, 15.2],
        },
    },

    # ==========================================================
    # PRESERVATION
    # ==========================================================
    "regle_preservation": {
        "source_of_truth": "PDF APDP officiel",
        "preserve_official_structure": True,
        "preserve_official_tables": True,
        "preserve_official_text": True,
        "preserve_official_examples": True,
        "preserve_pagination": True,
        "preserve_header": True,
        "preserve_footer": True,
        "do_not_simplify": True,
        "do_not_invent_missing_fields": True,
        "source_pdf_must_not_be_modified": True,
    },
}
