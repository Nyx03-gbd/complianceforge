"""
Mapping officiel APDP
FORMULAIRE D’ENGAGEMENT DE CONFORMITE
DE TRAITEMENTS DE DONNEES A CARACTERE PERSONNEL

PDF officiel :
    engagement_conformite.pdf

IMPORTANT :
- Le PDF APDP officiel est la source de vérité.
- Aucune rubrique officielle n'est supprimée.
- Aucune rubrique n'est simplifiée.
- Les tableaux, cases et zones officielles sont conservés.
- Ce fichier décrit uniquement les zones de remplissage du PDF officiel.
"""

APDP_ENGAGEMENT_CONFORMITE_MAPPING = {
    "document": "engagement_conformite.pdf",
    "titre": "FORMULAIRE D’ENGAGEMENT DE CONFORMITE DE TRAITEMENTS DE DONNEES A CARACTERE PERSONNEL",
    "pages": 6,
    "official_layout": True,
    "editable": False,

    # ==========================================================
    # PAGE 1
    # ==========================================================
    "page_1": {

        "identification_responsable_traitement": {

            "nom_prenoms_raison_sociale": {
                "type": "text",
                "rect": [103.21, 598.52, 431.36, 22.85],
            },

            "npi_rccm": {
                "type": "text",
                "rect": [198.90, 531.78, 335.66, 22.85],
            },

            "carre_lot": {
                "type": "text",
                "rect": [103.21, 508.93, 200.38, 22.85],
            },

            "quartier": {
                "type": "text",
                "rect": [303.59, 508.93, 230.98, 22.85],
            },

            "ville": {
                "type": "text",
                "rect": [103.21, 486.08, 200.38, 22.85],
            },

            "adresse_postale": {
                "type": "text",
                "rect": [303.59, 486.08, 230.98, 22.85],
            },

            "adresse_electronique": {
                "type": "text",
                "rect": [103.21, 463.23, 431.36, 22.85],
            },

            "contact_telephonique": {
                "type": "text",
                "rect": [103.21, 440.38, 200.38, 22.85],
            },

            "autres_contacts": {
                "type": "text",
                "rect": [303.59, 440.38, 230.98, 22.85],
            },

            "activite": {
                "type": "text",
                "rect": [103.21, 417.53, 431.36, 22.85],
            },

            "secteur": {
                "type": "checkbox_group",

                "prive": {
                    "type": "checkbox",
                    "position": [209.55, 403.00],
                },

                "public": {
                    "type": "checkbox",
                    "position": [293.96, 403.00],
                },

                "institutions_etrangeres": {
                    "type": "checkbox",
                    "position": [389.39, 403.00],
                },
            },
        },

        "representant_legal": {

            "nom_prenoms": {
                "type": "text",
                "rect": [103.21, 339.94, 431.36, 31.89],
            },

            "npi": {
                "type": "text",
                "rect": [303.59, 317.09, 230.98, 22.85],
            },

            "carre_lot": {
                "type": "text",
                "rect": [103.21, 294.24, 200.38, 22.85],
            },

            "quartier": {
                "type": "text",
                "rect": [303.59, 294.24, 230.98, 22.85],
            },

            "ville": {
                "type": "text",
                "rect": [103.21, 271.39, 200.38, 22.85],
            },

            "adresse_postale": {
                "type": "text",
                "rect": [303.59, 271.39, 230.98, 22.85],
            },

            "adresse_electronique": {
                "type": "text",
                "rect": [103.21, 248.54, 431.36, 22.85],
            },

            "contact_telephonique": {
                "type": "text",
                "rect": [103.21, 225.69, 200.38, 22.85],
            },

            "autres_contacts": {
                "type": "text",
                "rect": [303.59, 225.69, 230.98, 22.85],
            },
        },

        "traitement_anterieur": {

            "reference_anterieure_apdp": {
                "type": "text",
                "rect": [303.59, 134.29, 230.98, 22.85],
            },

            "date_mise_en_oeuvre": {
                "type": "text",
                "rect": [303.59, 87.55, 230.98, 23.89],
            },
        },
    },

    # ==========================================================
    # PAGE 2
    # ==========================================================
    "page_2": {

        "nature_traitement": {
            "type": "checkbox_group",

            "prive": {
                "type": "checkbox",
                "position": [109.27, 445.76],
            },

            "public": {
                "type": "checkbox",
                "position": [243.69, 445.76],
            },

            "institutions_etrangeres": {
                "type": "checkbox",
                "position": [382.41, 445.76],
            },
        },

        "donnees_personnelles": {
            "changement_parametre": {
                "type": "checkbox_group",
                "oui": [105.82, 643.76],
                "non": [105.82, 631.76],
            },

            "origine_donnees": {
                "type": "multiline_text",
                "rect": [103.46, 598.02, 199.11, 65.06],
            },
        },

        "personnes_concernees": {
            "changement_parametre": {
                "type": "checkbox_group",
                "oui": [306.82, 643.76],
                "non": [306.82, 631.76],
            },

            "categories": {
                "salaries": [109.27, 433.76],
                "usagers": [109.27, 421.76],
                "patients": [109.27, 409.76],
                "eleves_etudiants": [109.27, 397.76],
                "adherents": [245.18, 397.76],
                "visiteurs": [109.27, 385.76],
                "clients": [182.83, 385.76],
                "autres": [109.27, 373.76],
            },

            "autres_precision": {
                "type": "text",
                "rect": [103.46, 255.31, 430.09, 228.21],
            },

            "nombre_personnes": {
                "type": "text",
                "rect": [206.49, 154.44, 327.70, 45.45],
            },
        },

        "operations_traitement": {
            "changement_parametre": {
                "type": "checkbox_group",
                "oui": [105.82, 217.76],
                "non": [279.95, 217.76],
            },

            "operations": {
                "collecte": [109.27, 349.76],
                "developpement": [109.27, 337.76],
                "exposition_affichage": [109.27, 325.76],
                "conservation": [109.27, 313.76],
                "copie": [109.27, 301.76],
                "traitement_image": [363.56, 301.76],
                "exploitation": [109.27, 289.76],
                "enregistrement": [109.27, 277.76],
                "adaptation": [240.65, 373.76],
                "modification": [358.56, 373.76],
                "extraction": [109.27, 385.76],
                "sauvegarde": [182.83, 385.76],
                "consultation": [109.27, 397.76],
                "utilisation": [245.18, 397.76],
                "communication_transmission": [362.50, 397.76],
                "diffusion_mise_disposition": [109.27, 409.76],
                "structuration": [109.27, 421.76],
                "rapprochement_interconnexion": [244.91, 421.76],
                "limitation": [109.27, 433.76],
                "cryptage": [109.27, 445.76],
                "effacement": [109.27, 373.76],
                "destruction": [240.65, 373.76],
                "organisation": [109.27, 349.76],
            },

            "autre_precision": {
                "type": "multiline_text",
                "rect": [103.46, 232.03, 430.73, 22.73],
            },
        },

        "type_traitement": {
            "videosurveillance_photographie": [105.82, 172.76],
            "site_web_application": [306.82, 172.76],
            "donnees_biometriques": [398.63, 172.76],
            "manuel": [105.82, 103.76],
            "automatise": [105.82, 103.76],

            "autres": {
                "type": "text",
                "rect": [103.46, 63.04, 102.14, 91.04],
            },
        },

        "procedure": {
            "type": "multiline_text",
            "rect": [206.49, 108.74, 327.70, 45.45],
        },

        "caracteristiques_techniques": {
            "type": "multiline_text",
            "rect": [206.49, 63.04, 327.70, 45.45],
        },
    },

    # ==========================================================
    # PAGE 3
    # ==========================================================
    "page_3": {

        "type_traitement": {
            "changement_parametre": {
                "type": "checkbox_group",
                "oui": [105.82, 331.76],
                "non": [229.23, 331.76],
            },

            "procedure": {
                "type": "multiline_text",
                "rect": [103.46, 556.87, 430.73, 31.64],
            },

            "caracteristiques_techniques": {
                "type": "multiline_text",
                "rect": [103.46, 458.36, 430.73, 29.71],
            },

            "fonctionnalites_systeme": {
                "type": "multiline_text",
                "rect": [103.46, 382.32, 430.73, 43.90],
            },
        },

        "conservation_donnees": {
            "changement_parametre": {
                "type": "checkbox_group",
                "oui": [105.82, 331.76],
                "non": [229.23, 331.76],
            },

            "duree_conservation": {
                "type": "text",
                "rect": [103.46, 273.62, 430.73, 29.71],
            },

            "texte_legal_conservation": {
                "type": "multiline_text",
                "rect": [103.46, 250.78, 430.73, 22.60],
            },
        },

        "stockage_donnees": {
            "changement_parametre": {
                "type": "checkbox_group",
                "oui": [105.82, 331.76],
                "non": [229.23, 331.76],
            },

            "lieu": {
                "type": "text",
                "rect": [103.46, 227.93, 102.78, 22.60],
            },

            "modalites": {
                "type": "text",
                "rect": [103.46, 205.07, 102.78, 22.60],
            },

            "responsable": {
                "type": "text",
                "rect": [103.46, 182.22, 102.78, 22.60],
            },

            "systemes_stockage": {
                "ordinaire": [105.82, 331.76],
                "cloud": [229.23, 331.76],
                "serveur_local_nas": [362.43, 331.76],
            },

            "forme_archivage": {
                "papier": [105.82, 331.76],
                "numerique": [229.23, 331.76],
                "autres": [362.43, 331.76],
            },
        },
    },

    # ==========================================================
    # PAGE 4
    # ==========================================================
    "page_4": {

        "partage_donnees": {
            "sous_traitance": {
                "type": "checkbox_group",
                "non": [303.59, 263.76],
                "oui": [303.59, 245.76],
            },

            "communication": {
                "type": "checkbox_group",
                "non": [303.96, 602.76],
                "oui": [303.96, 638.76],
            },

            "interconnexion": {
                "type": "checkbox_group",
                "non": [303.96, 477.76],
                "oui": [303.96, 554.76],
            },

            "transfert": {
                "type": "checkbox_group",
                "non": [303.96, 692.76],
                "oui": [303.96, 721.76],
            },
        },

        "date_mise_en_oeuvre": {
            "type": "text",
            "rect": [103.71, 218.58, 199.88, 55.49],
        },

        "licéite_legitimite": {
            "type": "checkbox_group",
            "consentement": [106.07, 259.76],
            "obligation_legale": [106.07, 241.76],
            "mission_interet_public": [106.07, 223.76],
            "contrat": [307.79, 554.76],
            "interet_legitime": [306.12, 525.76],
            "interets_vitaux": [306.12, 448.76],
        },
    },

    # ==========================================================
    # PAGE 5 — SECURITE
    # ==========================================================
    "page_5": {

        "securite_systeme_information": {

            "technique": {
                "type": "checkbox_group",
                "oui": [114.11, 650.51],
                "non": [345.28, 650.51],
            },

            "physique": {
                "type": "checkbox_group",
                "oui": [114.11, 578.51],
                "non": [345.28, 578.51],
            },

            "organisationnelle": {
                "type": "checkbox_group",
                "oui": [114.11, 505.51],
                "non": [345.28, 505.51],
            },

            "facteur_humain": {
                "type": "checkbox_group",
                "oui": [114.11, 432.51],
                "non": [345.28, 432.51],
            },

            "mesures_juridiques": {
                "type": "checkbox_group",
                "oui": [114.11, 360.51],
                "non": [345.28, 360.51],
            },
        },

        "securite_traitement_donnees": {

            "confidentialite": {
                "type": "checkbox_group",
                "oui": [114.11, 241.51],
                "non": [345.28, 241.51],
            },

            "integrite": {
                "type": "checkbox_group",
                "oui": [114.11, 168.51],
                "non": [345.28, 168.51],
            },

            "disponibilite": {
                "type": "checkbox_group",
                "oui": [114.11, 96.51],
                "non": [345.28, 96.51],
            },
        },
    },

    # ==========================================================
    # PAGE 6 — TRAÇABILITE / AUTRES PRECISIONS / DECLARATION
    # ==========================================================
    "page_6": {

        "preuve_tracabilite": {

            "type": "checkbox_group",

            "oui": {
                "type": "checkbox",
                "position": [114.11, 747.38],
            },

            "non": {
                "type": "checkbox",
                "position": [345.28, 747.38],
            },
        },

        "autres_precisions": {
            "type": "multiline_text",
            "rect": [56.69, 374.15, 481.89, 19.71],
        },

        "declaration_sur_honneur": {

            "nom_prenom": {
                "type": "text",
                "rect": [56.69, 393.86, 96.01, 11.00],
            },

            "fonction": {
                "type": "text",
                "rect": [56.69, 404.86, 159.17, 11.00],
            },

            "date": {
                "type": "text",
                "rect": [347.24, 404.86, 191.35, 11.00],
            },
        },
    },
}
