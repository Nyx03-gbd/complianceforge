"""
Mapping officiel APDP
Document : Consentement à la transmission par voie électronique

Le PDF officiel est la source de vérité.
Aucune modification de structure, de texte ou de pagination.
"""

APDP_CONSENTEMENT_ELECTRONIQUE_MAPPING = {
    "document": "consentement_transmission_electronique.pdf",
    "titre": "CONSENTEMENT A LA TRANSMISSION PAR VOIE ELECTRONIQUE",
    "pages": 3,
    "official_layout": True,
    "editable": False,

    "page_1": {

        "represente_par": {
            "type": "section",
            "nom_prenoms_raison_sociale": {
                "rect": [71.40, 263.28, 452.52, 38.28]
            },
            "rccm": {
                "rect": [71.40, 221.04, 452.52, 41.76]
            },
            "ifu": {
                "rect": [71.40, 185.40, 452.52, 35.16]
            },
            "adresse": {
                "rect": [71.40, 150.00, 452.52, 34.92]
            }
        },

        "declarant": {
            "type": "section",

            "nom_prenoms_raison_sociale": {
                "rect": [71.40, 647.76, 452.52, 36.24]
            },

            "rccm": {
                "rect": [71.40, 606.60, 452.52, 40.68]
            },

            "ifu": {
                "rect": [71.40, 570.60, 452.52, 35.52]
            },

            "adresse": {
                "rect": [71.40, 535.56, 452.52, 34.56]
            },

            "quartier_lieu_dit": {
                "rect": [71.40, 500.28, 301.56, 34.80]
            },

            "arrondissement": {
                "rect": [373.44, 500.28, 150.48, 34.68]
            },

            "commune": {
                "rect": [71.40, 465.00, 301.56, 34.68]
            },

            "pays": {
                "rect": [373.44, 465.00, 150.48, 34.68]
            },

            "telephone_portable": {
                "rect": [71.40, 429.24, 301.56, 35.28]
            },

            "boite_postale": {
                "rect": [373.44, 429.24, 150.48, 35.28]
            },

            "portable_1": {
                "rect": [71.40, 374.76, 301.56, 54.00]
            },

            "portable_2": {
                "rect": [71.40, 330.00, 150.48, 44.28]
            },

            "adresse_electronique": {
                "rect": [222.36, 330.00, 150.60, 44.28]
            }
        }
    },

    "page_2": {

        "coordonnees_reprises": {
            "type": "section",

            "quartier_lieu_dit": {
                "rect": [71.40, 728.16, 325.44, 42.36]
            },

            "arrondissement": {
                "rect": [397.32, 728.16, 126.60, 42.36]
            },

            "commune": {
                "rect": [71.40, 686.64, 325.44, 40.92]
            },

            "pays": {
                "rect": [397.32, 686.64, 126.60, 40.92]
            },

            "telephone": {
                "rect": [71.40, 650.16, 325.44, 36.00]
            },

            "boite_postale": {
                "rect": [397.32, 650.16, 126.60, 36.00]
            },

            "adresse_electronique": {
                "rect": [71.40, 608.76, 452.52, 40.80]
            }
        },

        "transmission_electronique": {

            "type": "section",

            "adresse_electronique": {
                "rect": [71.40, 563.64, 452.52, 44.64]
            },

            "messagerie_instantanee": {
                "rect": [71.40, 520.80, 452.52, 42.36]
            },

            "numero": {
                "rect": [71.40, 478.32, 452.52, 42.00]
            }
        },

        "consentements": {

            "retrait_consentement": {
                "type": "checkbox",
                "position": [94.56, 457.56]
            },

            "mise_a_jour_coordonnees": {
                "type": "checkbox",
                "position": [94.54, 396.96]
            },

            "information_utilisation_consentement": {
                "type": "checkbox",
                "position": [94.54, 336.47]
            },

            "reception_documents": {
                "type": "information_officielle",
                "position": [130.55, 300.47],
                "editable": False
            },

            "alerte_modifications_dossier": {
                "type": "information_officielle",
                "position": [130.55, 282.46],
                "editable": False
            },

            "rappel_convocation_sms_appel": {
                "type": "information_officielle",
                "position": [130.56, 246.48],
                "editable": False
            },

            "autorisation_documents_procedure": {
                "type": "texte_officiel",
                "rect": [71.40, 206.28, 452.52, 271.56],
                "editable": False
            }
        }
    },

    "page_3": {

        "procedure": {
            "type": "text",
            "rect": [71.40, 707.04, 452.52, 36.12]
        },

        "reference_dossier": {
            "type": "text",
            "rect": [71.40, 671.88, 452.52, 34.56]
        },

        "autres_references_apdp": {
            "type": "text",
            "rect": [71.40, 636.24, 452.52, 35.16],
            "editable": False
        },

        "date_signature_demande": {
            "type": "text",
            "rect": [71.40, 573.36, 452.52, 34.56]
        },

        "soussigné_prenom_nom": {
            "type": "text",
            "rect": [71.40, 518.88, 452.52, 54.00]
        },

        "fait_a": {
            "type": "text",
            "rect": [71.40, 482.40, 150.48, 36.00]
        },

        "le": {
            "type": "text",
            "rect": [222.36, 482.40, 301.56, 36.00]
        },

        "date": {
            "type": "text",
            "rect": [222.36, 426.72, 301.56, 55.20]
        },

        "signature": {
            "type": "signature",
            "rect": [71.40, 326.28, 452.52, 72.00]
        },

        "mention_legale": {
            "type": "texte_officiel",
            "rect": [71.40, 115.68, 452.52, 90.00],
            "editable": False
        }
    }
}
