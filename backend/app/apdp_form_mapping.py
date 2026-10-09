"""
Mapping officiel du Formulaire Unique APDP.

IMPORTANT :
- Le PDF source APDP n'est jamais modifié.
- Les coordonnées sont exprimées dans le système ReportLab
  (origine en bas à gauche).
- Les zones correspondent aux cellules de réponse du PDF officiel.
"""

FORMULAIRE_UNIQUE_MAPPING = {

    # =========================================================
    # PAGE 1
    # =========================================================
    1: {

        # -----------------------------------------------------
        # I. IDENTIFICATION DU RESPONSABLE DE TRAITEMENT
        # -----------------------------------------------------

        "nom_prenoms_raison_sociale": {
            "type": "multiline",
            "x": 303.59,
            "y": 554.63,
            "width": 230.98,
            "height": 43.89,
        },

        "npi_rccm": {
            "type": "text",
            "x": 303.59,
            "y": 531.78,
            "width": 230.98,
            "height": 22.85,
        },

        "carre_lot": {
            "type": "text",
            "x": 162.73,
            "y": 508.93,
            "width": 140.86,
            "height": 22.85,
        },

        "quartier": {
            "type": "text",
            "x": 353.56,
            "y": 508.93,
            "width": 181.01,
            "height": 22.85,
        },

        "ville": {
            "type": "text",
            "x": 134.40,
            "y": 486.08,
            "width": 169.19,
            "height": 22.85,
        },

        "adresse_postale": {
            "type": "text",
            "x": 392.70,
            "y": 486.08,
            "width": 141.87,
            "height": 22.85,
        },

        "adresse_electronique": {
            "type": "text",
            "x": 217.15,
            "y": 463.23,
            "width": 317.42,
            "height": 22.85,
        },

        "contact_telephonique": {
            "type": "text",
            "x": 217.78,
            "y": 440.38,
            "width": 85.81,
            "height": 22.85,
        },

        "autres_contacts": {
            "type": "text",
            "x": 389.64,
            "y": 440.38,
            "width": 144.93,
            "height": 22.85,
        },

        "activite": {
            "type": "text",
            "x": 143.16,
            "y": 417.53,
            "width": 391.41,
            "height": 22.85,
        },

        # -----------------------------------------------------
        # Secteur d'activité
        # -----------------------------------------------------

        "secteur_prive": {
            "type": "checkbox_group",
            "x": 217.55,
            "y": 402.89,
            "width": 9.70,
            "height": 7.15,
        },

        "secteur_public": {
            "type": "checkbox_group",
            "x": 301.96,
            "y": 402.89,
            "width": 9.70,
            "height": 7.15,
        },

        "secteur_institutions_etrangeres": {
            "type": "checkbox_group",
            "x": 397.39,
            "y": 402.89,
            "width": 9.70,
            "height": 7.15,
        },

        # -----------------------------------------------------
        # Représentant légal
        # -----------------------------------------------------

        "representant_legal_nom_prenoms": {
            "type": "multiline",
            "x": 303.59,
            "y": 339.94,
            "width": 230.98,
            "height": 31.89,
        },

        "representant_legal_npi": {
            "type": "text",
            "x": 303.59,
            "y": 317.09,
            "width": 230.98,
            "height": 22.85,
        },

        "representant_legal_carre_lot": {
            "type": "text",
            "x": 162.73,
            "y": 294.24,
            "width": 140.86,
            "height": 22.85,
        },

        "representant_legal_quartier": {
            "type": "text",
            "x": 353.56,
            "y": 294.24,
            "width": 181.01,
            "height": 22.85,
        },

        "representant_legal_ville": {
            "type": "text",
            "x": 134.40,
            "y": 271.39,
            "width": 169.19,
            "height": 22.85,
        },

        "representant_legal_adresse": {
            "type": "text",
            "x": 392.70,
            "y": 271.39,
            "width": 141.87,
            "height": 22.85,
        },

        "representant_legal_adresse_electronique": {
            "type": "text",
            "x": 217.15,
            "y": 248.54,
            "width": 317.42,
            "height": 22.85,
        },

        "representant_legal_contact": {
            "type": "text",
            "x": 217.78,
            "y": 225.69,
            "width": 85.81,
            "height": 22.85,
        },

        "representant_legal_autres_contacts": {
            "type": "text",
            "x": 389.64,
            "y": 225.69,
            "width": 144.93,
            "height": 22.85,
        },
    },

    # =========================================================
    # PAGES SUIVANTES
    # =========================================================
    2: {

        # =====================================================
        # ORIGINE DES DONNÉES
        # =====================================================

        "origine_autres": {
            "type": "checkbox",
            "x": 107.19,
            "y": 770.14,
            "width": 8.35,
            "height": 7.15,
        },

        "origine_donnees": {
            "type": "multiline",
            "x": 102.96,
            "y": 709.18,
            "width": 431.36,
            "height": 19.89,
        },

        # =====================================================
        # PERSONNES CONCERNÉES
        # =====================================================

        "personnes_salaries": {
            "type": "checkbox",
            "x": 107.19,
            "y": 645.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_adherents": {
            "type": "checkbox",
            "x": 308.19,
            "y": 645.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_usagers": {
            "type": "checkbox",
            "x": 107.19,
            "y": 633.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_visiteurs": {
            "type": "checkbox",
            "x": 308.19,
            "y": 633.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_patients": {
            "type": "checkbox",
            "x": 107.19,
            "y": 621.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_clients": {
            "type": "checkbox",
            "x": 308.19,
            "y": 621.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_eleves_etudiants": {
            "type": "checkbox",
            "x": 107.19,
            "y": 609.14,
            "width": 9.70,
            "height": 7.15,
        },

        "personnes_autres": {
            "type": "checkbox",
            "x": 107.19,
            "y": 582.14,
            "width": 8.35,
            "height": 7.15,
        },

        "nombre_personnes": {
            "type": "text",
            "x": 222.40,
            "y": 552.19,
            "width": 311.92,
            "height": 22.85,
        },

        # =====================================================
        # OPÉRATIONS DE TRAITEMENT
        # =====================================================

        "operation_collecte": {
            "type": "checkbox",
            "x": 110.64,
            "y": 447.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_developpement": {
            "type": "checkbox",
            "x": 245.06,
            "y": 447.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_exposition_affichage": {
            "type": "checkbox",
            "x": 383.79,
            "y": 447.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_conservation": {
            "type": "checkbox",
            "x": 110.64,
            "y": 435.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_copie": {
            "type": "checkbox",
            "x": 110.64,
            "y": 423.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_traitement_image": {
            "type": "checkbox",
            "x": 246.29,
            "y": 423.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_exploitation": {
            "type": "checkbox",
            "x": 110.64,
            "y": 411.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_adaptation": {
            "type": "checkbox",
            "x": 246.55,
            "y": 399.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_modification": {
            "type": "checkbox",
            "x": 363.88,
            "y": 399.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_enregistrement": {
            "type": "checkbox",
            "x": 110.64,
            "y": 399.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_extraction": {
            "type": "checkbox",
            "x": 110.64,
            "y": 387.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_sauvegarde": {
            "type": "checkbox",
            "x": 184.20,
            "y": 387.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_consultation": {
            "type": "checkbox",
            "x": 110.64,
            "y": 375.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_utilisation": {
            "type": "checkbox",
            "x": 242.02,
            "y": 375.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_communication_transmission": {
            "type": "checkbox",
            "x": 359.93,
            "y": 375.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_diffusion": {
            "type": "checkbox",
            "x": 110.64,
            "y": 351.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_structuration": {
            "type": "checkbox",
            "x": 110.64,
            "y": 339.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_rapprochement_interconnexion": {
            "type": "checkbox",
            "x": 110.64,
            "y": 327.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_limitation": {
            "type": "checkbox",
            "x": 367.37,
            "y": 327.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_cryptage": {
            "type": "checkbox",
            "x": 110.64,
            "y": 315.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_effacement": {
            "type": "checkbox",
            "x": 110.64,
            "y": 303.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_destruction": {
            "type": "checkbox",
            "x": 364.93,
            "y": 303.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_organisation": {
            "type": "checkbox",
            "x": 110.64,
            "y": 291.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_autre": {
            "type": "checkbox",
            "x": 110.64,
            "y": 279.14,
            "width": 8.35,
            "height": 7.15,
        },

        "operation_autre_precision": {
            "type": "text",
            "x": 250.39,
            "y": 276.43,
            "width": 266.88,
            "height": 12.29,
        },

        # =====================================================
        # TYPE DE TRAITEMENT
        # =====================================================

        "type_videosurveillance_photographie": {
            "type": "checkbox",
            "x": 107.19,
            "y": 219.14,
            "width": 9.70,
            "height": 7.15,
        },

        "type_site_web_application": {
            "type": "checkbox",
            "x": 281.33,
            "y": 219.14,
            "width": 9.70,
            "height": 7.15,
        },

        "type_donnees_biometriques": {
            "type": "checkbox",
            "x": 400.00,
            "y": 219.14,
            "width": 9.70,
            "height": 7.15,
        },

        # =====================================================
        # MODE DE TRAITEMENT
        # =====================================================

        "mode_manuel": {
            "type": "checkbox",
            "x": 107.19,
            "y": 174.14,
            "width": 9.70,
            "height": 7.15,
        },

        "procedure_mise_en_oeuvre": {
            "type": "multiline",
            "x": 206.36,
            "y": 177.16,
            "width": 327.96,
            "height": 23.35,
            "clear_before": True,
        },

        "mode_automatise": {
            "type": "checkbox",
            "x": 107.19,
            "y": 105.14,
            "width": 9.70,
            "height": 7.15,
        },

       "caracteristiques_techniques": {
            "type": "multiline",
            "x": 206.36,
            "y": 131.46,
            "width": 327.96,
            "height": 22.85,
            "clear_before": True,
            "clear_zones": [
        {
            "x": 209.5,
            "y": 124.5,
            "width": 43.5,
            "height": 17.5,
        }
    ],
},
        "fonctionnalites_systeme": {
            "type": "multiline",
            "x": 205.86,
            "y": 85.76,
            "width": 328.46,
            "height": 22.85,
            "clear_before": True,
        },
    },
    3: {
        "finalite_traitement": {
            "type": "multiline",
            "x": 102.96,
            "y": 611.48,
            "width": 431.36,
            "height": 127.89,
        },

        "fondement_juridique": {
            "type": "multiline",
            "x": 102.96,
            "y": 556.74,
            "width": 431.36,
            "height": 31.89,
        },

        "duree_conservation": {
            "type": "text",
            "x": 303.34,
            "y": 426.35,
            "width": 230.98,
            "height": 31.89,
        },

        "texte_legal_conservation": {
            "type": "multiline",
            "x": 102.96,
            "y": 382.20,
            "width": 431.36,
            "height": 44.15,
        },

        "support_papier": {
            "type": "checkbox",
            "x": 107.19,
            "y": 333.14,
            "width": 8.35,
            "height": 7.15,
        },

        "support_numerique": {
            "type": "checkbox",
            "x": 230.61,
            "y": 333.14,
            "width": 8.35,
            "height": 7.15,
        },

        "support_autres": {
            "type": "checkbox",
            "x": 363.80,
            "y": 333.14,
            "width": 8.35,
            "height": 7.15,
        },

        "lieu_stockage": {
            "type": "text",
            "x": 102.96,
            "y": 227.80,
            "width": 103.40,
            "height": 22.85,
        },

        "modalites_stockage": {
            "type": "text",
            "x": 102.96,
            "y": 204.95,
            "width": 103.40,
            "height": 22.85,
        },

        "responsable_stockage": {
            "type": "text",
            "x": 102.96,
            "y": 182.10,
            "width": 103.40,
            "height": 22.85,
        },
    },
    4: {
        # H — PARTAGE DES DONNÉES

        "sous_traitance_oui": {
            "type": "checkbox_group",
            "x": 304.44,
            "y": 723.14,
            "width": 8.35,
            "height": 7.15,
        },

        "sous_traitance_non": {
            "type": "checkbox_group",
            "x": 304.44,
            "y": 694.14,
            "width": 8.35,
            "height": 7.15,
        },

        "communication_donnees_oui": {
            "type": "checkbox_group",
            "x": 304.44,
            "y": 640.14,
            "width": 8.35,
            "height": 7.15,
        },

        "communication_donnees_non": {
            "type": "checkbox_group",
            "x": 304.44,
            "y": 604.14,
            "width": 8.35,
            "height": 7.15,
        },

        "interconnexion_oui": {
            "type": "checkbox_group",
            "x": 309.17,
            "y": 556.14,
            "width": 9.70,
            "height": 7.15,
        },

        "interconnexion_non": {
            "type": "checkbox_group",
            "x": 307.50,
            "y": 527.14,
            "width": 9.70,
            "height": 7.15,
        },

        "transfert_pays_tiers_oui": {
            "type": "checkbox_group",
            "x": 309.75,
            "y": 479.14,
            "width": 9.70,
            "height": 7.15,
        },

        "transfert_pays_tiers_non": {
            "type": "checkbox_group",
            "x": 307.50,
            "y": 450.14,
            "width": 9.70,
            "height": 7.15,
        },

        # III.A — LICÉITÉ ET LÉGITIMITÉ DU TRAITEMENT

        "consentement": {
            "type": "checkbox",
            "x": 107.44,
            "y": 261.14,
            "width": 8.35,
            "height": 7.15,
        },

        "obligation_legale": {
            "type": "checkbox",
            "x": 107.44,
            "y": 243.14,
            "width": 8.35,
            "height": 7.15,
        },

        "mission_interet_public": {
            "type": "checkbox",
            "x": 107.44,
            "y": 225.14,
            "width": 8.35,
            "height": 7.15,
        },

        "contrat": {
            "type": "checkbox",
            "x": 303.44,
            "y": 265.14,
            "width": 8.35,
            "height": 7.15,
        },

        "interet_legitime": {
            "type": "checkbox",
            "x": 303.44,
            "y": 247.14,
            "width": 8.35,
            "height": 7.15,
        },

        "sauvegarde_interets_vitaux": {
            "type": "checkbox",
            "x": 303.44,
            "y": 229.14,
            "width": 8.35,
            "height": 7.15,
        },
    },
5: {
    "situation_surete_etat": {
        "type": "checkbox",
        "x": 211.19, "y": 758.39,
        "width": 9.70, "height": 7.15,
    },
    "situation_condamnations_penales": {
        "type": "checkbox",
        "x": 211.19, "y": 730.90,
        "width": 9.70, "height": 7.15,
    },
    "situation_infraction": {
        "type": "checkbox",
        "x": 211.19, "y": 703.41,
        "width": 9.70, "height": 7.15,
    },
    "situation_autres": {
        "type": "checkbox",
        "x": 211.19, "y": 675.92,
        "width": 9.70, "height": 7.15,
    },

    "information_prealable_non": {
        "type": "checkbox_group",
        "x": 107.19, "y": 724.14,
        "width": 9.70, "height": 7.15,
    },
    "information_prealable_oui": {
        "type": "checkbox_group",
        "x": 107.19, "y": 626.14,
        "width": 9.70, "height": 7.15,
    },

    "info_affichage": {
        "type": "checkbox",
        "x": 211.19, "y": 644.14,
        "width": 9.70, "height": 7.15,
    },
    "info_mentions_ecrites": {
        "type": "checkbox",
        "x": 285.04, "y": 644.14,
        "width": 9.70, "height": 7.15,
    },
    "info_entretien": {
        "type": "checkbox",
        "x": 430.59, "y": 644.14,
        "width": 9.70, "height": 7.15,
    },
    "info_courrier_electronique": {
        "type": "checkbox",
        "x": 211.19, "y": 632.14,
        "width": 9.70, "height": 7.15,
    },
    "info_courrier_postal": {
        "type": "checkbox",
        "x": 342.70, "y": 632.14,
        "width": 9.70, "height": 7.15,
    },
    "info_questionnaire": {
        "type": "checkbox",
        "x": 443.62, "y": 632.14,
        "width": 9.70, "height": 7.15,
    },
    "info_mention_legale": {
        "type": "checkbox",
        "x": 211.19, "y": 620.14,
        "width": 9.70, "height": 7.15,
    },
    "info_autres": {
        "type": "checkbox",
        "x": 211.19, "y": 608.14,
        "width": 9.70, "height": 7.15,
    },

"contenu_information_prealable": {
    "type": "multiline",
    "x": 303.34,
    "y": 536.00,
    "width": 230.98,
    "height": 50.00,
    "clear_zones": [
        {
            "x": 298.53,
            "y": 572.06,
            "width": 234.68,
            "height": 15.02,
        },
        {
            "x": 107.46,
            "y": 560.06,
            "width": 220.68,
            "height": 15.02,
        },
        {
            "x": 339.14,
            "y": 560.06,
            "width": 194.09,
            "height": 15.02,
        },
        {
            "x": 107.46,
            "y": 548.06,
            "width": 425.73,
            "height": 15.02,
        },
        {
            "x": 107.46,
            "y": 536.05,
            "width": 195.65,
            "height": 15.02,
        },
    ],
},
    "preuve_information_prealable": {
        "type": "text",
        "x": 303.34, "y": 487.20,
        "width": 230.98, "height": 22.85,
        "clear_before": True,
    },

    "consentement_non": {
        "type": "checkbox_group",
        "x": 107.19, "y": 378.14,
        "width": 9.70, "height": 7.15,
    },
    "consentement_oui": {
        "type": "checkbox_group",
        "x": 107.19, "y": 275.14,
        "width": 9.70, "height": 7.15,
    },

    "exclusion_obligation_legale": {
        "type": "checkbox",
        "x": 211.19, "y": 432.14,
        "width": 9.70, "height": 7.15,
    },
    "exclusion_mission_interet_public": {
        "type": "checkbox",
        "x": 211.19, "y": 408.14,
        "width": 9.70, "height": 7.15,
    },
    "exclusion_contrat": {
        "type": "checkbox",
        "x": 211.19, "y": 372.14,
        "width": 9.70, "height": 7.15,
    },
    "exclusion_interets_vitaux": {
        "type": "checkbox",
        "x": 211.19, "y": 336.14,
        "width": 9.70, "height": 7.15,
    },
    "exclusion_autre_justification": {
        "type": "checkbox",
        "x": 211.19, "y": 312.14,
        "width": 9.70, "height": 7.15,
    },

    "consentement_ecrit": {
        "type": "checkbox",
        "x": 211.19, "y": 269.14,
        "width": 9.70, "height": 7.15,
    },
    "consentement_oral": {
        "type": "checkbox",
        "x": 298.65, "y": 269.14,
        "width": 9.70, "height": 7.15,
    },
    "consentement_electronique": {
        "type": "checkbox",
        "x": 384.89, "y": 269.14,
        "width": 9.70, "height": 7.15,
    },
    "consentement_autres": {
        "type": "checkbox",
        "x": 211.19, "y": 257.14,
        "width": 9.70, "height": 7.15,
    },

    "consentement_prospection": {
        "type": "checkbox",
        "x": 211.19, "y": 237.14,
        "width": 9.70, "height": 7.15,
    },
    "consentement_partage": {
        "type": "checkbox",
        "x": 295.01, "y": 237.14,
        "width": 9.70, "height": 7.15,
    },
    "consentement_duree_conservation": {
        "type": "checkbox",
        "x": 358.05, "y": 237.14,
        "width": 9.70, "height": 7.15,
    },
    "utilite_donnees": {
        "type": "multiline",
        "x": 303.34,
        "y": 142.20,
        "width": 230.98,
        "height": 31.89,
    },

    "quantite_utile": {
        "type": "text",
        "x": 303.34,
        "y": 119.35,
        "width": 230.98,
        "height": 22.85,
    },

    "adequation_finalite": {
        "type": "text",
        "x": 303.34,
        "y": 96.50,
        "width": 230.98,
        "height": 22.85,
    },
},
6: {
    # ---------------------------------------------------------
    # IV — SECURITE DU DISPOSITIF
    # A — SECURITE DU SYSTEME D'INFORMATION
    # 1 — SECURITE TECHNIQUE
    # ---------------------------------------------------------
"personne_acces_1_mme": {
    "type": "text",
    "x": 339.00,
    "y": 657.52,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 339.00, "y": 657.52, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_1_m": {
    "type": "text",
    "x": 429.00,
    "y": 657.52,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 429.00, "y": 657.52, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_2_mme": {
    "type": "text",
    "x": 339.00,
    "y": 616.27,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 339.00, "y": 616.27, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_2_m": {
    "type": "text",
    "x": 429.00,
    "y": 616.27,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 429.00, "y": 616.27, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_3_mme": {
    "type": "text",
    "x": 339.00,
    "y": 575.02,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 339.00, "y": 575.02, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_3_m": {
    "type": "text",
    "x": 429.00,
    "y": 575.02,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 429.00, "y": 575.02, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_4_mme": {
    "type": "text",
    "x": 339.00,
    "y": 533.77,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 339.00, "y": 533.77, "width": 84.00, "height": 28.76},
    ],
},

