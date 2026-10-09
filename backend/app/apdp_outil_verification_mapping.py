"""
Mapping du document officiel APDP :

    OUTIL DE VERIFICATION DU REMPLISSAGE DU FORMULAIRE
    DE DECLARATION — TRAITEMENT DES VIDEO-SURVEILLANCES

Source :
    templates/apdp/outil_verification.pdf

Document officiel : 5 pages.

IMPORTANT
---------
Le PDF APDP est la source de vérité.

Ce module :
- conserve la pagination officielle ;
- conserve les rubriques et critères officiels ;
- conserve les colonnes de vérification ;
- ne simplifie pas les critères ;
- ne crée aucun critère supplémentaire ;
- ne modifie jamais le PDF original.

Les coordonnées sont exprimées dans le repère PDF :
    x, y = origine en haut à gauche
    width, height = dimensions de la zone
"""

PAGE_WIDTH = 1185.97
PAGE_HEIGHT = 838.31

APDP_OUTIL_VERIFICATION_MAPPING = {
    "document": "outil_verification.pdf",
    "title": "Vérification du remplissage du formulaire de déclaration",
    "subtitle": "TRAITEMENT DES VIDEO-SURVEILLANCES",
    "pages": 5,

    "coordinate_system": {
        "origin": "top-left",
        "page_width": PAGE_WIDTH,
        "page_height": PAGE_HEIGHT,
    },

    # =========================================================
    # STRUCTURE OFFICIELLE DES COLONNES
    # =========================================================

    "columns": {
        "numero": {
            "x": 129.32,
            "width": 129.83,
        },

        "rubrique": {
            "x": 259.15,
            "width": 308.47,
        },

        "disponible": {
            "x": 567.45,
            "width": 156.53,
        },

        "note": {
            "x": 672.27,
            "width": 51.71,
        },

        "note_reservee": {
            "x": 723.98,
            "width": 70.85,
        },

        "observations": {
            "x": 795.33,
            "width": 246.45,
        },
    },

    # =========================================================
    # PAGE 1
    # =========================================================

    "page_1": {
        "rect": [129.32, 76.08, 912.46, 630.15],

        "sections": {

            "1": {
                "title": "IDENTITE DU RESPONSABLE DE TRAITEMENT",

                "criteria": {
                    "1-1": {
                        "label": "Identité du déclarant RCCM / IFU / CIP",
                        "rect": [129.32, 244.78, 912.46, 30.59],
                        "note": 3,
                    },

                    "1-2": {
                        "label": "Personne à contacter par l’APDP en cas de besoin (DPO)",
                        "rect": [129.32, 305.65, 912.46, 29.07],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 334.55, 912.46, 12.68],
                    "note": 5,
                },
            },

            "2": {
                "title": "FINALITES DU SYSTÈME",

                "criteria": {
                    "2-1": {
                        "label": "Finalités",
                        "rect": [129.32, 386.95, 912.46, 18.25],
                        "note": 3,
                    },

                    "2-2": {
                        "label": "Base Juridique du traitement",
                        "rect": [129.32, 405.03, 912.46, 36.36],
                        "note": 1,
                    },
                },

                "total": {
                    "rect": [129.32, 453.56, 912.46, 12.51],
                    "note": 4,
                },
            },

            "3": {
                "title": "LOCALISATION DU SYSTÈME",

                "criteria": {
                    "3-1": {
                        "label": "Lieu d’installation du système de vidéosurveillance",
                        "rect": [129.32, 481.11, 912.46, 76.25],
                        "note": 10,
                    },

                    "3-2": {
                        "label": "Plan d’installation des caméras",
                        "rect": [129.32, 557.19, 912.46, 15.38],
                        "note": 2,
                    },

                    "3-3": {
                        "label": "Emplacement des caméras",
                        "rect": [129.32, 572.40, 912.46, 15.38],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 602.83, 912.46, 15.38],
                    "note": 14,
                },
            },

            "4": {
                "title": "CARACTERISTIQUES ET FONCTIONNALITÉS DU SYSTEME",

                "criteria": {
                    "4-1": {
                        "label": "Date de mise en œuvre du système",
                        "rect": [129.32, 655.39, 308.47, 26.73],
                        "note": 1,
                    },

                    "4-2": {
                        "label": "Visualisation des images en temps réel",
                        "rect": [129.32, 696.65, 308.47, 29.58],
                        "note": 1,
                    },
                },
            },
        },
    },

    # =========================================================
    # PAGE 2
    # =========================================================

    "page_2": {
        "rect": [129.32, 76.08, 912.46, 653.69],

        "sections": {

            "4": {
                "title": "CARACTERISTIQUES ET FONCTIONNALITÉS DU SYSTEME",

                "criteria": {
                    "4-3": {
                        "label": "Prise de son",
                        "rect": [129.32, 76.08, 912.46, 14.37],
                        "note": 1,
                    },

                    "4-4": {
                        "label": "Enregistrement",
                        "rect": [129.32, 90.44, 912.46, 14.37],
                        "note": 1,
                    },

                    "4-5": {
                        "label": "Support de l’enregistreur",
                        "rect": [129.32, 105.15, 912.46, 14.37],
                        "note": 1,
                    },

                    "4-6": {
                        "label": "Nature de la camera",
                        "rect": [129.32, 134.55, 912.46, 29.07],
                        "note": 2,
                    },

                    "4-7": {
                        "label": "Liaison et Réseau",
                        "rect": [129.32, 149.26, 912.46, 29.07],
                        "note": 2,
                    },

                    "4-8": {
                        "label": "Résolution du capteur",
                        "rect": [129.32, 186.13, 912.46, 43.30],
                        "note": 1,
                    },

                    "4-9a": {
                        "label": "Utilisation de systèmes experts",
                        "rect": [129.32, 283.49, 912.46, 29.07],
                        "note": 1,
                    },

                    "4-9b": {
                        "label": "Accès aux images à distance",
                        "rect": [129.32, 326.26, 912.46, 29.07],
                        "note": 1,
                    },

                    "4-10": {
                        "label": "Durée de conservation des images",
                        "rect": [129.32, 384.41, 912.46, 14.87],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 355.51, 912.46, 29.07],
                    "note": 15,
                },
            },

            "5": {
                "title": "DONNÉES COLLECTÉES ET TRAITÉES",

                "criteria": {
                    "5": {
                        "label": "Données collectées et traitées",
                        "rect": [129.32, 399.12, 912.46, 14.87],
                        "note": 4,
                    },
                },

                "total": {
                    "rect": [129.32, 428.04, 912.46, 14.37],
                    "note": 4,
                },
            },

            "6": {
                "title": "TRANSFERT DES DONNEES VERS UN PAYS TIERS",

                "criteria": {
                    "6-1": {
                        "label": "Identité du destinataire des données",
                        "rect": [129.32, 442.24, 912.46, 15.38],
                        "note": 2,
                    },

                    "6-2": {
                        "label": "Type de destinataire / lien juridique avec le responsable de traitement",
                        "rect": [129.32, 457.45, 912.46, 106.67],
                        "note": 2,
                    },

                    "6-3": {
                        "label": "Finalité du transfert à l’étranger envisagé",
                        "rect": [129.32, 563.95, 912.46, 22.31],
                        "note": 2,
                    },

                    "6-4": {
                        "label": "Nature des traitements opérés par le destinataire des données",
                        "rect": [129.32, 586.09, 912.46, 41.58],
                        "note": 2,
                    },

                    "6-5": {
                        "label": "Fondement juridique au transfert",
                        "rect": [129.32, 627.50, 912.46, 24.00],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 651.34, 543.45, 78.95],
                    "note": 2,
                },
            },
        },
    },

    # =========================================================
    # PAGE 3
    # =========================================================

    "page_3": {
        "rect": [129.32, 76.08, 912.46, 644.56],

        "sections": {

            "6": {
                "criteria": {
                    "6-4": {
                        "label": "Veuillez préciser la nature des traitements opérés par le destinataire des données",
                        "rect": [129.32, 76.08, 912.46, 57.97],
                        "note": 0,
                    },

                    "6-5": {
                        "label": "Veuillez indiquer s’il existe un fondement juridique au transfert",
                        "rect": [129.32, 115.00, 912.46, 38.00],
                        "note": 0,
                    },
                },

                "total": {
                    "rect": [129.32, 133.88, 912.46, 19.44],
                    "note": 2,
                },
            },

            "7": {
                "title": "SOUS-TRAITANCE",

                "criteria": {
                    "7-1": {
                        "label": "Consignation sur support (Contrat de confidentialité)",
                        "rect": [129.32, 229.74, 912.46, 49.69],
                        "note": 2,
                    },

                    "7-2": {
                        "label": "Accessibilité au sous-traitant",
                        "rect": [129.32, 279.26, 912.46, 22.84],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 301.93, 912.46, 27.38],
                    "note": 2,
                },
            },

            "8": {
                "title": "INTERCONNEXION",

                "criteria": {
                    "8": {
                        "label": "Interconnexion",
                        "rect": [129.32, 329.14, 912.46, 37.69],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 366.66, 912.46, 14.37],
                    "note": 2,
                },
            },

            "10": {
                "title": "SECURITE DES TRAITEMENTS ET DES DONNEES",

                "criteria": {
                    "10-1": {
                        "label": "Personnes habilitées à y accéder",
                        "rect": [129.32, 424.49, 912.46, 15.38],
                        "note": 2,
                    },

                    "10-2": {
                        "label": "Accès physique au poste central de surveillance",
                        "rect": [129.32, 470.13, 912.46, 30.59],
                        "note": 4,
                    },

                    "10-3": {
                        "label": "Accès logique / sauvegarde et protection des enregistrements",
                        "rect": [129.32, 500.55, 912.46, 58.67],
                        "note": 2,
                    },
                },
            },
        },
    },

    # =========================================================
    # PAGE 4
    # =========================================================

    "page_4": {
        "rect": [129.32, 76.08, 912.46, 645.76],

        "sections": {

            "10": {
                "title": "SECURITE DES TRAITEMENTS ET DES DONNEES",

                "criteria": {
                    "10-4": {
                        "label": "Mesures prises pour la suppression des enregistrements",
                        "rect": [129.32, 76.08, 912.46, 30.25],
                        "note": 2,
                    },

                    "10-5": {
                        "label": "Sensibilisation des personnes habilitées au respect de la vie privée et à la politique de sécurité",
                        "rect": [129.32, 106.17, 912.46, 64.42],
                        "note": 2,
                    },

                    "10-9": {
                        "label": "Garanties de protection des données",
                        "rect": [129.32, 183.43, 912.46, 19.94],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 203.21, 912.46, 19.94],
                    "note": 14,
                },
            },

            "11": {
                "title": "DROITS DES PERSONNES FILMEES",

                "criteria": {
                    "11-1-1": {
                        "label": "Nombre d’affiches ou de panneaux d’information",
                        "rect": [129.32, 288.38, 912.46, 95.85],
                        "note": 2,
                    },

                    "11-1-2": {
                        "label": "Localisation(s) de l’affichage",
                        "rect": [129.32, 384.07, 912.46, 30.76],
                        "note": 2,
                    },

                    "11-1-3": {
                        "label": "Autres modalités d’information des personnes concernées",
                        "rect": [129.32, 414.66, 912.46, 82.00],
                        "note": 2,
                    },

                    "11-2-1": {
                        "label": "Service ou personne auprès duquel s’exerce le droit d’accès",
                        "rect": [129.32, 541.81, 912.46, 21.80],
                        "note": 2,
                    },

                    "11-2-2": {
                        "label": "Délai de communication des informations en cas d’exercice du droit d’accès",
                        "rect": [129.32, 586.09, 912.46, 22.82],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 608.74, 912.46, 46.65],
                    "note": 10,
                },
            },

            "12": {
                "title": "ENGAGEMENT DU RESPONSABLE DU TRAITEMENT",

                "criteria": {
                    "12": {
                        "label": "Engagement du responsable du traitement",
                        "rect": [129.32, 655.21, 912.46, 30.78],
                        "note": 2,
                    },
                },

                "total": {
                    "rect": [129.32, 685.84, 912.46, 36.00],
                    "note": 2,
                },
            },
        },
    },

    # =========================================================
    # PAGE 5
    # =========================================================

    "page_5": {

        "documentation_produite": {
            "title": "DOCUMENTATION PRODUITE",

            "table": {
                "rect": [129.32, 76.09, 912.46, 89.82],

                "columns": {
                    "numero": [129.32, 76.09, 202.50, 89.82],
                    "document": [331.65, 76.09, 341.12, 89.82],
                    "verification": [672.60, 76.09, 369.18, 89.82],
                },

                "documents": {
                    "1": "Plan d’installation des caméras",
                    "2": "RCCM/NIP",
                    "3": "Politique de confidentialité",
                    "4": "Politique de sécurité",
                    "5": "AIPD",
                },
            },
        },

        "taux_conformite": {
            "label": "Taux de Conformiter",
            "rect": [129.32, 129.82, 912.46, 18.09],
            "value": "0%",
        },
    },

    # =========================================================
    # REGLES DE PRESERVATION
    # =========================================================

    "preservation": {
        "source_of_truth": "PDF APDP officiel",
        "official_layout": True,
        "preserve_all_sections": True,
        "preserve_all_criteria": True,
        "preserve_tables": True,
        "preserve_column_structure": True,
        "preserve_notes": True,
        "preserve_observations": True,
        "preserve_pagination": True,
        "preserve_official_wording": True,
        "do_not_simplify": True,
        "do_not_invent_fields": True,
        "do_not_modify_source_pdf": True,
    },
}
