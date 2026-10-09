"""
Mapping officiel — APDP — Annexe 4 : TRANSFERT

IMPORTANT :
- Le PDF officiel reste la source de vérité.
- Aucune modification de sa structure.
- Les coordonnées correspondent au PDF officiel.
- Les pages et cases officielles sont conservées.
"""

APDP_ANNEXE4_MAPPING = {
    "document": "annexe_4_transfert.pdf",
    "titre": "ANNEXE 4 : TRANSFERT",
    "pages": 3,
    "official_layout": True,
    "editable": False,

    "page_1": {
        "destinataires_transfert": {
            "type": "table",
            "instruction": "Identifiez l’ensemble des destinataires des données transférées",
            "columns": {
                "denomination": {
                    "rect": [103.08, 314.17, 95.44, 22.60]
                },
                "contacts": {
                    "rect": [198.78, 314.17, 104.44, 22.60]
                },
                "representant": {
                    "rect": [303.46, 314.17, 99.89, 22.60]
                },
                "role": {
                    "rect": [403.60, 314.17, 130.59, 22.60]
                }
            }
        },

        "lien_destinataire_responsable": {
            "type": "text",
            "rect": [103.08, 222.77, 431.11, 22.60]
        },

        "pays_transfert": {
            "type": "text",
            "rect": [103.08, 168.03, 431.11, 22.60]
        },

        "entite_protection_donnees_pays_destination": {
            "type": "checkbox_group",
            "non": {
                "rect": [105.82, 498.77, 12.45, 9.90]
            },
            "oui": {
                "rect": [201.82, 552.77, 12.45, 9.90]
            },
            "nom_entite": {
                "rect": [198.82, 427.76, 335.38, 151.31]
            },
            "contacts_entite": {
                "type": "same_area",
                "rect": [198.82, 427.76, 335.38, 151.31]
            }
        },

        "lien_destinataire": {
            "type": "checkbox_group",
            "groupe_filiale_succursale": {
                "rect": [105.82, 208.77, 10.40, 9.90]
            },
            "client": {
                "rect": [259.11, 208.77, 10.40, 9.90]
            },
            "sous_traitant": {
                "rect": [317.03, 208.77, 10.40, 9.90]
            },
            "fournisseur": {
                "rect": [406.13, 208.77, 10.40, 9.90]
            },
            "autres": {
                "rect": [105.82, 196.77, 10.40, 9.90]
            },
            "description_autres": {
                "rect": [103.08, 191.44, 430.84, 31.09]
            }
        },

        "justification_transfert": {
            "type": "checkbox_group",
            "obligation_legale": {
                "rect": [201.82, 552.77, 12.45, 9.90]
            },
            "mission_interet_public": {
                "rect": [201.82, 528.77, 12.45, 9.90]
            },
            "contrat": {
                "rect": [201.82, 492.77, 12.45, 9.90]
            },
            "interets_fondamentaux_vie_privee": {
                "rect": [201.82, 456.77, 12.45, 9.90]
            },
            "autre": {
                "rect": [201.82, 432.77, 12.45, 9.90]
            },
            "justification_autre": {
                "rect": [198.82, 427.76, 335.38, 151.31]
            }
        },

        "consentement_prealable": {
            "type": "checkbox_group",
            "non": {
                "rect": [105.82, 498.77, 12.45, 9.90]
            },
            "oui": {
                "rect": [105.82, 389.77, 12.45, 9.90]
            }
        },

        "methode_obtention_consentement": {
            "type": "checkbox_group",
            "ecrit": {
                "rect": [201.82, 377.77, 12.45, 9.90]
            },
            "oral": {
                "rect": [289.28, 377.77, 12.45, 9.90]
            },
            "acceptation_electronique": {
                "rect": [375.52, 377.77, 12.45, 9.90]
            },
            "autres": {
                "rect": [201.82, 365.77, 12.45, 9.90]
            },
            "description_autres": {
                "rect": [198.82, 360.44, 335.38, 67.08]
            }
        }
    },

    "page_2": {
        "niveau_protection_legislation_etrangere": {
            "type": "text",
            "rect": [103.08, 762.35, 431.11, 22.60]
        },

        "donnees_objet_transfert": {
            "type": "text",
            "rect": [103.08, 707.61, 431.11, 22.60]
        },

        "finalite_transfert": {
            "type": "text",
            "rect": [103.08, 639.06, 431.11, 22.60]
        },

        "transfert_prevu_texte_legal": {
            "type": "checkbox_group",
            "non": {
                "rect": [105.82, 747.76, 12.45, 9.90]
            },
            "oui": {
                "rect": [338.23, 747.76, 12.45, 9.90]
            },
            "texte_reglementaire": {
                "rect": [103.08, 730.46, 431.10, 31.61]
            }
        },

        "nombre_personnes": {
            "type": "text",
            "rect": [103.08, 538.62, 199.88, 22.60]
        },

        "volume_fichier_base_donnees": {
            "type": "text",
            "rect": [303.71, 538.62, 230.48, 22.60]
        },

        "operations_destinataire": {
            "type": "checkbox_group",
            "zone": [103.08, 341.43, 431.11, 151.24],
            "cases": [
                [109.27, 466.76, 11.10, 9.90],
                [243.69, 466.76, 11.10, 9.90],
                [382.41, 466.76, 11.10, 9.90],
                [109.27, 454.76, 11.10, 9.90],
                [244.31, 454.76, 11.10, 9.90],
                [383.62, 454.76, 11.10, 9.90],
                [109.27, 442.76, 11.10, 9.90],
                [244.91, 442.76, 11.10, 9.90],
                [109.27, 430.76, 11.10, 9.90],
                [246.14, 430.76, 11.10, 9.90],
                [385.47, 430.76, 11.10, 9.90],
                [109.27, 418.76, 11.10, 9.90],
                [245.18, 418.76, 11.10, 9.90],
                [386.95, 418.76, 11.10, 9.90],
                [109.27, 406.76, 11.10, 9.90],
                [243.70, 406.76, 11.10, 9.90],
                [340.22, 406.76, 11.10, 9.90],
                [109.27, 394.76, 11.10, 9.90],
                [109.27, 382.76, 11.10, 9.90],
                [335.43, 382.76, 11.10, 9.90],
                [442.34, 382.76, 11.10, 9.90],
                [109.27, 370.76, 11.10, 9.90],
                [336.05, 370.76, 11.10, 9.90],
                [109.27, 358.76, 11.10, 9.90]
            ]
        },

        "autre_operation": {
            "type": "text",
            "rect": [103.08, 295.47, 430.84, 22.45]
        },

        "mode_transfert": {
            "type": "checkbox_group",
            "electronique": {
                "rect": [105.82, 301.76, 12.45, 9.90]
            },
            "physique": {
                "rect": [232.43, 301.76, 12.45, 9.90]
            }
        },

        "support_transfert": {
            "type": "checkbox_group",
            "zone": [103.08, 240.59, 430.84, 31.49],
            "cle_usb": {
                "rect": [105.82, 257.76, 12.45, 9.90]
            },
            "mail": {
                "rect": [185.95, 257.76, 12.45, 9.90]
            },
            "service_web": {
                "rect": [250.19, 257.76, 12.45, 9.90]
            },
            "autres": {
                "rect": [340.11, 257.76, 12.45, 9.90]
            }
        },

        "contrat_confidentialite": {
            "type": "table",
            "denomination": {
                "rect": [103.08, 194.89, 95.44, 22.60]
            },
            "date_contrat": {
                "rect": [198.78, 194.89, 104.44, 22.60]
            },
            "garanties_offertes": {
                "rect": [303.46, 194.89, 230.73, 22.60]
            }
        },

        "garanties_destinataire": {
            "type": "checkbox_group",
            "responsabilite": {
                "rect": [306.82, 180.76, 10.40, 9.90]
            },
            "securite": {
                "rect": [424.05, 180.76, 10.40, 9.90]
            },
            "confidentialite": {
                "rect": [306.82, 168.76, 10.40, 9.90]
            },
            "droits_personnes": {
                "rect": [306.82, 156.76, 10.40, 9.90]
            }
        },

        "mise_en_conformite_destinataire": {
            "type": "checkbox_group",
            "zone": [103.08, 75.22, 431.11, 31.64],
            "obligations_responsable": {
                "rect": [105.82, 578.76, 12.45, 9.90]
            },
            "controle_prealable": {
                "rect": [105.82, 566.76, 12.45, 9.90]
            }
        },

        "droits_personnes_concernees": {
            "type": "checkbox_group",
            "responsabilite": {
                "rect": [306.82, 136.76, 10.40, 9.90]
            },
            "securite": {
                "rect": [424.05, 136.76, 10.40, 9.90]
            },
            "confidentialite": {
                "rect": [306.82, 124.76, 10.40, 9.90]
            },
            "droits_personnes": {
                "rect": [306.82, 112.76, 10.40, 9.90]
            }
        }
    },

    "page_3": {
        "securite_organisee_destinataire": {
            "type": "checkbox_group",
            "communication_pssi": {
                "rect": [105.82, 715.76, 11.10, 9.90]
            },
            "audits_securite": {
                "rect": [105.82, 691.76, 11.10, 9.90]
            },
            "mesures_organisationnelles": {
                "rect": [105.82, 679.76, 11.10, 9.90]
            },
            "mesures_physiques": {
                "rect": [105.82, 667.76, 11.10, 9.90]
            }
        },

        "declaration_honneur": {
            "type": "declaration",
            "texte": "Je déclare sur l'honneur que les renseignements fournis sont exacts.",
            "zone": [56.94, 616.87, 477.25, 22.60],
            "champs": {
                "nom_prenom": {
                    "rect": [56.94, 594.02, 246.15, 22.60]
                },
                "fonction": {
                    "rect": [303.59, 594.02, 99.64, 22.60]
                },
                "date": {
                    "rect": [403.73, 594.02, 130.46, 22.60]
                }
            }
        },

        "conformite_destinataire": {
            "type": "checkbox_group",
            "non": {
                "rect": [105.82, 770.76, 11.10, 9.90]
            },
            "oui": {
                "rect": [105.82, 758.76, 11.10, 9.90]
            },
            "references": {
                "rect": [103.09, 753.43, 430.84, 31.52]
            }
        }
    }
}
