"""
Mapping officiel APDP
FORMULAIRE DE SIGNALEMENT

Le PDF officiel est la source de vérité.
Aucune modification de structure, texte ou pagination.
"""

APDP_SIGNALEMENT_MAPPING = {
    "document": "formulaire_signalement.pdf",
    "titre": "FORMULAIRE DE SIGNALEMENT",
    "pages": 4,
    "official_layout": True,
    "editable": False,

    "page_1": {
        "identification": {
            "sexe": {
                "type": "checkbox_group",
                "madame": [76.56, 465.24],
                "monsieur": [229.00, 465.24],
            },

            "nom_famille": {
                "type": "text",
                "rect": [71.40, 413.40, 452.52, 34.68],
            },

            "prenoms": {
                "type": "text",
                "rect": [71.40, 371.40, 452.52, 41.52],
            },

            "adresse": {
                "type": "text",
                "rect": [71.40, 335.88, 452.52, 35.04],
            },

            "quartier_lieu_dit": {
                "type": "text",
                "rect": [71.40, 292.68, 341.40, 42.60],
            },

            "arrondissement": {
                "type": "text",
                "rect": [413.40, 292.68, 110.52, 42.60],
            },

            "commune": {
                "type": "text",
                "rect": [71.40, 251.04, 341.40, 41.16],
            },

            "pays": {
                "type": "text",
                "rect": [413.40, 251.04, 110.52, 41.16],
            },

            "telephone_portable": {
                "type": "text",
                "rect": [71.40, 202.80, 341.40, 47.76],
            },

            "boite_postale": {
                "type": "text",
                "rect": [413.40, 202.80, 110.52, 47.76],
            },

            "adresse_electronique": {
                "type": "text",
                "rect": [71.40, 157.68, 452.52, 44.64],
            },
        },

        "types_violation": {
            "traitement_non_autorise": {
                "type": "checkbox",
                "position": [76.56, 94.56],
            },

            "changement_finalite_sans_consentement": {
                "type": "checkbox",
                "position": [76.56, 77.16],
            },
        },
    },

    "page_2": {
        "types_violation_suite": {
            "detournement_finalite": {
                "type": "checkbox",
                "position": [76.56, 703.44],
            },

            "prospection_directe_illegale": {
                "type": "checkbox",
                "position": [76.56, 686.04],
            },

            "transfert_etat_tiers_sans_autorisation": {
                "type": "checkbox",
                "position": [76.55, 668.63],
            },

            "absence_garantie_droits": {
                "type": "checkbox",
                "position": [76.53, 636.47],
            },

            "conservation_duree_excessive": {
                "type": "checkbox",
                "position": [76.53, 575.14],
            },

            "violation_disponibilite_integrite_confidentialite": {
                "type": "checkbox",
                "position": [76.52, 528.46],
            },

            "refus_reclamations_droits": {
                "type": "checkbox",
                "position": [76.52, 481.78],
            },

            "autres": {
                "type": "checkbox_text",
                "position": [76.56, 464.28],
                "text_rect": [71.40, 448.56, 452.52, 30.72],
            },
        },

        "information_violation": {
            "auteur_presume": {
                "nom_prenoms_denomination": {
                    "type": "text",
                    "rect": [71.40, 349.92, 452.52, 29.28],
                },

                "ville": {
                    "type": "text",
                    "rect": [71.40, 334.80, 332.40, 14.64],
                },

                "pays": {
                    "type": "text",
                    "rect": [404.28, 334.80, 119.64, 14.64],
                },

                "contact": {
                    "type": "text",
                    "rect": [71.40, 319.68, 332.40, 14.64],
                },
            },

            "date_heure_lieu": {
                "date_heure_violation": {
                    "type": "text",
                    "rect": [71.40, 304.56, 452.52, 14.64],
                },

                "date_heure_constatation": {
                    "type": "text",
                    "rect": [71.40, 274.80, 452.52, 29.28],
                },

                "lieu_violation": {
                    "type": "text",
                    "rect": [71.40, 259.68, 452.52, 14.64],
                },
            },

            "resume_incident": {
                "type": "multiline_text",
                "rect": [71.40, 155.76, 452.52, 73.20],
            },
        },
    },

    "page_3": {
        "donnees_personnelles_concernees": {
            "type": "multiline_text",
            "rect": [71.40, 627.48, 452.52, 60.24],
        },

        "consequences_potentielles": {
            "detenues_stockees_utilisees_illicitement": {
                "type": "checkbox",
                "position": [76.56, 523.44],
            },

            "diffusion_excessive": {
                "type": "checkbox",
                "position": [76.56, 491.40],
            },

            "correlation_avec_autres_informations": {
                "type": "checkbox",
                "position": [76.56, 430.07],
            },

            "exploitation_autres_fins": {
                "type": "checkbox",
                "position": [76.56, 368.75],
            },

            "donnees_modifiees_invalides": {
                "type": "checkbox",
                "position": [76.56, 307.42],
            },

            "donnees_modifiees_autres_donnees_valides": {
                "type": "checkbox",
                "position": [76.56, 231.45],
            },

            "donnees_manquantes_service_indisponible": {
                "type": "checkbox",
                "position": [76.56, 170.12],
            },

            "donnees_manquantes_service_different": {
                "type": "checkbox",
                "position": [76.56, 94.20],
            },
        },
    },

    "page_4": {
        "suite_consequences": {
            "type": "texte_officiel",
            "editable": False,
            "rect": [71.40, 688.32, 452.52, 29.16],
        },

        "observations_techniques": {
            "type": "multiline_text",
            "rect": [71.40, 567.24, 452.52, 60.24],
        },

        "pieces": {
            "type": "section",

            "piece_1": {
                "type": "text",
                "position": [76.56, 518.00],
            },

            "piece_2": {
                "type": "text",
                "position": [76.56, 503.00],
            },

            "piece_3": {
                "type": "text",
                "position": [76.56, 488.00],
            },

            "piece_4": {
                "type": "text",
                "position": [76.56, 473.00],
            },
        },
    },
}