"personne_acces_4_m": {
    "type": "text",
    "x": 429.00,
    "y": 533.77,
    "width": 84.00,
    "height": 28.76,
    "font_size": 7,
    "clear_before": True,
    "clear_zones": [
        {"x": 429.00, "y": 533.77, "width": 84.00, "height": 28.76},
    ],
},
    "securite_donnees_non": {
        "type": "checkbox_group",
        "x": 107.44,
        "y": 469.89,
        "width": 9.70,
        "height": 7.15,
    },
    "securite_donnees_oui": {
        "type": "checkbox_group",
        "x": 107.44,
        "y": 446.89,
        "width": 9.70,
        "height": 7.15,
    },

    "securite_donnees_pourquoi": {
        "type": "text",
        "x": 303.59,
        "y": 462.19,
        "width": 230.98,
        "height": 22.85,
    },

    "securite_donnees_comment": {
        "type": "text",
        "x": 303.59,
        "y": 439.34,
        "width": 230.98,
        "height": 22.85,
    },

    # ---------------------------------------------------------
    # 2 — SECURITE PHYSIQUE
    # ---------------------------------------------------------

    "politique_acces_non": {
        "type": "checkbox_group",
        "x": 107.44,
        "y": 345.89,
        "width": 9.70,
        "height": 7.15,
    },
    "politique_acces_oui": {
        "type": "checkbox_group",
        "x": 107.44,
        "y": 322.89,
        "width": 9.70,
        "height": 7.15,
    },

    "politique_acces_pourquoi": {
        "type": "text",
        "x": 303.59,
        "y": 337.75,
        "width": 230.98,
        "height": 22.85,
    },

    "politique_acces_description": {
        "type": "multiline",
        "x": 303.59,
        "y": 315.90,
        "width": 230.98,
        "height": 22.85,
    },

    # Mesures prises en compte
