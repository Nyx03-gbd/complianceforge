from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.models import StatutTraitement


class OrganisationCreate(BaseModel):
    nom: str
    secteur_activite: Optional[str] = None
    ifu_rccm: Optional[str] = None
    adresse: Optional[str] = None
    contact_dpo_email: Optional[str] = None


class OrganisationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    nom: str
    secteur_activite: Optional[str]
    ifu_rccm: Optional[str]
    adresse: Optional[str]
    contact_dpo_email: Optional[str]
    date_creation: datetime


class CategorieDonneeCreate(BaseModel):
    categorie: str
    sensible: bool = False


class CategorieDonneeOut(CategorieDonneeCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str


class TraitementCreate(BaseModel):
    nom: str
    service_responsable: Optional[str] = None
    finalite: Optional[str] = None
    base_legale: Optional[str] = None
    justification_base_legale: Optional[str] = None
    organisation_id: str
    categories_donnees: list[CategorieDonneeCreate] = []
    sensibilite_donnees: Optional[int] = None
    niveau_mesures_securite: Optional[int] = None
    sous_traitance_transferts: Optional[int] = None
    exposition: Optional[int] = None
    volume: Optional[int] = None


class TraitementUpdate(BaseModel):
    nom: Optional[str] = None
    service_responsable: Optional[str] = None
    statut: Optional[StatutTraitement] = None
    finalite: Optional[str] = None
    base_legale: Optional[str] = None
    justification_base_legale: Optional[str] = None
    sensibilite_donnees: Optional[int] = None
    niveau_mesures_securite: Optional[int] = None
    sous_traitance_transferts: Optional[int] = None
    exposition: Optional[int] = None
    volume: Optional[int] = None


class TraitementOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    organisation_id: str
    nom: str
    service_responsable: Optional[str]
    statut: StatutTraitement
    finalite: Optional[str]
    base_legale: Optional[str]
    date_creation: datetime
    derniere_revision: datetime
    categories_donnees: list[CategorieDonneeOut] = []
    sensibilite_donnees: Optional[int] = None
    niveau_mesures_securite: Optional[int] = None
    sous_traitance_transferts: Optional[int] = None
    exposition: Optional[int] = None
    volume: Optional[int] = None


class ScoreConformiteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    traitement_id: str
    score_global: float
    version_grille: str
    details: dict
    date_calcul: datetime


class ScoreRisqueOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    traitement_id: str
    score_global: float
    niveau: str
    composantes: dict
    date_calcul: datetime


class ScoresCalcules(BaseModel):
    conformite: ScoreConformiteOut
    risque: ScoreRisqueOut


class DocumentGenereOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    traitement_id: str
    type_document: str
    nom_fichier: str
    hash_integrite: str
    template_version: str
    date_generation: datetime

# ============================================================
# SCHÉMAS APDP
# ============================================================

class ProfilResponsableAPDPCreate(BaseModel):
    organisation_id: str
    nom_prenoms_raison_sociale: Optional[str] = None
    npi_rccm: Optional[str] = None
    carre_lot: Optional[str] = None
    quartier: Optional[str] = None
    ville: Optional[str] = None
    adresse_postale: Optional[str] = None
    adresse_electronique: Optional[str] = None
    contact_telephonique: Optional[str] = None
    autres_contacts: Optional[str] = None
    activite: Optional[str] = None
    secteur_activite: Optional[str] = None
    representant_legal_nom_prenoms: Optional[str] = None
    representant_legal_npi: Optional[str] = None
    representant_legal_adresse: Optional[str] = None
    representant_legal_contacts: Optional[str] = None


class ProfilResponsableAPDPOut(ProfilResponsableAPDPCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str


class TraitementAPDPCreate(BaseModel):
    traitement_id: str

    donnees_personnelles: Optional[str] = None
    origine_donnees: Optional[str] = None

    personnes_salaries: Optional[bool] = None
    personnes_adherents: Optional[bool] = None
    personnes_usagers: Optional[bool] = None
    personnes_visiteurs: Optional[bool] = None
    personnes_patients: Optional[bool] = None
    personnes_clients: Optional[bool] = None
    personnes_eleves_etudiants: Optional[bool] = None
    personnes_autres: Optional[str] = None
    nombre_personnes: Optional[int] = None

    operation_collecte: Optional[bool] = None
    operation_developpement: Optional[bool] = None
    operation_exposition_affichage: Optional[bool] = None
    operation_conservation: Optional[bool] = None
    operation_copie: Optional[bool] = None
    operation_traitement_image: Optional[bool] = None
    operation_exploitation: Optional[bool] = None
    operation_enregistrement: Optional[bool] = None
    operation_adaptation: Optional[bool] = None
    operation_modification: Optional[bool] = None
    operation_extraction: Optional[bool] = None
    operation_sauvegarde: Optional[bool] = None
    operation_consultation: Optional[bool] = None
    operation_utilisation: Optional[bool] = None
    operation_communication_transmission_diffusion: Optional[bool] = None
    operation_structuration_rapprochement_interconnexion: Optional[bool] = None
    operation_limitation: Optional[bool] = None
    operation_cryptage: Optional[bool] = None
    operation_effacement: Optional[bool] = None
    operation_destruction: Optional[bool] = None
    operation_organisation: Optional[bool] = None
    operation_autre: Optional[str] = None

    type_video_photo: Optional[bool] = None
    type_site_web_application: Optional[bool] = None
    type_biometrique: Optional[bool] = None

    procedure_manuelle: Optional[bool] = None
    procedure_automatisee: Optional[bool] = None
    caracteristiques_techniques: Optional[str] = None
    fonctionnalites: Optional[str] = None

    duree_conservation: Optional[str] = None
    texte_legal_reglementaire_conservation: Optional[str] = None
    support_papier: Optional[bool] = None
    support_numerique: Optional[bool] = None
    autre_support: Optional[str] = None

    lieu_stockage: Optional[str] = None
    modalites_stockage: Optional[str] = None
    responsable_stockage: Optional[str] = None
    stockage_systeme_ordinaire: Optional[bool] = None
    stockage_cloud: Optional[bool] = None
    stockage_local_nas: Optional[bool] = None
    stockage_lvm: Optional[bool] = None

    sous_traitance_oui_non: Optional[bool] = None
    sous_traitance_annexe: Optional[str] = None

    communication_oui_non: Optional[bool] = None
    communication_benin_cedeao: Optional[str] = None
    communication_annexe: Optional[str] = None

    interconnexion_oui_non: Optional[bool] = None
    interconnexion_annexe: Optional[str] = None

    transfert_oui_non: Optional[bool] = None
    transfert_pays_tiers: Optional[str] = None
    transfert_autorisation_annexe: Optional[str] = None


class TraitementAPDPOut(TraitementAPDPCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str


class PrincipesAPDPCreate(BaseModel):
    traitement_id: str

    licéite_consentement: Optional[bool] = None
    licéite_contrat: Optional[bool] = None
    licéite_obligation_legale: Optional[bool] = None
    licéite_interet_legitime: Optional[bool] = None
    licéite_interet_public: Optional[bool] = None
    licéite_interets_vitaux: Optional[bool] = None
    licéite_exceptions: Optional[str] = None

    information_prealable: Optional[bool] = None
    information_exceptions: Optional[str] = None
    information_modalites: Optional[str] = None
    information_contenu: Optional[str] = None
    information_preuve: Optional[str] = None

    consentement_mode: Optional[str] = None
    consentement_finalites: Optional[str] = None
    consentement_duree: Optional[str] = None

    pertinence_utilite: Optional[str] = None
    pertinence_quantite: Optional[str] = None
    pertinence_adequation: Optional[str] = None


class PrincipesAPDPOut(PrincipesAPDPCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str


class SecuriteAPDPCreate(BaseModel):
    traitement_id: str

    personnes_autorisees: Optional[str] = None
    protection_intervention_non_autorisee: Optional[str] = None

    politique_acces_physique: Optional[str] = None
    mesures_physiques: Optional[str] = None
    mesures_electroniques: Optional[str] = None
    autres_mesures: Optional[str] = None

    protection_incendie: Optional[str] = None
    protection_inondation: Optional[str] = None
    protection_surtensions: Optional[str] = None
    protection_phenomenes_magnetiques: Optional[str] = None

    mesures_organisationnelles: Optional[str] = None
    mesures_logiques: Optional[str] = None
    tests: Optional[str] = None
    certifications: Optional[str] = None
    verification_identite: Optional[str] = None
    journalisation: Optional[str] = None
    authentification_multifacteur: Optional[str] = None
    chiffrement: Optional[str] = None
    sensibilisation_personnel: Optional[str] = None
    mesures_juridiques: Optional[str] = None

    confidentialite: Optional[str] = None
    integrite: Optional[str] = None
    disponibilite: Optional[str] = None
    sauvegardes: Optional[str] = None
    continuite_energie: Optional[str] = None
    architecture_reseau: Optional[str] = None


class SecuriteAPDPOut(SecuriteAPDPCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str


class DroitsPersonnesAPDPCreate(BaseModel):
    traitement_id: str

    droit_acces: Optional[str] = None
    droit_portabilite: Optional[str] = None
    droit_opposition_retrait_consentement: Optional[str] = None
    droit_interrogation: Optional[str] = None
    droit_rectification_suppression: Optional[str] = None
    droit_oubli_numerique: Optional[str] = None

    modalites_exercice: Optional[str] = None
    responsable_exercice: Optional[str] = None
    delai_exercice: Optional[str] = None


class DroitsPersonnesAPDPOut(DroitsPersonnesAPDPCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str


class TraitementsAnterieursAPDPCreate(BaseModel):
    traitement_id: str

    enregistrement_apdp_anterieur: Optional[str] = None
    reference_apdp_anterieure: Optional[str] = None
    registre_activites_a_jour: Optional[str] = None
    dpo_designe: Optional[str] = None
    representant_legal_declaration: Optional[str] = None
    declaration_sur_honneur: Optional[str] = None


class TraitementsAnterieursAPDPOut(TraitementsAnterieursAPDPCreate):
    model_config = ConfigDict(from_attributes=True)
    id: str

# ============================================================
# APDP — INCIDENTS / VIOLATIONS — WORKFLOW 72 H
# ============================================================

class IncidentCreate(BaseModel):
    organisation_id: str
    traitement_id: Optional[str] = None

    # Identification du déclarant
    sexe_declarant: Optional[str] = None
    nom_famille: Optional[str] = None
    prenoms: Optional[str] = None
    adresse: Optional[str] = None
    quartier_lieu_dit: Optional[str] = None
    arrondissement: Optional[str] = None
    commune: Optional[str] = None
    pays: Optional[str] = None
    telephone_portable: Optional[str] = None
    boite_postale: Optional[str] = None
    adresse_electronique: Optional[str] = None

    # Type de violation
    types_violation: list[str] = []
    violation_autre: Optional[str] = None

    # Informations sur la violation
    auteur_presume_nom: Optional[str] = None
    auteur_presume_ville: Optional[str] = None
    auteur_presume_pays: Optional[str] = None
    auteur_presume_contact: Optional[str] = None

    date_heure_violation: Optional[datetime] = None
    date_heure_constatation: datetime
    lieu_violation: Optional[str] = None
    resume_incident: Optional[str] = None

    # Données personnelles concernées
    donnees_personnelles_concernees: Optional[str] = None

    # Conséquences potentielles
    consequences_potentielles: list[str] = []

    # Observations techniques
    observations_techniques: Optional[str] = None

    # Pièces
    pieces: list[str] = []


class IncidentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    organisation_id: str
    traitement_id: Optional[str]

    sexe_declarant: Optional[str]
    nom_famille: Optional[str]
    prenoms: Optional[str]
    adresse: Optional[str]
    quartier_lieu_dit: Optional[str]
    arrondissement: Optional[str]
    commune: Optional[str]
    pays: Optional[str]
    telephone_portable: Optional[str]
    boite_postale: Optional[str]
    adresse_electronique: Optional[str]

    types_violation: list[str]
    violation_autre: Optional[str]

    auteur_presume_nom: Optional[str]
    auteur_presume_ville: Optional[str]
    auteur_presume_pays: Optional[str]
    auteur_presume_contact: Optional[str]

    date_heure_violation: Optional[datetime]
    date_heure_constatation: datetime
    lieu_violation: Optional[str]
    resume_incident: Optional[str]

    donnees_personnelles_concernees: Optional[str]
    consequences_potentielles: list[str]
    observations_techniques: Optional[str]
    pieces: list[str]

    statut: str
    echeance_notification: datetime
    date_notification: Optional[datetime]
    notification_dans_les_delais: Optional[bool]

    date_creation: datetime
    derniere_revision: datetime
# ============================================================
# APDP — MISE À JOUR INCIDENT / SUIVI NOTIFICATION 72 H
# ============================================================

class IncidentUpdate(BaseModel):
    statut: Optional[str] = None
    date_notification: Optional[datetime] = None
