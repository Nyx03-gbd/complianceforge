from app.services.apdp_generator import render_apdp_pdf
from app.services.apdp_overlay_builder import (
    build_formulaire_unique_overlays,
)


data = {
    # =====================================================
    # PAGE 1
    # =====================================================

    "nom_prenoms_raison_sociale":
        "Entreprise Démonstration ComplianceForge",

    "npi_rccm":
        "TEST-2026-001",

    "carre_lot":
        "123",

    "quartier":
        "Zongo",

    "ville":
        "Cotonou",

    "adresse_postale":
        "BP 0000 Cotonou",

    "adresse_electronique":
        "demo@complianceforge.local",

    "contact_telephonique":
        "+229 00 00 00 00",

    "autres_contacts":
        "Contact fictif",

    "activite":
        "Services numériques et conformité",

    "secteur_prive":
        True,

    "secteur_public":
        False,

    "secteur_institutions_etrangeres":
        False,

    "representant_legal_nom_prenoms":
        "Jean Exemple",

    "representant_legal_npi":
        "NPI-FICTIF-001",

    "representant_legal_carre_lot":
        "456",

    "representant_legal_quartier":
        "Cadjèhoun",

    "representant_legal_ville":
        "Cotonou",

    "representant_legal_adresse":
        "Adresse fictive",

    "representant_legal_adresse_electronique":
        "representant@complianceforge.local",

    "representant_legal_contact":
        "+229 11 11 11 11",

    "representant_legal_autres_contacts":
        "Contact secondaire fictif",


    # =====================================================
    # PAGE 2
    # =====================================================

    "origine_donnees":
        "Données fictives collectées directement auprès des personnes concernées.",

    "origine_autres":
        False,

    "personnes_salaries":
        True,

    "personnes_adherents":
        False,

    "personnes_usagers":
        False,

    "personnes_visiteurs":
        False,

    "personnes_patients":
        False,

    "personnes_clients":
        True,

    "personnes_eleves_etudiants":
        False,

    "personnes_autres":
        False,

    "nombre_personnes":
        "250",

    "operation_collecte":
        True,

    "operation_developpement":
        False,

    "operation_exposition_affichage":
        False,

    "operation_conservation":
        True,

    "operation_copie":
        False,

    "operation_traitement_image":
        False,

    "operation_exploitation":
        False,

    "operation_adaptation":
        False,

    "operation_modification":
        False,

    "operation_enregistrement":
        True,

    "operation_extraction":
        False,

    "operation_sauvegarde":
        True,

    "operation_consultation":
        True,

    "operation_utilisation":
        True,

    "operation_communication_transmission":
        False,

    "operation_diffusion":
        False,

    "operation_structuration":
        False,

    "operation_rapprochement_interconnexion":
        False,

    "operation_limitation":
        False,

    "operation_cryptage":
        True,

    "operation_effacement":
        False,

    "operation_destruction":
        False,

    "operation_organisation":
        False,

    "operation_autre":
        False,

    "operation_autre_precision":
        "",

    "type_videosurveillance_photographie":
        False,

    "type_site_web_application":
        True,

    "type_donnees_biometriques":
        False,

    "mode_manuel":
        False,

    "procedure_mise_en_oeuvre":
        "Les données sont collectées et traitées dans ComplianceForge.",

    "mode_automatise":
        True,

    "caracteristiques_techniques":
        "Application FastAPI avec PostgreSQL et contrôle des accès.",

    "fonctionnalites_systeme":
        "Gestion du registre, scoring, conformité et suivi des violations.",
}


overlays = build_formulaire_unique_overlays(data)

print("Pages avec overlays :", sorted(overlays.keys()))

for page, zones in overlays.items():
    print(
        f"Page {page} : {len(zones)} zones"
    )


output_path, source_hash, output_hash = render_apdp_pdf(
    document_id="formulaire_unique",
    page_overlays=overlays,
    output_name="TEST_formulaire_unique_pages1_2.pdf",
)

print()
print("==============================================")
print("PDF généré")
print("==============================================")
print(f"Fichier : {output_path}")
print(f"SHA256 source : {source_hash}")
print(f"SHA256 sortie : {output_hash}")