"mesures_physique": {
    "type": "text",
    "x": 303.59,
    "y": 292.05,
    "width": 230.98,
    "height": 22.85,
    "clear_zones": [
        {
            "x": 307.71,
            "y": 530.98,
            "width": 45.25,
            "height": 15.02,
        },
    ],
},

"mesures_electronique": {
    "type": "text",
    "x": 303.59,
    "y": 269.20,
    "width": 230.98,
    "height": 22.85,
    "clear_zones": [
        {
            "x": 307.71,
            "y": 553.83,
            "width": 64.20,
            "height": 15.02,
        },
    ],
},

"mesures_autres": {
    "type": "text",
    "x": 303.59,
    "y": 246.35,
    "width": 230.98,
    "height": 22.85,
    "clear_zones": [
        {
            "x": 307.71,
            "y": 576.68,
            "width": 40.97,
            "height": 15.02,
        },
    ],
},
    # Accès
    "acces_physique": {
        "type": "text",
        "x": 303.59,
        "y": 223.50,
        "width": 230.98,
        "height": 22.85,
    },
    "acces_electronique": {
        "type": "text",
        "x": 303.59,
        "y": 200.65,
        "width": 230.98,
        "height": 22.85,
    },
    "acces_autres": {
        "type": "text",
        "x": 303.59,
        "y": 177.80,
        "width": 230.98,
        "height": 22.85,
    },

    # Incendie
    "incendie_extincteurs": {
        "type": "text",
        "x": 303.59,
        "y": 154.95,
        "width": 230.98,
        "height": 22.85,
    },
    "incendie_autres": {
        "type": "text",
        "x": 303.59,
        "y": 132.10,
        "width": 230.98,
        "height": 22.85,
    },

    # Inondation
    "inondation_hygrometre": {
        "type": "text",
        "x": 303.59,
        "y": 109.25,
        "width": 230.98,
        "height": 22.85,
    },

    # Surtensions
    "surtensions_parafoudre": {
        "type": "text",
        "x": 303.59,
        "y": 86.40,
        "width": 230.98,
        "height": 22.85,
    },
    "surtensions_autres": {
        "type": "text",
        "x": 303.59,
        "y": 63.55,
        "width": 230.98,
        "height": 22.85,
    },
},
    7: {
        # Sécurité organisationnelle
        "protection_objets_persistants": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 660.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 648.14, 9.70, 7.15]},
        },
        "protection_objets_persistants_details": {
            "type": "text",
            "x": 345,
            "y": 646,
            "width": 185,
            "height": 18,
        },

        "procedure_test_securite": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 610.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 598.14, 9.70, 7.15]},
        },
        "procedure_test_securite_details": {
            "type": "text",
            "x": 345,
            "y": 596,
            "width": 185,
            "height": 18,
        },

        "autres_mesures_logiques": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 560.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 548.14, 9.70, 7.15]},
        },
        "autres_mesures_logiques_details": {
            "type": "text",
            "x": 345,
            "y": 546,
            "width": 185,
            "height": 18,
        },

        "certification_agrement": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 510.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 498.14, 9.70, 7.15]},
        },
        "certification_agrement_details": {
            "type": "multiline",
            "x": 345,
            "y": 490,
            "width": 185,
            "height": 35,
        },

        "verification_identite_tiers": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 448.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 436.14, 9.70, 7.15]},
        },
        "verification_identite_tiers_details": {
            "type": "text",
            "x": 345,
            "y": 434,
            "width": 185,
            "height": 18,
        },

        "journalisation_identite": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 392.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 380.14, 9.70, 7.15]},
        },
        "journalisation_identite_details": {
            "type": "text",
            "x": 345,
            "y": 378,
            "width": 185,
            "height": 18,
        },

        "authentification_cryptographie": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 306.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 294.14, 9.70, 7.15]},
        },

        # Facteur humain
        "information_personnel_securite": {
            "type": "checkbox_group",
            "non": {"rect": [308.19, 223.14, 9.70, 7.15]},
            "oui": {"rect": [308.19, 211.14, 9.70, 7.15]},
        },

        # Mesures juridiques
        "mesures_juridiques": {
            "type": "checkbox_group",
            "politique_securite_si": {"rect": [107.19, 148.14, 9.70, 7.15]},
            "politique_confidentialite": {"rect": [107.19, 136.14, 9.70, 7.15]},
            "charte_informatique": {"rect": [107.19, 124.14, 9.70, 7.15]},
            "mentions_legales": {"rect": [107.19, 112.14, 9.70, 7.15]},
            "politique_incidents": {"rect": [107.19, 100.14, 9.70, 7.15]},
            "accord_confidentialite": {"rect": [107.19, 88.14, 9.70, 7.15]},
            "autres": {"rect": [107.19, 76.14, 9.70, 7.15]},
        },
        "mesures_juridiques_details": {
            "type": "text",
            "x": 125,
            "y": 70,
            "width": 405,
            "height": 18,
        },
    },

    8: {
        # Confidentialité
        "confidentialite": {
            "type": "checkbox_group",
            "engagement_confidentialite": {"rect": [107.44, 677.54, 8.35, 7.15]},
            "pseudonymisation": {"rect": [107.44, 665.54, 8.35, 7.15]},
            "authentification_habilitations": {"rect": [107.44, 653.54, 8.35, 7.15]},
            "chiffrement": {"rect": [107.44, 629.54, 8.35, 7.15]},
            "autres": {"rect": [107.44, 617.54, 8.35, 7.15]},
        },
        "confidentialite_autres": {
            "type": "text",
            "x": 175,
            "y": 614,
            "width": 355,
            "height": 18,
        },

        # Intégrité
        "integrite": {
            "type": "checkbox_group",
            "hashage": {"rect": [107.44, 572.54, 8.35, 7.15]},
            "chiffrement_integrite": {"rect": [107.44, 560.54, 8.35, 7.15]},
            "blockchain": {"rect": [107.44, 548.54, 8.35, 7.15]},
            "logs": {"rect": [107.44, 536.54, 8.35, 7.15]},
            "gestion_habilitations": {"rect": [107.44, 524.54, 8.35, 7.15]},
            "protection_attaques": {"rect": [107.44, 512.54, 8.35, 7.15]},
            "autres": {"rect": [107.44, 500.54, 8.35, 7.15]},
        },
        "integrite_autres": {
            "type": "text",
            "x": 175,
            "y": 497,
            "width": 355,
            "height": 18,
        },

        # Disponibilité
        "dispositif_recuperation": {
            "type": "text",
            "x": 303.59,
            "y": 429.34,
            "width": 230.98,
            "height": 22.85,
        },
        "sauvegarde_frequence": {
            "type": "text",
            "x": 303.59,
            "y": 406.49,
            "width": 230.98,
            "height": 22.85,
        },
        "sauvegarde_nombre": {
            "type": "text",
            "x": 303.59,
            "y": 383.64,
            "width": 230.98,
            "height": 22.85,
        },
        "sauvegarde_support": {
            "type": "text",
            "x": 303.59,
            "y": 360.79,
            "width": 230.98,
            "height": 22.85,
        },
        "dispositif_energetique_continuite": {
            "type": "multiline",
            "x": 303.59,
            "y": 304.90,
            "width": 230.98,
            "height": 55.89,
        },
        "architecture_reseau": {
            "type": "multiline",
            "x": 303.59,
            "y": 237.01,
            "width": 230.98,
            "height": 67.89,
        },
        "architecture_reseau_autres": {
            "type": "text",
            "x": 403.73,
            "y": 145.61,
            "width": 130.84,
            "height": 22.85,
        },

        # Droit d'accès
        "droit_acces_modalites": {
            "type": "checkbox_group",
            "requete_ecrite": {"rect": [211.44, 102.14, 9.70, 7.15]},
            "requete_orale": {"rect": [308.72, 102.14, 9.70, 7.15]},
            "formulaire": {"rect": [397.44, 102.14, 9.70, 7.15]},
            "guichet": {"rect": [469.62, 102.14, 9.70, 7.15]},
            "autres": {"rect": [211.44, 88.39, 9.70, 7.15]},
        },
        "droit_acces_autres": {
            "type": "text",
            "x": 260,
            "y": 84,
            "width": 270,
            "height": 18,
        },
    },

    9: {
        # Droit d'accès - suite
        "droit_acces_responsables": {
            "type": "text",
            "x": 206.36,
            "y": 627.37,
            "width": 327.96,
            "height": 22.85,
        },
        "droit_acces_delai": {
            "type": "text",
            "x": 206.36,
            "y": 604.52,
            "width": 327.96,
            "height": 22.85,
        },

        # Portabilité
        "portabilite_modalites": {
            "type": "checkbox_group",
            "requete_ecrite": {"rect": [211.19, 672.14, 9.70, 7.15]},
            "requete_orale": {"rect": [308.47, 672.14, 9.70, 7.15]},
            "formulaire": {"rect": [397.19, 672.14, 9.70, 7.15]},
            "guichet": {"rect": [469.37, 672.14, 9.70, 7.15]},
            "autres": {"rect": [211.19, 658.39, 9.70, 7.15]},
        },
        "portabilite_autres": {
            "type": "text",
            "x": 260,
            "y": 654,
            "width": 270,
            "height": 18,
        },
        "portabilite_responsables": {
            "type": "text",
            "x": 206.36,
            "y": 627.37 - 0.0,
            "width": 327.96,
            "height": 22.85,
        },
        "portabilite_delai": {
            "type": "text",
            "x": 206.36,
            "y": 604.52 - 0.0,
            "width": 327.96,
            "height": 22.85,
        },

        # Opposition / retrait
        "opposition_exclusion": {
            "type": "text",
            "x": 303.34,
            "y": 528.86,
            "width": 230.98,
            "height": 22.85,
        },
        "opposition_preuve_information": {
            "type": "multiline",
            "x": 303.34,
            "y": 496.97,
            "width": 230.98,
            "height": 31.89,
        },
        "opposition_modalites": {
            "type": "checkbox_group",
            "requete_ecrite": {"rect": [211.19, 483.54, 9.70, 7.15]},
            "requete_orale": {"rect": [308.47, 483.54, 9.70, 7.15]},
            "formulaire": {"rect": [397.19, 483.54, 9.70, 7.15]},
            "guichet": {"rect": [469.37, 483.54, 9.70, 7.15]},
            "autres": {"rect": [211.19, 469.79, 9.70, 7.15]},
        },
        "opposition_autres": {
            "type": "text",
            "x": 260,
            "y": 465,
            "width": 270,
            "height": 18,
        },
        "opposition_responsables": {
            "type": "text",
            "x": 206.36,
            "y": 437.77,
            "width": 327.96,
            "height": 22.85,
        },
        "opposition_delai": {
            "type": "text",
            "x": 206.36,
            "y": 414.92,
            "width": 327.96,
            "height": 22.85,
        },

        # Interrogation
        "interrogation_modalites": {
            "type": "checkbox_group",
            "requete_ecrite": {"rect": [211.19, 355.54, 9.70, 7.15]},
            "requete_orale": {"rect": [308.47, 355.54, 9.70, 7.15]},
            "formulaire": {"rect": [397.19, 355.54, 9.70, 7.15]},
            "guichet": {"rect": [469.37, 355.54, 9.70, 7.15]},
            "autres": {"rect": [211.19, 341.79, 9.70, 7.15]},
        },
        "interrogation_autres": {
            "type": "text",
            "x": 260,
            "y": 337,
            "width": 270,
            "height": 18,
        },
        "interrogation_responsables": {
            "type": "text",
            "x": 206.36,
            "y": 302.92,
            "width": 327.96,
            "height": 22.85,
        },
        "interrogation_delai": {
            "type": "text",
            "x": 206.36,
            "y": 280.07,
            "width": 327.96,
            "height": 22.85,
        },

        # Rectification / suppression
        "rectification_modalites": {
            "type": "checkbox_group",
            "requete_ecrite": {"rect": [211.19, 220.54, 9.70, 7.15]},
            "requete_orale": {"rect": [308.47, 220.54, 9.70, 7.15]},
            "formulaire": {"rect": [397.19, 220.54, 9.70, 7.15]},
            "guichet": {"rect": [469.37, 220.54, 9.70, 7.15]},
            "autres": {"rect": [211.19, 206.79, 9.70, 7.15]},
        },
        "rectification_autres": {
            "type": "text",
            "x": 260,
            "y": 202,
            "width": 270,
            "height": 18,
        },
        "rectification_responsables": {
            "type": "text",
            "x": 206.36,
            "y": 168.06,
            "width": 327.96,
            "height": 22.85,
        },
        "rectification_delai": {
            "type": "text",
            "x": 206.36,
            "y": 145.21,
            "width": 327.96,
            "height": 22.85,
        },
    },

    10: {
        # Droit à l'oubli numérique
        "oubli_modalites": {
            "type": "checkbox_group",
            "requete_ecrite": {"rect": [211.44, 717.54, 9.70, 7.15]},
            "requete_orale": {"rect": [308.72, 717.54, 9.70, 7.15]},
            "formulaire": {"rect": [397.44, 717.54, 9.70, 7.15]},
            "guichet": {"rect": [469.62, 717.54, 9.70, 7.15]},
            "autres": {"rect": [211.44, 703.79, 9.70, 7.15]},
        },
        "oubli_autres": {
            "type": "text",
            "x": 260,
            "y": 699,
            "width": 270,
            "height": 18,
        },
        "oubli_responsables": {
            "type": "text",
            "x": 206.61,
            "y": 673.07,
            "width": 327.96,
            "height": 22.85,
        },
        "oubli_delai": {
            "type": "text",
            "x": 206.61,
            "y": 650.22,
            "width": 327.96,
            "height": 22.85,
        },

        # Traitements antérieurs
        "traitement_anterieur_apdp": {
            "type": "checkbox_group",
            "non": {"rect": [308.44, 587.54, 9.70, 7.15]},
            "oui": {"rect": [308.44, 575.54, 9.70, 7.15]},
        },
        "traitement_anterieur_references": {
            "type": "text",
            "x": 345,
            "y": 574,
            "width": 185,
            "height": 20,
        },

        "registre_traitements": {
            "type": "checkbox_group",
            "non": {"rect": [308.44, 531.54, 9.70, 7.15]},
            "oui": {"rect": [308.44, 519.54, 9.70, 7.15]},
        },

        "dpo_designe": {
            "type": "checkbox_group",
            "non": {"rect": [308.44, 475.54, 9.70, 7.15]},
            "oui": {"rect": [308.44, 463.54, 9.70, 7.15]},
        },

        # Représentant légal
        "representant_nom_prenoms": {
            "type": "multiline",
            "x": 303.59,
            "y": 436.60,
            "width": 230.98,
            "height": 67.89,
        },
        "representant_cip": {
            "type": "text",
            "x": 303.59,
            "y": 404.71,
            "width": 230.98,
            "height": 22.85,
        },
        "representant_carre_lot": {
            "type": "text",
            "x": 206.61,
            "y": 362.56,
            "width": 96.98,
            "height": 22.85,
        },
        "representant_quartier": {
            "type": "text",
            "x": 403.73,
            "y": 362.56,
            "width": 130.84,
            "height": 22.85,
        },
        "representant_ville": {
            "type": "text",
            "x": 206.61,
            "y": 339.71,
            "width": 96.98,
            "height": 22.85,
        },
        "representant_adresse_postale": {
            "type": "text",
            "x": 403.73,
            "y": 339.71,
            "width": 130.84,
            "height": 22.85,
        },
        "representant_adresse_electronique": {
            "type": "text",
            "x": 206.61,
            "y": 316.86,
            "width": 327.96,
            "height": 22.85,
        },
        "representant_contact_telephonique": {
            "type": "text",
            "x": 206.61,
            "y": 294.01,
            "width": 197.12,
            "height": 22.85,
        },
        "representant_autres_contacts": {
            "type": "text",
            "x": 403.73,
            "y": 294.01,
            "width": 130.84,
            "height": 22.85,
        },

        # Déclaration sur l'honneur
        "declaration_nom_prenom": {
            "type": "text",
            "x": 57.07,
            "y": 199.06,
            "width": 246.52,
            "height": 22.85,
        },
        "declaration_fonction": {
            "type": "text",
            "x": 303.59,
            "y": 199.06,
            "width": 100.14,
            "height": 22.85,
        },
        "declaration_date": {
            "type": "text",
            "x": 403.73,
            "y": 199.06,
            "width": 130.84,
            "height": 22.85,
        },
    },
}
