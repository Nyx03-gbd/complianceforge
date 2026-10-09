"""
Mapping officiel — Annexe 3 APDP : INTERCONNEXION.

IMPORTANT :
- Le PDF officiel APDP est la source de vérité.
- Le PDF original n'est jamais modifié.
- Les coordonnées servent uniquement à la superposition.
- La page 3 est une check-list officielle et n'est pas une zone de saisie.
"""

ANNEXE_3_INTERCONNEXION_MAPPING = {

    # ================================================================
    # PAGE 1
    # ================================================================

    1: {

        # ------------------------------------------------------------
        # FICHIER / TRAITEMENT 1
        # ------------------------------------------------------------

        "traitement_1": {
            "fichier_ou_traitement": {
                "type": "multiline",
                "x": 103.08,
                "y": 547.76,
                "width": 95.19,
                "height": 31.64,
            },

            "reference_apdp": {
                "type": "text",
                "x": 199.03,
                "y": 547.76,
                "width": 335.16,
                "height": 31.64,
            },

            "finalite": {
                "type": "multiline",
                "x": 199.03,
                "y": 524.91,
                "width": 104.31,
                "height": 22.60,
            },
        },

        # ------------------------------------------------------------
        # FICHIER / TRAITEMENT 2
        # ------------------------------------------------------------

        "traitement_2": {
            "fichier_ou_traitement": {
                "type": "multiline",
                "x": 103.08,
                "y": 493.02,
                "width": 95.57,
                "height": 31.64,
            },

            "reference_apdp": {
                "type": "multiline",
                "x": 198.65,
                "y": 493.02,
                "width": 335.54,
                "height": 31.64,
            },

            "finalite": {
                "type": "multiline",
                "x": 199.03,
                "y": 470.17,
                "width": 104.31,
                "height": 22.60,
            },
        },

        # ------------------------------------------------------------
        # FICHIER / TRAITEMENT 3
        # ------------------------------------------------------------

        "traitement_3": {
            "fichier_ou_traitement": {
                "type": "multiline",
                "x": 103.08,
                "y": 438.28,
                "width": 95.19,
                "height": 31.64,
            },

            "reference_apdp": {
                "type": "multiline",
                "x": 199.03,
                "y": 438.28,
                "width": 335.16,
                "height": 31.64,
            },

            "finalite": {
                "type": "multiline",
                "x": 199.03,
                "y": 415.43,
                "width": 104.31,
                "height": 22.60,
            },
        },

        # ------------------------------------------------------------
        # MODALITES DE MISE EN OEUVRE
        # ------------------------------------------------------------

        "modalites_mise_en_oeuvre": {
            "type": "multiline",
            "x": 103.08,
            "y": 392.58,
            "width": 431.11,
            "height": 22.60,
        },

        # ------------------------------------------------------------
        # NATURE / PORTEE DE L'AUTOMATISATION
        # ------------------------------------------------------------

        "nature_portee_automatisation": {
            "type": "multiline",
            "x": 103.08,
            "y": 337.84,
            "width": 431.11,
            "height": 31.64,
        },

        # ------------------------------------------------------------
        # TYPES DE MISE EN OEUVRE
        # ------------------------------------------------------------

        "type_mise_en_oeuvre": {
            "type": "checkbox_group",

            "fusion": {
                "x": 105.82,
                "y": 323.77,
                "width": 12.45,
                "height": 9.90,
            },

            "transfert_informations": {
                "x": 171.33,
                "y": 323.77,
                "width": 12.45,
                "height": 9.90,
            },

            "assemblage": {
                "x": 311.92,
                "y": 323.77,
                "width": 12.45,
                "height": 9.90,
            },

            "consultation_bases_internet": {
                "x": 404.71,
                "y": 323.77,
                "width": 12.45,
                "height": 9.90,
            },
        },

        # ------------------------------------------------------------
        # SERVICES / API / SERVICES WEB
        # ------------------------------------------------------------

        "services_interconnexion": {
            "type": "checkbox_group",

            "api_services_web_autres": {
                "x": 105.82,
                "y": 375.77,
                "width": 12.45,
                "height": 9.90,
            },

            "autre_service": {
                "x": 163.95,
                "y": 375.77,
                "width": 12.45,
                "height": 9.90,
            },

            "description_autre": {
                "type": "text",
                "x": 103.08,
                "y": 369.73,
                "width": 430.84,
                "height": 22.34,
            },
        },

        # ------------------------------------------------------------
        # DONNEES CONCERNEES
        # ------------------------------------------------------------

        "donnees_concernees": {
            "type": "multiline",
            "x": 103.08,
            "y": 191.44,
            "width": 430.84,
            "height": 91.41,
        },

        # ------------------------------------------------------------
        # SERVICES NECESSITANT UNE INTERCONNEXION INTERNET
        # ------------------------------------------------------------

        "services_internet": {
            "type": "checkbox_group",

            "navigation_web": {
                "x": 105.82,
                "y": 268.77,
                "width": 12.45,
                "height": 9.90,
            },

            "sources_sites_confiance": {
                "x": 212.87,
                "y": 268.77,
                "width": 12.45,
                "height": 9.90,
            },

            "resolution_dns": {
                "x": 105.82,
                "y": 256.77,
                "width": 12.45,
                "height": 9.90,
            },

            "hebergement_web": {
                "x": 261.16,
                "y": 256.77,
                "width": 12.45,
                "height": 9.90,
            },

            "services_infrastructure_exposes": {
                "x": 105.82,
                "y": 244.77,
                "width": 12.45,
                "height": 9.90,
            },

            "services_collaboratifs_exposes": {
                "x": 105.82,
                "y": 208.77,
                "width": 12.45,
                "height": 9.90,
            },
        },

        # ------------------------------------------------------------
        # INTERCONNEXION PREVUE PAR UN TEXTE
        # ------------------------------------------------------------

        "texte_reglementaire_legal": {
            "type": "checkbox_group",

            "non": {
                "x": 105.82,
                "y": 95.77,
                "width": 12.45,
                "height": 9.90,
            },

            "oui": {
                "x": 105.82,
                "y": 107.77,
                "width": 12.45,
                "height": 9.90,
            },

            "texte": {
                "type": "multiline",
                "x": 103.08,
                "y": 90.77,
                "width": 430.84,
                "height": 31.31,
            },
        },

        # ------------------------------------------------------------
        # RAISONS DE L'INTERCONNEXION
        # ------------------------------------------------------------

        "raisons_interconnexion": {
            "type": "multiline",
            "x": 103.08,
            "y": 67.92,
            "width": 431.11,
            "height": 22.60,
        },
    },

    # ================================================================
    # PAGE 2
    # ================================================================

    2: {

        # ------------------------------------------------------------
        # DUREE DE L'INTERCONNEXION
        # ------------------------------------------------------------

        "duree_interconnexion": {
            "type": "text",
            "x": 103.09,
            "y": 739.50,
            "width": 431.11,
            "height": 22.60,
        },

        # ------------------------------------------------------------
        # RISQUES IDENTIFIES
        # ------------------------------------------------------------

        "risques_identifies": {
            "type": "multiline",
            "x": 103.09,
            "y": 693.80,
            "width": 431.11,
            "height": 22.60,
        },

        # ------------------------------------------------------------
        # ARCHITECTURE ET FONCTION DE SECURITE
        # ------------------------------------------------------------

        "architecture_fonction_securite": {
            "type": "checkbox_group",

            "dmz": {
                "x": 105.82,
                "y": 624.76,
                "width": 12.45,
                "height": 9.90,
            },

            "pare_feux": {
                "x": 253.21,
                "y": 624.76,
                "width": 12.45,
                "height": 9.90,
            },

            "filtrage_perimetrique": {
                "x": 388.40,
                "y": 624.76,
                "width": 12.45,
                "height": 9.90,
            },

            "rupture_protocolaire": {
                "x": 105.82,
                "y": 612.76,
                "width": 12.45,
                "height": 9.90,
            },

            "authentification_sans_annuaire": {
                "x": 403.84,
                "y": 612.76,
                "width": 12.45,
                "height": 9.90,
            },

            "cloisonnement_zones": {
                "x": 218.95,
                "y": 600.76,
                "width": 12.45,
                "height": 9.90,
            },

            "journalisation": {
                "x": 105.82,
                "y": 588.76,
                "width": 12.45,
                "height": 9.90,
            },

            "interception_tls": {
                "x": 199.42,
                "y": 588.76,
                "width": 12.45,
                "height": 9.90,
            },

            "poste_rebond_navigation_web": {
                "x": 314.84,
                "y": 588.76,
                "width": 12.45,
                "height": 9.90,
            },

            "autres": {
                "x": 105.82,
                "y": 576.76,
                "width": 12.45,
                "height": 9.90,
            },

            "autres_description": {
                "type": "text",
                "x": 103.09,
                "y": 571.43,
                "width": 431.11,
                "height": 67.38,
            },
        },

        # ------------------------------------------------------------
        # RISQUES IDENTIFIES — CASES
        # ------------------------------------------------------------

        "risques_cases": {
            "type": "checkbox_group",

            "exfiltration_donnees_internet": {
                "x": 105.82,
                "y": 679.76,
                "width": 12.45,
                "height": 9.90,
            },

            "intrusion": {
                "x": 307.04,
                "y": 679.76,
                "width": 12.45,
                "height": 9.90,
            },

            "usurpation_identite": {
                "x": 378.02,
                "y": 679.76,
                "width": 12.45,
                "height": 9.90,
            },

            "acces_sites_interdits": {
                "x": 105.82,
                "y": 667.76,
                "width": 12.45,
                "height": 9.90,
            },

            "facteur_humain": {
                "x": 255.05,
                "y": 667.76,
                "width": 12.45,
                "height": 9.90,
            },
        },

        # ------------------------------------------------------------
        # DECLARATION SUR L'HONNEUR
        # ------------------------------------------------------------

        "declaration_honneur": {
            "nom_prenom": {
                "x": 56.94,
                "y": 502.62,
                "width": 246.15,
                "height": 22.60,
            },

            "fonction": {
                "x": 303.59,
                "y": 502.62,
                "width": 99.64,
                "height": 22.60,
            },

            "date": {
                "x": 403.73,
                "y": 502.62,
                "width": 130.46,
                "height": 22.60,
            },
        },
    },

    # ================================================================
    # PAGE 3
    # ================================================================

    3: {

        # La page 3 contient la CHECK LIST MESURE DE SECURITE
        # INTERCONNEXION A INTERNET.
        #
        # Elle constitue un contenu officiel du document.
        # Il n'y a pas de zone de saisie à remplir.
        #
        "type": "checklist_officielle",
        "editable": False,
    },
}
