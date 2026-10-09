"""
Mapping officiel APDP
FORMULAIRE COMPLEMENTAIRE POUR LA MISE EN OEUVRE
DE TRAITEMENTS SUR SITE WEB

Source de vérité :
    formulaire_site_web.pdf

IMPORTANT :
- Le PDF officiel APDP n'est jamais modifié.
- La structure officielle, les rubriques, les tableaux,
  les cases et la pagination sont conservés.
- Ce fichier décrit uniquement les zones utilisables
  pour le remplissage ultérieur.
"""

APDP_SITE_WEB_MAPPING = {
    "document": "formulaire_site_web.pdf",
    "titre": "FORMULAIRE COMPLEMENTAIRE POUR LA MISE EN OEUVRE DE TRAITEMENTS SUR SITE WEB",
    "pages": 5,
    "official_layout": True,
    "editable": False,

    # ==========================================================
    # PAGE 1
    # ==========================================================
    "page_1": {

        "donnees_personnelles_concernees": {
            "type": "section",

            "donnees_specifiques": {
                "type": "multiline_text",
                "rect": [114.003, 619.011, 423.35, 22.85],
            },

            "origine_donnees": {
                "type": "multiline_text",
                "rect": [114.003, 586.861, 423.35, 31.90],
            },
        },

        "operations_traitement": {
            "type": "section",

            "personnes_concernees": {
                "type": "checkbox_group",

                "responsable_traitement": {
                    "type": "checkbox",
                    "position": [116.625, 353.677],
                },

                "tiers": {
                    "type": "checkbox",
                    "position": [116.625, 341.677],
                },

                "autres": {
                    "type": "checkbox",
                    "position": [116.625, 329.677],
                },

                "responsable_precision": {
                    "type": "text",
                    "rect": [114.003, 268.086, 423.35, 135.485],
                },
            },

            "finalite": {
                "type": "checkbox_group",

                "prospection_ciblage_marketing": {
                    "type": "checkbox",
                    "position": [116.625, 455.736],
                },

                "identification_gestion_experience_utilisateur": {
                    "type": "checkbox",
                    "position": [259.746, 455.736],
                },

                "mesure_audience_frequentation": {
                    "type": "checkbox",
                    "position": [116.625, 443.317],
                },

                "controle_publications": {
                    "type": "checkbox",
                    "position": [389.872, 443.317],
                },

                "suivi_activites_internet_reseautage": {
                    "type": "checkbox",
                    "position": [116.625, 194.677],
                },

                "autres": {
                    "type": "checkbox",
                    "position": [116.625, 182.677],
                },

                "autres_precision": {
                    "type": "multiline_text",
                    "rect": [114.003, 109.321, 423.35, 111.665],
                },
            },

            "operations_specifiques": {
                "type": "checkbox_group",

                "newsletters": {
                    "type": "checkbox",
                    "position": [116.625, 194.677],
                },

                "intelligence_artificielle": {
                    "type": "checkbox",
                    "position": [116.625, 182.677],
                },

                "enregistrement": {
                    "type": "checkbox",
                    "position": [116.625, 170.677],
                },

                "selection": {
                    "type": "checkbox",
                    "position": [116.625, 158.677],
                },

                "autres": {
                    "type": "checkbox",
                    "position": [116.625, 146.677],
                },

                "autres_precision": {
                    "type": "multiline_text",
                    "rect": [114.003, 109.321, 423.35, 111.665],
                },
            },

            "donnees_techniques": {
                "type": "checkbox_group",

                "adresse_ip": {
                    "type": "checkbox",
                    "position": [116.625, 572.677],
                },

                "traces_connexion": {
                    "type": "checkbox",
                    "position": [282.631, 572.677],
                },

                "numero_mac_terminal": {
                    "type": "checkbox",
                    "position": [116.625, 560.677],
                },

                "traces_clics_souris": {
                    "type": "checkbox",
                    "position": [282.829, 560.677],
                },

                "cookies": {
                    "type": "checkbox",
                    "position": [116.625, 548.677],
                },

                "pages_consultees": {
                    "type": "checkbox",
                    "position": [284.656, 548.677],
                },

                "metadonnees_localisation": {
                    "type": "checkbox",
                    "position": [116.625, 536.677],
                },

                "identifiant_publicitaire": {
                    "type": "checkbox",
                    "position": [284.07, 536.677],
                },

                "autre": {
                    "type": "checkbox",
                    "position": [116.625, 524.677],
                },

                "references_terminal": {
                    "type": "checkbox",
                    "position": [283.463, 524.677],
                },

                "autre_precision": {
                    "type": "text",
                    "rect": [114.003, 494.436, 422.972, 92.175],
                },
            },
        },
    },

    # ==========================================================
    # PAGE 2
    # ==========================================================
    "page_2": {

        "gestion_cookies_rapports": {
            "type": "section",

            "utilisation_cookies_traceurs": {
                "type": "checkbox_group",

                "oui": {
                    "type": "checkbox",
                    "position": [402.142, 382.866],
                },

                "non": {
                    "type": "checkbox",
                    "position": [446.696, 382.866],
                },
            },

            "caracteristiques_cookies": {
                "type": "table",

                "colonnes": [
                    "type",
                    "fonction",
                    "duree_validite",
                ],

                "rect": [114.003, 654.91, 423.35, 22.85],
            },

            "modalites_rapport": {
                "type": "multiline_text",
                "rect": [114.003, 456.629, 94.341, 47.64],
            },

            "frequence": {
                "type": "text",
                "rect": [412.777, 456.629, 124.577, 47.64],
            },
        },

        "information_visiteur_utilisateur": {
            "type": "section",

            "modalites_information": {
                "type": "multiline_text",
                "rect": [114.003, 409.43, 423.35, 23.35],
            },
        },

        "infrastructure_logicielle_technologie": {
            "type": "section",

            "langages_framework": {
                "type": "table",

                "colonnes": [
                    "denomination",
                    "framework",
                    "type_fonction",
                    "derniere_mise_a_jour",
                ],

                "rect": [114.003, 237.359, 423.35, 22.49],

                "lignes": [
                    "HTML",
                    "My SQL",
                    "PHP",
                    "JAVA SCRIPT",
                    "PYTHON",
                    "Autre",
                ],
            },

            "cms": {
                "type": "text",
                "rect": [114.003, 74.677, 423.35, 22.49],
            },

            "premiere_connexion_information_cookies": {
                "type": "checkbox_group",

                "oui": {
                    "type": "checkbox",
                    "position": [416.241, 439.866],
                },

                "non": {
                    "type": "checkbox",
                    "position": [460.795, 439.866],
                },
            },

            "modalites_information_cookies": {
                "type": "checkbox_group",

                "mentions_legales": {
                    "type": "checkbox",
                    "position": [313.16, 366.866],
                },

                "politique_confidentialite": {
                    "type": "checkbox",
                    "position": [313.16, 354.866],
                },

                "popup_avertissement": {
                    "type": "checkbox",
                    "position": [313.16, 342.866],
                },

                "formulaire_consentement": {
                    "type": "checkbox",
                    "position": [313.16, 330.866],
                },
            },

            "desactivation_retrait_consentement": {
                "type": "checkbox_group",

                "oui": {
                    "type": "checkbox",
                    "position": [147.192, 509.866],
                },

                "non": {
                    "type": "checkbox",
                    "position": [191.747, 509.866],
                },
            },

            "echange_serveur_ou_editeur_distant": {
                "type": "checkbox_group",

                "oui": {
                    "type": "checkbox",
                    "position": [460.795, 439.866],
                },

                "non": {
                    "type": "checkbox",
                    "position": [416.241, 439.866],
                },
            },
        },
    },

    # ==========================================================
    # PAGE 3
    # ==========================================================
    "page_3": {

        "extensions_plugins": {
            "type": "table",

            "colonnes": [
                "type",
                "fonction",
                "duree_validite",
            ],

            "rect": [114.003, 762.06, 423.101, 22.49],
        },

        "protocole_ssl_tls": {
            "type": "section",

            "nom_domaine": {
                "type": "text",
                "rect": [114.003, 669.099, 423.35, 22.49],
            },

            "beneficiaire_certificat": {
                "type": "text",
                "rect": [114.003, 590.469, 423.35, 22.49],
            },

            "autorite_certification": {
                "type": "text",
                "rect": [114.003, 566.978, 198.282, 22.49],
            },

            "signature_numerique": {
                "type": "text",
                "rect": [114.003, 543.488, 198.282, 22.49],
            },

            "sous_domaines_associes": {
                "type": "text",
                "rect": [114.003, 519.998, 198.282, 22.49],
            },

            "date_emission_certificat": {
                "type": "text",
                "rect": [114.003, 496.508, 198.282, 22.49],
            },

            "date_expiration_certificat": {
                "type": "text",
                "rect": [114.003, 473.017, 198.282, 22.49],
            },

            "cloudfare": {
                "type": "text",
                "rect": [114.003, 449.527, 198.282, 22.49],
            },
        },

        "architecture_site": {
            "type": "multiline_text",
            "rect": [114.003, 318.435, 422.972, 37.272],
        },

        "interconnexion": {
            "type": "checkbox_group",

            "active_directory": {
                "type": "checkbox",
                "position": [116.625, 339.03],
            },

            "base_de_donnees": {
                "type": "checkbox",
                "position": [116.625, 324.03],
            },

            "cable": {
                "type": "checkbox",
                "position": [116.625, 255.616],
            },

            "wifi_sans_fil": {
                "type": "checkbox",
                "position": [185.027, 255.616],
            },

            "internet": {
                "type": "checkbox",
                "position": [277.25, 255.616],
            },

            "wan": {
                "type": "checkbox",
                "position": [116.625, 232.616],
            },

            "vpn": {
                "type": "checkbox",
                "position": [187.654, 232.616],
            },

            "mpls": {
                "type": "checkbox",
                "position": [252.989, 232.616],
            },

            "api": {
                "type": "checkbox",
                "position": [465.052, 232.616],
            },

            "autres": {
                "type": "text",
                "rect": [114.003, 202.716, 423.35, 22.85],
            },
        },

        "securite_donnees": {
            "type": "multiline_text",
            "rect": [114.003, 249.075, 422.972, 22.691],
        },

        "documentation_legale": {
            "type": "checkbox_group",

            "mentions_legales": {
                "type": "checkbox",
                "position": [116.625, 654.616],
            },

            "politique_confidentialite": {
                "type": "checkbox",
                "position": [265.062, 654.616],
            },

            "conditions_generales_utilisation": {
                "type": "checkbox",
                "position": [393.33, 654.616],
            },

            "autres_ligne_1": {
                "type": "text",
                "position": [116.625, 636.616],
            },

            "autres_ligne_2": {
                "type": "text",
                "position": [265.062, 636.616],
            },

            "autres_ligne_3": {
                "type": "text",
                "position": [393.33, 636.616],
            },
        },
    },

    # ==========================================================
    # PAGE 4
    # ==========================================================
    "page_4": {

        "documentation_disponible": {
            "type": "checkbox_group",

            "mentions_legales": {
                "type": "checkbox",
                "position": [313.16, 774.866],
            },

            "politique_confidentialite": {
                "type": "checkbox",
                "position": [313.16, 762.866],
            },

            "conditions_generales_utilisation": {
                "type": "checkbox",
                "position": [313.16, 750.866],
            },

            "autres": {
                "type": "checkbox",
                "position": [313.16, 738.866],
            },
        },

        "hebergement": {
            "type": "section",

            "hebergeur_web": {
                "type": "text",
                "rect": [114.003, 737.41, 198.407, 47.64],
            },

            "telephone": {
                "type": "text",
                "rect": [114.003, 668.11, 298.024, 22.85],
            },

            "mail": {
                "type": "text",
                "rect": [113.878, 645.01, 198.532, 22.85],
            },

            "nature_hebergement": {
                "type": "checkbox_group",

                "partage": {
                    "type": "checkbox",
                    "position": [249.925, 628.866],
                },

                "vps": {
                    "type": "checkbox",
                    "position": [336.062, 628.866],
                },
            },

            "acces_ftp": {
                "type": "checkbox_group",

                "oui": {
                    "type": "checkbox",
                    "position": [297.357, 605.866],
                },

                "non": {
                    "type": "checkbox",
                    "position": [341.911, 605.866],
                },
            },
        },

        "securite_physique": {
            "type": "multiline_text",
            "rect": [114.003, 552.61, 423.35, 22.85],
        },

        "declaration_sur_honneur": {
            "type": "section",

            "nom_prenoms": {
                "type": "text",
                "rect": [67.75, 320.689, 469.603, 22.85],
            },

            "fonction": {
                "type": "text",
                "rect": [67.75, 297.589, 244.91, 22.85],
            },

            "date": {
                "type": "text",
                "rect": [412.527, 297.589, 124.827, 22.85],
            },
        },
    },

    # ==========================================================
    # PAGE 5
    # ==========================================================
    "page_5": {

        "documentation_a_joindre": {
            "type": "texte_officiel",
            "editable": False,

            "items": [
                {
                    "numero": 1,
                    "texte": "Caractéristiques techniques des équipements utilisés",
                },
                {
                    "numero": 2,
                    "texte": "Preuve du recueil de consentement des personnes concernées en cas de transfert",
                },
                {
                    "numero": 3,
                    "texte": "Engagement de confidentialité signé entre les agents en charge du traitement des données personnelles et le Responsable de Traitement",
                },
                {
                    "numero": 4,
                    "texte": "Copie du Contrat de confidentialité signé entre le Responsable de Traitement et le sous-traitant ou les prestataires le cas échéant",
                },
                {
                    "numero": 5,
                    "texte": "Copie des clauses de confidentialité de l’hébergeur ou du propriétaire du cloud en cas de conservation des données",
                },
                {
                    "numero": 6,
                    "texte": "Politique de sécurité appliquée au traitement",
                },
                {
                    "numero": 7,
                    "texte": "Copie du NPI ou de la pièce d’identité (CIN ou Passeport) du Responsable de traitement de la société",
                },
                {
                    "numero": 8,
                    "texte": "Copie de l’extrait du Registre de Commerce et de Crédit Mobilier (RCCM) et / ou de l’Identifiant Fiscal Unique (IFU) de la société / structure",
                },
                {
                    "numero": 9,
                    "texte": "Preuve des dispositions prises pour satisfaire le droit à l’information préalable",
                },
                {
                    "numero": 10,
                    "texte": "…..",
                },
            ],
        },
    },
}
