"""
Modèles cœur du registre — Phase 2 du plan de construction.

Tables volontairement limitées au strict nécessaire pour faire tourner
un premier CRUD de bout en bout (Phase 3). Les tables suivantes seront
ajoutées au fur et à mesure, une par formulaire implémenté :

  - sous_traitants, communications, interconnexions, transferts
    (+ leurs tables filles) -> Annexes 1-4
  - capteurs_dispositifs, site_web_traitements -> formulaires complémentaires
  - annexes_activees -> quelles annexes s'appliquent à un traitement
  - mesures_securite, documents_joints
  - grille_ponderation, grille_champs, scores_conformite, scores_risque
  - incidents, documents_generes, traitements_versions
  - formations_sensibilisation, demandes_exercice_droits, relations_apdp,
    audits_conformite, plan_remediation (rapport annuel)

Voir ComplianceForge_Synthese_Globale.docx pour le schéma complet.
"""

import enum
import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column, String, Boolean, DateTime, ForeignKey, Enum, Text, Integer, Float, JSON,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


def gen_uuid():
    return str(uuid.uuid4())


class StatutTraitement(str, enum.Enum):
    brouillon = "brouillon"
    actif = "actif"
    archive = "archive"


class RoleUtilisateur(str, enum.Enum):
    dpo = "dpo"
    metier = "metier"
    direction = "direction"
    admin = "admin"


class Organisation(Base):
    """Support du multi-tenant — voir section 5 de la synthèse (organisation_id partout)."""
    __tablename__ = "organisations"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    nom = Column(String, nullable=False)
    secteur_activite = Column(String)
    ifu_rccm = Column(String)
    adresse = Column(String)
    contact_dpo_email = Column(String)
    date_creation = Column(DateTime, default=datetime.utcnow)

    utilisateurs = relationship("Utilisateur", back_populates="organisation")
    traitements = relationship("Traitement", back_populates="organisation")


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    organisation_id = Column(UUID(as_uuid=False), ForeignKey("organisations.id"), nullable=True)
    nom = Column(String, nullable=False)
    prenoms = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    fonction = Column(String)
    role = Column(Enum(RoleUtilisateur), nullable=False, default=RoleUtilisateur.metier)
    mot_de_passe_hash = Column(String, nullable=False)

    # Authentification / vérification e-mail
    email_verifie = Column(Boolean, nullable=False, default=False)

    token_verification_hash = Column(String, nullable=True)
    token_verification_expire_at = Column(DateTime, nullable=True)

    token_reset_hash = Column(String, nullable=True)
    token_reset_expire_at = Column(DateTime, nullable=True)

    date_creation = Column(DateTime, default=datetime.utcnow)

    organisation = relationship("Organisation", back_populates="utilisateurs")


class Traitement(Base):
    """Le registre pivot — table centrale de toute la plateforme."""
    __tablename__ = "traitements"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    organisation_id = Column(UUID(as_uuid=False), ForeignKey("organisations.id"), nullable=False)
    nom = Column(String, nullable=False)
    service_responsable = Column(String)
    statut = Column(Enum(StatutTraitement), default=StatutTraitement.brouillon)

    finalite = Column(Text)
    base_legale = Column(String)
    justification_base_legale = Column(Text)

    responsable_id = Column(UUID(as_uuid=False), ForeignKey("utilisateurs.id"), nullable=True)
    dpo_id = Column(UUID(as_uuid=False), ForeignKey("utilisateurs.id"), nullable=True)

    reference_apdp_anterieure = Column(String, nullable=True)
    date_mise_en_oeuvre = Column(DateTime, nullable=True)
    sensibilite_donnees = Column(Integer, nullable=True)
    niveau_mesures_securite = Column(Integer, nullable=True)
    sous_traitance_transferts = Column(Integer, nullable=True)
    exposition = Column(Integer, nullable=True)
    volume = Column(Integer, nullable=True)
    date_creation = Column(DateTime, default=datetime.utcnow)
    derniere_revision = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    organisation = relationship("Organisation", back_populates="traitements")
    categories_donnees = relationship(
        "CategorieDonnee", back_populates="traitement", cascade="all, delete-orphan"
    )


