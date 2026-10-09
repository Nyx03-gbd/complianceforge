"""
Structure fonctionnelle fidèle au Formulaire Unique APDP.

IMPORTANT :
- Le PDF APDP officiel reste la source de vérité.
- Cette structure ne modifie jamais le PDF.
- Elle sert uniquement à représenter les réponses nécessaires
  au remplissage du formulaire.
- Aucun champ absent du formulaire officiel ne doit être inventé.
"""

FORMULAIRE_UNIQUE_SECTIONS = {

    # =========================================================
    # I — IDENTIFICATION DU RESPONSABLE DE TRAITEMENT
    # =========================================================

    "I": {
        "titre": "IDENTIFICATION DU RESPONSABLE DE TRAITEMENT",

        "rubriques": {
            "responsable": [
                "nom_prenoms_raison_sociale",
                "npi_rccm",
                "carre_lot",
                "quartier",
                "ville",
                "adresse_postale",
                "adresse_electronique",
                "contact_telephonique",
                "autres_contacts",
                "activite",
                "secteur_activite",
            ],

            "representant_legal": [
                "nom_prenoms",
                "npi",
                "adresse",
                "contacts",
            ],
        },
    },

    # =========================================================
    # II — LE TRAITEMENT ENVISAGE
    # =========================================================

    "II": {
        "titre": "LE TRAITEMENT ENVISAGE",

        "rubriques": {

            # II.A — Données personnelles
            "donnees": [
                "donnees_personnelles",
                "origine_donnees",
            ],

            # II.B — Personnes concernées
            "personnes_concernees": [
                "salaries",
                "adherents",
                "usagers",
                "visiteurs",
                "patients",
                "clients",
                "eleves_etudiants",
                "autres",
                "nombre_personnes",
            ],

            # II.C — Opérations effectuées
            "operations": [
                "collecte",
                "developpement",
                "exposition_affichage",
                "conservation",
                "copie",
                "traitement_image",
                "exploitation",
                "enregistrement",
                "adaptation",
                "modification",
                "extraction",
                "sauvegarde",
                "consultation",
                "utilisation",
                "communication_transmission_diffusion_mise_a_disposition",
                "structuration_rapprochement_interconnexion",
                "limitation",
                "cryptage",
                "effacement",
                "destruction",
                "organisation",
                "autre",
            ],

            # II.C — Type de traitement
            "type_traitement": [
                "video_photo",
                "site_web_application",
                "biometrique",
            ],

            # II.C — Procédure
            "procedure": [
                "manuelle",
                "automatisee",
                "caracteristiques_techniques",
                "fonctionnalites",
            ],

            # II.D — Finalité
            "finalite": [
                "description",
            ],

            # II.E — Fondement juridique
            "fondement_juridique": [
                "fondement",
                "justification",
            ],

            # II.F — Conservation
            "conservation": [
                "duree",
                "texte_legal_reglementaire",
                "support_papier",
                "support_numerique",
                "autre_support",
            ],

            # II.G — Stockage
            "stockage": [
                "lieu",
                "modalites",
                "responsable",
                "systeme_ordinaire",
                "cloud",
                "local_nas",
                "lvm",
            ],

            # II.H — Partage
            "partage": {
                "sous_traitance": [
                    "oui_non",
                    "annexe",
                ],
                "communication": [
                    "oui_non",
                    "benin_ceDEAO",
                    "annexe",
                ],
                "interconnexion": [
                    "oui_non",
                    "annexe",
                ],
                "transfert": [
                    "oui_non",
                    "pays_tiers",
                    "autorisation_annexe",
                ],
            },

            # II.I — Date de mise en œuvre
            "mise_en_oeuvre": [
                "date",
            ],
        },
    },

    # =========================================================
    # III — RESPECT DES PRINCIPES RELATIFS AU TRAITEMENT
    # =========================================================

    "III": {
        "titre": "RESPECT DES PRINCIPES RELATIFS AU TRAITEMENT",

        "rubriques": {

            "A_licéite_legitimite": [
                "consentement",
                "contrat",
                "obligation_legale",
                "interet_legitime",
                "interet_public",
                "interets_vitaux",
                "exceptions",
            ],

            "B_transparence_loyaute": [
                "information_prealable",
                "exceptions",
                "modalites_information",
                "contenu_information",
                "preuve_information",
                "mode_consentement",
                "finalites_consentement",
                "duree_consentement",
            ],

            "C_pertinence_proportionnalite_minimisation": [
                "utilite",
                "quantite",
                "adequation",
            ],
        },
    },

    # =========================================================
    # IV — SECURITE DU DISPOSITIF
    # =========================================================

    "IV": {
        "titre": "SECURITE DU DISPOSITIF",

        "rubriques": {

            "acces_systeme": [
                "personnes_autorisees",
                "protection_intervention_non_autorisee",
            ],

            "securite_physique": [
                "politique_acces_physique",
                "mesures_physiques",
                "mesures_electroniques",
                "autres_mesures",
                "incendie",
                "inondation",
                "surtensions",
                "phenomenes_magnetiques",
            ],

            "securite_organisationnelle_logique": [
                "mesures_organisationnelles",
                "mesures_logiques",
                "tests",
                "certifications",
                "verification_identite",
                "journalisation",
                "authentification_multifacteur",
                "chiffrement",
                "sensibilisation_personnel",
                "mesures_juridiques",
            ],

            "confidentialite_integrite_disponibilite": [
                "confidentialite",
                "integrite",
                "disponibilite",
                "sauvegardes",
                "continuite_energie",
                "architecture_reseau",
            ],
        },
    },

    # =========================================================
    # V — DROITS DES PERSONNES CONCERNEES
    # =========================================================

    "V": {
        "titre": "DROIT DES PERSONNES CONCERNEES",

        "rubriques": {

            "droits": [
                "acces",
                "portabilite",
                "opposition_retrait_consentement",
                "interrogation",
                "rectification_suppression",
                "oubli_numerique",
            ],

            "modalites_exercice": [
                "modalites",
                "responsable",
                "delai",
            ],
        },
    },

    # =========================================================
    # VI — TRAITEMENTS ANTERIEURS
    # =========================================================

    "VI": {
        "titre": "TRAITEMENTS ANTERIEURS",

        "rubriques": {
            "historique_apdp": [
                "enregistrement_apdp",
                "reference_apdp_anterieure",
                "registre_activites_a_jour",
                "dpo_designe",
                "representant_legal",
                "declaration_sur_honneur",
            ],
        },
    },
}
