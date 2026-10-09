"""
Mapping du document officiel APDP
FORMULAIRE COMPLEMENTAIRE POUR LA MISE EN OEUVRE
DE TRAITEMENTS PAR CAPTEURS
(IMAGE, VOIX, DONNEES BIOMETRIQUES)

Source :
    templates/apdp/formulaire_capteurs.pdf

Document officiel : 5 pages.

IMPORTANT :
- Le PDF officiel ne doit jamais être modifié.
- Les textes, rubriques, cases et pagination sont conservés.
- Les coordonnées ci-dessous proviennent de l'extraction du PDF officiel.
- Les pages 4 et 5 contiennent respectivement les mentions APDP/
  déclaration et la documentation à joindre.
"""

APDP_CAPTEURS_MAPPING = {
    "document": "formulaire_capteurs.pdf",
    "titre": (
        "FORMULAIRE COMPLEMENTAIRE POUR LA MISE EN OEUVRE "
        "DE TRAITEMENTS PAR CAPTEURS (IMAGE, VOIX, DONNEES BIOMETRIQUES)"
    ),
    "pages": 5,
    "official_layout": True,
    "editable": False,

    # ==========================================================
    # PAGE 1
    # ==========================================================
    "page_1": {

        "donnees_personnelles": {
            "categories_donnees": {
                "type": "multiline",
                "rect": [113.66, 572.86, 424.02, 31.90],
            },

            "origine_donnees": {
                "type": "multiline",
                "rect": [113.66, 456.96, 424.02, 22.85],
            },
        },

        "operations_traitement": {

            "categories": {
                "images_videos_personne": {
                    "type": "checkbox",
                    "rect": [116.62, 558.68, 11.10, 9.90],
                },
                "empreintes": {
                    "type": "checkbox",
                    "rect": [327.50, 558.68, 11.10, 9.90],
                },
                "voix": {
                    "type": "checkbox",
                    "rect": [116.62, 546.68, 11.10, 9.90],
                },
                "temperature_corporelle": {
                    "type": "checkbox",
                    "rect": [329.89, 546.68, 11.10, 9.90],
                },
                "localisation_geolocalisation": {
                    "type": "checkbox",
                    "rect": [116.62, 534.68, 11.10, 9.90],
                },
                "metadonnees": {
                    "type": "checkbox",
                    "rect": [116.62, 522.68, 11.10, 9.90],
                },
                "ecriture_manuscrite": {
                    "type": "checkbox",
                    "rect": [116.62, 510.68, 11.10, 9.90],
                },
                "autre": {
                    "type": "checkbox",
                    "rect": [116.62, 498.68, 11.10, 9.90],
                },
                "autre_precision": {
                    "type": "text",
                    "rect": [180.00, 494.00, 350.00, 14.00],
                },
            },

            "personnes_concernees": {

                "responsable_traitement": {
                    "type": "checkbox",
                    "rect": [116.62, 441.74, 12.45, 9.90],
                },

                "responsable_traitement_precision": {
                    "type": "text",
                    "rect": [300.00, 438.00, 230.00, 15.00],
                },

                "tiers": {
                    "type": "checkbox",
                    "rect": [116.62, 429.32, 12.45, 9.90],
                },

                "tiers_precision": {
                    "type": "text",
                    "rect": [170.00, 426.00, 210.00, 15.00],
                },

                "autres": {
                    "type": "checkbox",
                    "rect": [389.87, 429.32, 12.45, 9.90],
                },

                "autres_precision": {
                    "type": "text",
                    "rect": [440.00, 426.00, 90.00, 15.00],
                },
            },

            "finalite": {

                "securite_personnes": {
                    "type": "checkbox",
                    "rect": [116.62, 351.68, 11.10, 9.90],
                },

                "securite_biens": {
                    "type": "checkbox",
                    "rect": [268.80, 351.68, 11.10, 9.90],
                },

                "protection_abords_batiments": {
                    "type": "checkbox",
                    "rect": [116.62, 339.68, 11.10, 9.90],
                },

                "regulation_trafic_routier": {
                    "type": "checkbox",
                    "rect": [116.62, 327.68, 11.10, 9.90],
                },

                "protection_batiments_publics": {
                    "type": "checkbox",
                    "rect": [269.41, 327.68, 11.10, 9.90],
                },

                "prevention_risques": {
                    "type": "checkbox",
                    "rect": [116.62, 315.68, 11.10, 9.90],
                },

                "detection_age_osseux": {
                    "type": "checkbox",
                    "rect": [387.44, 315.68, 11.10, 9.90],
                },

                "surveillance_jeux": {
                    "type": "checkbox",
                    "rect": [116.62, 303.68, 11.10, 9.90],
                },

                "detection_rayonnement_thermique": {
                    "type": "checkbox",
                    "rect": [263.29, 303.68, 11.10, 9.90],
                },

                "gestion_acces": {
                    "type": "checkbox",
                    "rect": [116.62, 291.68, 11.10, 9.90],
                },

                "autres": {
                    "type": "checkbox",
                    "rect": [116.62, 279.68, 11.10, 9.90],
                },

                "autres_precision": {
                    "type": "multiline",
                    "rect": [113.66, 254.09, 424.02, 135.49],
                },
            },

            "traitements_images": {

                "systemes_experts": {
                    "type": "checkbox",
                    "rect": [116.62, 188.68, 11.10, 9.90],
                },

                "irm": {
                    "type": "checkbox",
                    "rect": [301.79, 188.68, 11.10, 9.90],
                },

                "retouche_image": {
                    "type": "checkbox",
                    "rect": [407.46, 188.68, 11.10, 9.90],
                },

                "intelligence_artificielle": {
                    "type": "checkbox",
                    "rect": [116.62, 176.68, 11.10, 9.90],
                },

                "compression": {
                    "type": "checkbox",
                    "rect": [303.63, 176.68, 11.10, 9.90],
                },

                "echographie": {
                    "type": "checkbox",
                    "rect": [408.09, 176.68, 11.10, 9.90],
                },

                "scintigraphie": {
                    "type": "checkbox",
                    "rect": [116.62, 164.68, 11.10, 9.90],
                },

                "operateurs_traitement_images": {
                    "type": "checkbox",
                    "rect": [302.40, 164.68, 11.10, 9.90],
                },

                "calibration": {
                    "type": "checkbox",
                    "rect": [116.62, 152.68, 11.10, 9.90],
                },

                "restauration": {
                    "type": "checkbox",
                    "rect": [300.55, 152.68, 11.10, 9.90],
                },

                "segmentation": {
                    "type": "checkbox",
                    "rect": [405.64, 152.68, 11.10, 9.90],
                },

                "deconvolution": {
                    "type": "checkbox",
                    "rect": [116.62, 140.68, 11.10, 9.90],
                },

                "reconnaissance": {
                    "type": "checkbox",
                    "rect": [116.62, 128.68, 11.10, 9.90],
                },

                "autres": {
                    "type": "checkbox",
                    "rect": [116.62, 116.68, 11.10, 9.90],
                },

                "autres_precision": {
                    "type": "multiline",
                    "rect": [114.03, 95.32, 423.23, 111.67],
                },
            },
        },
    },

    # ==========================================================
    # PAGE 2
    # ==========================================================
    "page_2": {

        "dispositif_acquisition": {

            "caracteristiques": {

                "liste_equipements": {
                    "type": "multiline",
                    "rect": [114.03, 724.31, 423.64, 23.00],
                },

                "fabricant": {
                    "type": "text",
                    "rect": [114.03, 701.46, 423.64, 22.60],
                },

                "origine_equipement": {
                    "type": "text",
                    "rect": [114.03, 677.86, 198.54, 22.85],
                },
            },

            "nature_technologie": {
                "type": "multiline",
                "rect": [114.03, 465.71, 423.64, 22.85],
            },

            "architecture_traitement": {
                "type": "multiline",
                "rect": [114.03, 375.36, 423.64, 22.85],
            },

            "connexions_liaisons_reseau": {

                "terminaux_acces": {
                    "type": "multiline",
                    "rect": [114.03, 224.52, 423.64, 22.85],
                },

                "acces_donnees_distance": {
                    "type": "text",
                    "rect": [114.03, 109.33, 423.23, 22.55],
                },

                "acces_distance_oui": {
                    "type": "checkbox",
                    "rect": [278.06, 115.87, 11.10, 9.90],
                },

                "acces_distance_non": {
                    "type": "checkbox",
                    "rect": [322.61, 115.87, 11.10, 9.90],
                },

                "vpn": {
                    "type": "checkbox",
                    "rect": [119.68, 184.87, 11.10, 9.90],
                },

                "type_acquisition": {
                    "type": "checkbox_group",
                    "rect": [114.03, 421.56, 423.64, 43.62],
                    "choices": {
                        "analogique": [116.62, 450.87, 11.10, 9.90],
                        "numerique": [201.56, 450.87, 11.10, 9.90],
                        "ultra_son": [291.97, 450.87, 11.10, 9.90],
                        "infra_rouge": [376.88, 450.87, 11.10, 9.90],
                        "rayon_x": [469.74, 450.87, 11.10, 9.90],
                        "rayonnement_thermique": [116.62, 438.87, 11.10, 9.90],
                        "autre": [116.62, 426.87, 11.10, 9.90],
                    },
                },

                "autre_technologie": {
                    "type": "text",
                    "rect": [150.00, 424.00, 380.00, 18.00],
                },

                "reseau": {
                    "type": "checkbox_group",
                    "rect": [114.03, 201.42, 423.23, 22.75],
                    "choices": {
                        "cable": [116.62, 207.87, 11.10, 9.90],
                        "wifi_sans_fil": [185.03, 207.87, 11.10, 9.90],
                        "internet": [277.25, 207.87, 11.10, 9.90],
                        "lan": [341.99, 207.87, 11.10, 9.90],
                    },
                },

                "acces_temps_reel_oui": {
                    "type": "checkbox",
                    "rect": [452.89, 140.87, 11.10, 9.90],
                },

                "acces_temps_reel_non": {
                    "type": "checkbox",
                    "rect": [497.45, 140.87, 11.10, 9.90],
                },

                "partage_connexion_oui": {
                    "type": "checkbox",
                    "rect": [298.84, 161.87, 11.10, 9.90],
                },

                "partage_connexion_non": {
                    "type": "checkbox",
                    "rect": [343.39, 161.87, 11.10, 9.90],
                },
            },
        },
    },

    # ==========================================================
    # PAGE 3
    # ==========================================================
    "page_3": {

        "localisation_dispositif": {

            "emplacements": {
                "type": "text",
                "rect": [114.03, 762.20, 423.64, 22.85],
            },

            "espace": {
                "type": "text",
                "rect": [114.03, 715.49, 198.54, 22.98],
            },

            "nombre_capteurs": {
                "type": "text",
                "rect": [114.03, 496.82, 198.54, 30.67],
            },

            "volume_donnees": {
                "type": "text",
                "rect": [114.03, 442.80, 198.54, 30.67],
            },
        },

        "securite_physique": {

            "donnees_protegees_oui": {
                "type": "checkbox",
                "rect": [376.36, 746.83, 11.10, 9.90],
            },

            "donnees_protegees_non": {
                "type": "checkbox",
                "rect": [420.72, 746.83, 11.10, 9.90],
            },

            "pourquoi_protection": {
                "type": "multiline",
                "rect": [114.03, 373.50, 423.64, 22.85],
            },

            "comment_protection": {
                "type": "multiline",
                "rect": [208.94, 302.71, 328.73, 22.49],
            },

            "politique_acces_oui": {
                "type": "checkbox",
                "rect": [152.69, 746.87, 11.10, 9.90],
            },

            "politique_acces_non": {
                "type": "checkbox",
                "rect": [197.24, 746.87, 11.10, 9.90],
            },

            "pourquoi_politique": {
                "type": "multiline",
                "rect": [208.94, 270.56, 328.73, 31.90],
            },

            "description_mesures": {
                "type": "multiline",
                "rect": [114.03, 162.47, 423.64, 55.90],
            },
        },

        "information_personnes": {

            "nombre_affiches_panneaux": {
                "type": "text",
                "rect": [114.03, 93.17, 298.23, 22.85],
            },

            "pictogrammes": {
                "type": "text",
                "rect": [113.91, 70.07, 298.35, 22.85],
            },

            "public_prive": {
                "type": "checkbox_group",
                "choices": {
                    "prive": [318.68, 700.87, 11.10, 9.90],
                    "ouvert_au_public": [318.68, 688.87, 11.10, 9.90],
                },
            },

            "fixe_mobile": {
                "type": "checkbox_group",
                "choices": {
                    "fixe_oui": [376.36, 746.83, 11.10, 9.90],
                    "fixe_non": [420.72, 746.83, 11.10, 9.90],
                    "mobile_oui": [318.68, 700.87, 11.10, 9.90],
                    "mobile_non": [318.68, 688.87, 11.10, 9.90],
                },
            },
        },
    },

    # ==========================================================
    # PAGE 4
    # ==========================================================
    "page_4": {

        # Le texte APDP est fixe et ne doit pas être réécrit.
        "mentions_apdp": {
            "type": "official_fixed_text",
            "editable": False,
        },

        "declaration_honneur": {

            "nom_prenoms": {
                "type": "text",
                "rect": [67.75, 716.00, 245.08, 22.85],
            },

            "fonction": {
                "type": "text",
                "rect": [313.08, 716.00, 99.44, 22.85],
            },

            "date": {
                "type": "text",
                "rect": [412.76, 716.00, 124.91, 22.85],
            },
        },
    },

    # ==========================================================
    # PAGE 5
    # ==========================================================
    "page_5": {

        "documentation_a_joindre": {
            "type": "official_fixed_text",
            "editable": False,

            "items": [
                "Caractéristiques techniques des équipements utilisés",
                "Preuve du recueil de consentement des personnes concernées en cas de transfert",
                "Engagement de confidentialité signé entre les agents en charge du traitement des données personnelles et le Responsable de Traitement",
                "Copie du Contrat de confidentialité signé entre le Responsable de Traitement et le sous-traitant ou les prestataires le cas échéant",
                "Copie des clauses de confidentialité de l’hébergeur ou du propriétaire du cloud en cas de conservation des données",
                "Politique de sécurité appliqué au traitement",
                "Copie du NPI ou de la pièce d’identité (CIN ou Passeport) du Responsable de traitement de la société",
                "Copie de l’extrait du Registre de Commerce et de Crédit Mobilier (RCCM) et / ou de l’Identifiant Fiscal Unique (IFU) de la société / structure",
                "Preuve des dispositions prises pour satisfaire le droit à l’information préalable",
                "Le plan d’installation des capteurs et leur champ de vision",
            ],
        },
    },

    # ==========================================================
    # REGLES DE PRESERVATION
    # ==========================================================
    "regle_preservation": {
        "source_of_truth": "PDF APDP officiel",
        "preserve_official_structure": True,
        "preserve_official_text": True,
        "preserve_tables": True,
        "preserve_checkboxes": True,
        "preserve_pagination": True,
        "preserve_header": True,
        "preserve_footer": True,
        "do_not_simplify": True,
        "do_not_invent_missing_fields": True,
        "source_pdf_must_not_be_modified": True,
    },
}