class CategorieDonnee(Base):
    """Une ligne par catégorie de donnée déclarée pour un traitement."""
    __tablename__ = "categories_donnees"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    traitement_id = Column(UUID(as_uuid=False), ForeignKey("traitements.id"), nullable=False)
    categorie = Column(String, nullable=False)  # ex: identification, donnees_sociales, sensibles...
    sensible = Column(Boolean, default=False)

    traitement = relationship("Traitement", back_populates="categories_donnees")
class ScoreConformite(Base):
    __tablename__ = "scores_conformite"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    traitement_id = Column(UUID(as_uuid=False), ForeignKey("traitements.id"), nullable=False)
    score_global = Column(Float, nullable=False)
    version_grille = Column(String, nullable=False)
    details = Column(JSON, nullable=False)
    date_calcul = Column(DateTime, default=datetime.utcnow)


class ScoreRisque(Base):
    __tablename__ = "scores_risque"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    traitement_id = Column(UUID(as_uuid=False), ForeignKey("traitements.id"), nullable=False)
    score_global = Column(Float, nullable=False)
    niveau = Column(String, nullable=False)
    composantes = Column(JSON, nullable=False)
    date_calcul = Column(DateTime, default=datetime.utcnow)

class DocumentGenere(Base):
    __tablename__ = "documents_generes"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    traitement_id = Column(UUID(as_uuid=False), ForeignKey("traitements.id"), nullable=False)
    type_document = Column(String, nullable=False)
    chemin_fichier = Column(String, nullable=False)
    nom_fichier = Column(String, nullable=False)
    hash_integrite = Column(String, nullable=False)
    template_version = Column(String, nullable=False)
    date_generation = Column(DateTime, default=datetime.utcnow)
# ============================================================
# APDP — FORMULAIRE UNIQUE
# ============================================================

class ProfilResponsableAPDP(Base):
    """
    Section I — Identification du responsable de traitement.
    """

    __tablename__ = "profils_responsables_apdp"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    organisation_id = Column(
        UUID(as_uuid=False),
        ForeignKey("organisations.id"),
        nullable=False,
        unique=True,
    )

    # Responsable de traitement
    nom_prenoms_raison_sociale = Column(Text)
    npi_rccm = Column(String)
    carre_lot = Column(String)
    quartier = Column(String)
    ville = Column(String)
    adresse_postale = Column(Text)
    adresse_electronique = Column(String)
    contact_telephonique = Column(String)
    autres_contacts = Column(Text)
    activite = Column(Text)
    secteur_activite = Column(String)

    # Représentant légal
    representant_legal_nom_prenoms = Column(Text)
    representant_legal_npi = Column(String)
    representant_legal_adresse = Column(Text)
    representant_legal_contacts = Column(Text)

    organisation = relationship("Organisation")


