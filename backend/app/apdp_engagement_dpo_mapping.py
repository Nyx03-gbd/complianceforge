"""
Mapping officiel APDP
ENGAGEMENT DE RESPECT DES OBLIGATIONS INCOMBANT AU
DELEGUE A LA PROTECTION DES DONNEES PERSONNELLES

Document officiel :
    engagement_dpo.pdf

Le document est une lettre d'engagement de 4 pages.
Les pages 2 et 3 contiennent le texte officiel des missions du DPD
et ne doivent pas être transformées ou simplifiées.

Le PDF source reste inchangé.
"""

APDP_ENGAGEMENT_DPO_MAPPING = {
    "document": "engagement_dpo.pdf",
    "titre": (
        "ENGAGEMENT DE RESPECT DES OBLIGATIONS INCOMBANT AU "
        "DELEGUE A LA PROTECTION DES DONNEES PERSONNELLES"
    ),
    "pages": 4,
    "official_layout": True,
    "editable": False,

    # ==========================================================
    # PAGE 1
    # ==========================================================
    "page_1": {

        "delegue": {

            "prenoms_nom": {
                "type": "text",
                "rect": [250.00, 532.04, 110.00, 7.50],
            },

            "piece_identite_numero": {
                "type": "text",
                "rect": [72.50, 519.04, 155.00, 8.00],
            },

            "piece_delivree_par": {
                "type": "text",
                "rect": [272.50, 519.04, 77.50, 8.00],
            },

            "piece_date_delivrance": {
                "type": "text",
                "rect": [367.50, 519.04, 150.00, 8.00],
            },

            "piece_date_expiration": {
                "type": "text",
                "rect": [72.50, 505.04, 237.50, 8.00],
            },

            "telephone": {
                "type": "text",
                "rect": [350.00, 505.04, 167.50, 8.00],
            },

            "fonction": {
                "type": "text",
                "rect": [250.00, 490.04, 100.00, 8.00],
            },

            "entreprise_organisme": {
                "type": "text",
                "rect": [72.50, 476.04, 347.50, 8.50],
            },

            "quartier": {
                "type": "text",
                "rect": [72.50, 462.04, 197.50, 8.50],
            },

            "rccm": {
                "type": "text",
                "rect": [330.00, 462.04, 190.00, 8.50],
            },

            "ifu": {
                "type": "text",
                "rect": [72.50, 448.54, 182.50, 8.50],
            },

            "telephone_entreprise": {
                "type": "text",
                "rect": [330.00, 448.54, 182.50, 8.50],
            },

            "email": {
                "type": "text",
                "rect": [125.00, 435.04, 195.00, 8.50],
            },
        },

        "designation_dpd": {

            # Reconnais que par courrier n°
            "numero_courrier_designation": {
                "type": "text",
                "rect": [230.00, 390.00, 105.00, 18.00],
            },

            # en date du
            "date_courrier_designation": {
                "type": "text",
                "rect": [390.00, 390.00, 115.00, 18.00],
            },

            # [...] organismes responsables des traitements
            "organismes_responsables_traitements": {
                "type": "text",
                "rect": [460.00, 360.00, 65.00, 18.00],
            },

            # le […indiquer la date de désignation du DPD…]
            "date_designation_dpd": {
                "type": "text",
                "rect": [390.00, 315.00, 120.00, 18.00],
            },

            # directement rattaché à […la direction ou nom du DG, PDG…]
            "direction_rattachement": {
                "type": "text",
                "rect": [225.00, 255.00, 225.00, 18.00],
            },

            # date de délivrance du récépissé/accusé de réception
            "date_recepisse_apdp": {
                "type": "text",
                "rect": [395.00, 180.00, 125.00, 18.00],
            },

            # date de prise d’effet
            "date_prise_effet": {
                "type": "text",
                "rect": [70.00, 145.00, 205.00, 18.00],
            },
        },

        # Le paragraphe suivant est conservé tel quel :
        #
        # "Mes coordonnées ont fait objet de publication dans
        #  l’entreprise/ l’organisme."
        #
        # Il ne constitue pas un champ à remplir.
        "publication_coordonnees": {
            "type": "official_fixed_text",
            "editable": False,
        },

        # Texte officiel de transition :
        #
        # "Je m'engage, par la présente, à remplir mes missions
        #  en tant que Délégué à la protection des données
        #  de la manière suivante :"
        "transition_missions": {
            "type": "official_fixed_text",
            "editable": False,
        },
    },

    # ==========================================================
    # PAGE 2
    # ==========================================================
    "page_2": {

        "type": "official_fixed_text",
        "editable": False,

        "contenu": (
            "Missions officielles du Délégué à la protection des données "
            "personnelles, points 1 à 9."
        ),

        "preservation": [
            "Conserver intégralement le texte officiel.",
            "Conserver la numérotation officielle.",
            "Ne pas reformuler les missions.",
            "Ne pas supprimer les références au Livre Vème du code du numérique.",
            "Conserver le pied de page APDP.",
        ],
    },

    # ==========================================================
    # PAGE 3
    # ==========================================================
    "page_3": {

        "type": "official_fixed_text",
        "editable": False,

        "contenu": (
            "Suite des missions officielles du Délégué à la protection "
            "des données personnelles, points 10 à 15, suivie des "
            "conditions et moyens nécessaires à l'exercice des missions."
        ),

        "preservation": [
            "Conserver intégralement les points 10 à 15.",
            "Conserver les paragraphes relatifs aux ressources et moyens.",
            "Conserver les obligations du responsable de traitement ou du sous-traitant.",
            "Ne pas simplifier le texte.",
            "Ne pas supprimer les obligations relatives à l'indépendance du DPD.",
            "Conserver le pied de page APDP.",
        ],
    },

    # ==========================================================
    # PAGE 4
    # ==========================================================
    "page_4": {

        "fin_engagement": {

            # Date de l'engagement :
            #
            # Fait à Cotonou le …………………………………………..
            "date_engagement": {
                "type": "text",
                "rect": [165.60, 294.00, 200.00, 18.00],
            },

            # Signature
            "signature": {
                "type": "signature",
                "rect": [425.00, 160.00, 95.00, 90.00],
            },
        },

        "mentions_finales": {
            "secret_professionnel": {
                "type": "official_fixed_text",
                "editable": False,
                "text": (
                    "Je reconnais que je suis soumis au secret professionnel "
                    "en ce qui concerne l’exercice de mes missions."
                ),
            },

            "sur_honneur": {
                "type": "official_fixed_text",
                "editable": False,
                "text": "Sur l'honneur et aux fins de droit.",
            },
        },
    },

    # ==========================================================
    # REGLE GENERALE
    # ==========================================================
    "regle_preservation": {
        "source_of_truth": "PDF APDP officiel",
        "preserve_official_structure": True,
        "preserve_official_text": True,
        "preserve_pagination": True,
        "preserve_footer": True,
        "preserve_header": True,
        "do_not_simplify": True,
        "do_not_invent_missing_fields": True,
        "source_pdf_must_not_be_modified": True,
    },
}