class TraitementAPDP(Base):
    """
    Section II — Le traitement envisagé.
    """

    __tablename__ = "traitements_apdp"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    traitement_id = Column(
        UUID(as_uuid=False),
        ForeignKey("traitements.id"),
        nullable=False,
        unique=True,
    )

    # ========================================================
    # II.A — DONNÉES PERSONNELLES
    # ========================================================

    donnees_personnelles = Column(Text)
    origine_donnees = Column(Text)

    # ========================================================
    # II.B — PERSONNES CONCERNÉES
    # ========================================================

    personnes_salaries = Column(Boolean)
    personnes_adherents = Column(Boolean)
    personnes_usagers = Column(Boolean)
    personnes_visiteurs = Column(Boolean)
    personnes_patients = Column(Boolean)
    personnes_clients = Column(Boolean)
    personnes_eleves_etudiants = Column(Boolean)
    personnes_autres = Column(Text)

    nombre_personnes = Column(Integer)

    # ========================================================
    # II.C — OPÉRATIONS DE TRAITEMENT
    # ========================================================

    operation_collecte = Column(Boolean)
    operation_developpement = Column(Boolean)
    operation_exposition_affichage = Column(Boolean)
    operation_conservation = Column(Boolean)
    operation_copie = Column(Boolean)
    operation_traitement_image = Column(Boolean)
    operation_exploitation = Column(Boolean)
    operation_enregistrement = Column(Boolean)
    operation_adaptation = Column(Boolean)
    operation_modification = Column(Boolean)
    operation_extraction = Column(Boolean)
    operation_sauvegarde = Column(Boolean)
    operation_consultation = Column(Boolean)
    operation_utilisation = Column(Boolean)

    operation_communication_transmission_diffusion = Column(Boolean)
    operation_structuration_rapprochement_interconnexion = Column(Boolean)
    operation_limitation = Column(Boolean)
    operation_cryptage = Column(Boolean)
    operation_effacement = Column(Boolean)
    operation_destruction = Column(Boolean)
    operation_organisation = Column(Boolean)
    operation_autre = Column(Text)

    # ========================================================
    # II.C — TYPE DE TRAITEMENT
    # ========================================================

    type_video_photo = Column(Boolean)
    type_site_web_application = Column(Boolean)
    type_biometrique = Column(Boolean)

    # ========================================================
    # II.C — PROCÉDURE
    # ========================================================

    procedure_manuelle = Column(Boolean)
    procedure_automatisee = Column(Boolean)

    caracteristiques_techniques = Column(Text)
    fonctionnalites = Column(Text)

    # ========================================================
    # II.F — CONSERVATION
    # ========================================================

    duree_conservation = Column(Text)
    texte_legal_reglementaire_conservation = Column(Text)

    support_papier = Column(Boolean)
    support_numerique = Column(Boolean)
    autre_support = Column(Text)

    # ========================================================
    # II.G — STOCKAGE
    # ========================================================

    lieu_stockage = Column(Text)
    modalites_stockage = Column(Text)
    responsable_stockage = Column(Text)

    stockage_systeme_ordinaire = Column(Boolean)
    stockage_cloud = Column(Boolean)
    stockage_local_nas = Column(Boolean)
    stockage_lvm = Column(Boolean)

    # ========================================================
    # II.H — PARTAGE
    # ========================================================

    sous_traitance_oui_non = Column(Boolean)
    sous_traitance_annexe = Column(Text)

    communication_oui_non = Column(Boolean)
    communication_benin_cedeao = Column(Text)
    communication_annexe = Column(Text)

    interconnexion_oui_non = Column(Boolean)
    interconnexion_annexe = Column(Text)

    transfert_oui_non = Column(Boolean)
    transfert_pays_tiers = Column(Text)
    transfert_autorisation_annexe = Column(Text)

    # ========================================================
    # II.I — MISE EN ŒUVRE
    # ========================================================

    traitement = relationship("Traitement")


class PrincipesAPDP(Base):
    """
    Section III — Respect des principes relatifs au traitement.
    """

    __tablename__ = "principes_apdp"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    traitement_id = Column(
        UUID(as_uuid=False),
        ForeignKey("traitements.id"),
        nullable=False,
        unique=True,
    )

    # III.A — Licéité / légitimité
    licéite_consentement = Column(Boolean)
    licéite_contrat = Column(Boolean)
    licéite_obligation_legale = Column(Boolean)
    licéite_interet_legitime = Column(Boolean)
    licéite_interet_public = Column(Boolean)
    licéite_interets_vitaux = Column(Boolean)
    licéite_exceptions = Column(Text)

    # III.B — Transparence / loyauté
    information_prealable = Column(Boolean)
    information_exceptions = Column(Text)
    information_modalites = Column(Text)
    information_contenu = Column(Text)
    information_preuve = Column(Text)

    consentement_mode = Column(Text)
    consentement_finalites = Column(Text)
    consentement_duree = Column(Text)

    # III.C — Pertinence / proportionnalité / minimisation
    pertinence_utilite = Column(Text)
    pertinence_quantite = Column(Text)
    pertinence_adequation = Column(Text)

    traitement = relationship("Traitement")

class SecuriteAPDP(Base):
    """
    Section IV — Sécurité du dispositif.
    """

    __tablename__ = "securites_apdp"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    traitement_id = Column(
        UUID(as_uuid=False),
        ForeignKey("traitements.id"),
        nullable=False,
        unique=True,
    )

    # IV — Accès au système
    personnes_autorisees = Column(Text)
    protection_intervention_non_autorisee = Column(Text)

    # IV — Sécurité physique
    politique_acces_physique = Column(Text)
    mesures_physiques = Column(Text)
    mesures_electroniques = Column(Text)
    autres_mesures = Column(Text)

    protection_incendie = Column(Text)
    protection_inondation = Column(Text)
    protection_surtensions = Column(Text)
    protection_phenomenes_magnetiques = Column(Text)

    # IV — Sécurité organisationnelle / logique
    mesures_organisationnelles = Column(Text)
    mesures_logiques = Column(Text)
    tests = Column(Text)
    certifications = Column(Text)
    verification_identite = Column(Text)
    journalisation = Column(Text)
    authentification_multifacteur = Column(Text)
    chiffrement = Column(Text)
    sensibilisation_personnel = Column(Text)
    mesures_juridiques = Column(Text)

    # IV — Confidentialité / intégrité / disponibilité
    confidentialite = Column(Text)
    integrite = Column(Text)
    disponibilite = Column(Text)

    sauvegardes = Column(Text)
    continuite_energie = Column(Text)
    architecture_reseau = Column(Text)

    traitement = relationship("Traitement")


class DroitsPersonnesAPDP(Base):
    """
    Section V — Droits des personnes concernées.
    """

    __tablename__ = "droits_personnes_apdp"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    traitement_id = Column(
        UUID(as_uuid=False),
        ForeignKey("traitements.id"),
        nullable=False,
        unique=True,
    )

    # V — Droits
    droit_acces = Column(Text)
    droit_portabilite = Column(Text)
    droit_opposition_retrait_consentement = Column(Text)
    droit_interrogation = Column(Text)
    droit_rectification_suppression = Column(Text)
    droit_oubli_numerique = Column(Text)

    # V — Modalités d'exercice
    modalites_exercice = Column(Text)
    responsable_exercice = Column(Text)
    delai_exercice = Column(Text)

    traitement = relationship("Traitement")


class TraitementsAnterieursAPDP(Base):
    """
    Section VI — Traitements antérieurs.
    """

    __tablename__ = "traitements_anterieurs_apdp"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    traitement_id = Column(
        UUID(as_uuid=False),
        ForeignKey("traitements.id"),
        nullable=False,
        unique=True,
    )

    # VI — Situation antérieure auprès de l'APDP
    enregistrement_apdp_anterieur = Column(Text)
    reference_apdp_anterieure = Column(String)

    # VI — Registre des activités
    registre_activites_a_jour = Column(Text)

    # VI — DPO
    dpo_designe = Column(Text)

    # VI — Représentant légal
    representant_legal_declaration = Column(Text)

    # VI — Déclaration sur l'honneur
    declaration_sur_honneur = Column(Text)

    traitement = relationship("Traitement")
# ============================================================
# APDP — GESTION DES VIOLATIONS DE DONNÉES — WORKFLOW 72 H
# ============================================================

class StatutIncident(str, enum.Enum):
    nouveau = "nouveau"
    analyse = "analyse"
    notification_preparee = "notification_preparee"
    notifie = "notifie"
    cloture = "cloture"


class Incident(Base):
    """
    Incident / violation de données personnelles.

    Les champs correspondent aux informations du formulaire
    officiel APDP de signalement et aux éléments nécessaires
    au suivi interne du délai de notification.
    """

    __tablename__ = "incidents"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)

    organisation_id = Column(
        UUID(as_uuid=False),
        ForeignKey("organisations.id"),
        nullable=False,
    )

    traitement_id = Column(
        UUID(as_uuid=False),
        ForeignKey("traitements.id"),
        nullable=True,
    )

    # --------------------------------------------------------
    # Identification du déclarant
    # --------------------------------------------------------

    sexe_declarant = Column(String)
    nom_famille = Column(String)
    prenoms = Column(String)
    adresse = Column(Text)
    quartier_lieu_dit = Column(String)
    arrondissement = Column(String)
    commune = Column(String)
    pays = Column(String)
    telephone_portable = Column(String)
    boite_postale = Column(String)
    adresse_electronique = Column(String)

    # --------------------------------------------------------
    # Type de violation
    # --------------------------------------------------------

    types_violation = Column(JSON, nullable=False, default=list)
    violation_autre = Column(Text)

    # --------------------------------------------------------
    # Informations sur la violation
    # --------------------------------------------------------

    auteur_presume_nom = Column(Text)
    auteur_presume_ville = Column(String)
    auteur_presume_pays = Column(String)
    auteur_presume_contact = Column(String)

    date_heure_violation = Column(DateTime, nullable=True)
    date_heure_constatation = Column(DateTime, nullable=False)
    lieu_violation = Column(Text)

    resume_incident = Column(Text)

    # --------------------------------------------------------
    # Données personnelles concernées
    # --------------------------------------------------------

    donnees_personnelles_concernees = Column(Text)

    # --------------------------------------------------------
    # Conséquences potentielles
    # --------------------------------------------------------

    consequences_potentielles = Column(JSON, nullable=False, default=list)

    # --------------------------------------------------------
    # Observations techniques
    # --------------------------------------------------------

    observations_techniques = Column(Text)

    # --------------------------------------------------------
    # Pièces
    # --------------------------------------------------------

    pieces = Column(JSON, nullable=False, default=list)

    # --------------------------------------------------------
    # Workflow interne — délai de 72 h
    # --------------------------------------------------------

    statut = Column(
        Enum(StatutIncident),
        nullable=False,
        default=StatutIncident.nouveau,
    )

    echeance_notification = Column(DateTime, nullable=False)

    date_notification = Column(DateTime, nullable=True)

    notification_dans_les_delais = Column(Boolean, nullable=True)

    date_creation = Column(DateTime, default=datetime.utcnow)
    derniere_revision = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    organisation = relationship("Organisation")
    traitement = relationship("Traitement")


# ============================================================
# AUTHENTIFICATION — JOURNAL DE SÉCURITÉ
# ============================================================

class JournalSecurite(Base):
    """
    Journal serveur des événements de sécurité liés aux comptes.
    Aucun mot de passe, JWT ou token sensible n'est enregistré.
    """

    __tablename__ = "journal_securite"

    id = Column(
        UUID(as_uuid=False),
        primary_key=True,
        default=gen_uuid,
    )

    utilisateur_id = Column(
        UUID(as_uuid=False),
        ForeignKey("utilisateurs.id"),
        nullable=True,
    )

    evenement = Column(
        String,
        nullable=False,
    )

    description = Column(
        Text,
        nullable=False,
    )

    adresse_ip = Column(
        String,
        nullable=True,
    )

    user_agent = Column(
        Text,
        nullable=True,
    )

    date_evenement = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    utilisateur = relationship(
        "Utilisateur",
        backref="evenements_securite",
    )
