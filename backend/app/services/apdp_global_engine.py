"""
Moteur global APDP.

Objectif :
- centraliser les données communes aux 8 formulaires APDP ;
- éviter de demander deux fois la même information ;
- conserver les mappings PDF propres à chaque document ;
- ne jamais modifier la structure officielle des PDF.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


APDP_DOCUMENTS = {
    "formulaire_unique": {
        "title": "Formulaire de formalités préalables — traitement envisagé",
        "template": "templates/apdp/formulaire_unique.pdf",
    },
    "annexe_1_sous_traitance": {
        "title": "Annexe 1 : Sous-traitance",
        "template": "templates/apdp/annexe_1_sous_traitance.pdf",
    },
    "annexe_2_communication": {
        "title": "Annexe 2 : Communication",
        "template": "templates/apdp/annexe_2_communication.pdf",
    },
    "annexe_3_interconnexion": {
        "title": "Annexe 3 : Interconnexion",
        "template": "templates/apdp/annexe_3_interconnexion.pdf",
    },
    "annexe_4_transfert": {
        "title": "Annexe 4 : Transfert",
        "template": "templates/apdp/annexe_4_transfert.pdf",
    },
    "formulaire_capteurs": {
        "title": "Formulaire complémentaire — traitements par capteurs",
        "template": "templates/apdp/formulaire_capteurs.pdf",
    },
    "formulaire_site_web": {
        "title": "Formulaire complémentaire — traitements sur site web",
        "template": "templates/apdp/formulaire_site_web.pdf",
    },
    "engagement_conformite": {
        "title": "Formulaire d’engagement de conformité",
        "template": "templates/apdp/engagement_conformite.pdf",
    },
}


# ---------------------------------------------------------------------------
# DONNÉES COMMUNES
# ---------------------------------------------------------------------------

COMMON_FIELDS = {
    "responsable_traitement": {
        "nom_prenoms_raison_sociale": None,
        "npi_rccm": None,
        "carre_lot": None,
        "quartier": None,
        "ville": None,
        "adresse_postale": None,
        "adresse_electronique": None,
        "contact_telephonique": None,
        "autres_contacts": None,
        "activite": None,
        "secteur": None,
    },

    "representant_legal": {
        "nom_prenoms": None,
        "npi": None,
        "carre_lot": None,
        "quartier": None,
        "ville": None,
        "adresse_postale": None,
        "adresse_electronique": None,
        "contact_telephonique": None,
        "autres_contacts": None,
    },

    "traitement": {
        "origine_donnees": None,
        "nombre_personnes": None,
        "caracteristiques_techniques": None,
        "fonctionnalites_systeme": None,
        "duree_conservation": None,
        "texte_legal_conservation": None,
    },

    "declaration_honneur": {
        "nom_prenom": None,
        "fonction": None,
        "date": None,
    },
}


# ---------------------------------------------------------------------------
# ALIAS
#
# Chaque alias relie un champ d'un PDF à une donnée métier commune.
# On ne fait PAS de correspondance automatique sur les noms "autres",
# "autres_precision", etc. : ils restent spécifiques à leur formulaire.
# ---------------------------------------------------------------------------

FIELD_ALIASES = {

    # ---------------- FORMULAIRE UNIQUE ----------------

    "formulaire_unique.1.nom_prenoms_raison_sociale":
        "responsable_traitement.nom_prenoms_raison_sociale",

    "formulaire_unique.1.npi_rccm":
        "responsable_traitement.npi_rccm",

    "formulaire_unique.1.carre_lot":
        "responsable_traitement.carre_lot",

    "formulaire_unique.1.quartier":
        "responsable_traitement.quartier",

    "formulaire_unique.1.ville":
        "responsable_traitement.ville",

    "formulaire_unique.1.adresse_postale":
        "responsable_traitement.adresse_postale",

    "formulaire_unique.1.adresse_electronique":
        "responsable_traitement.adresse_electronique",

    "formulaire_unique.1.contact_telephonique":
        "responsable_traitement.contact_telephonique",

    "formulaire_unique.1.autres_contacts":
        "responsable_traitement.autres_contacts",

    "formulaire_unique.1.activite":
        "responsable_traitement.activite",

    "formulaire_unique.1.representant_legal_nom_prenoms":
        "representant_legal.nom_prenoms",

    "formulaire_unique.1.representant_legal_npi":
        "representant_legal.npi",

    "formulaire_unique.1.representant_legal_carre_lot":
        "representant_legal.carre_lot",

    "formulaire_unique.1.representant_legal_quartier":
        "representant_legal.quartier",

    "formulaire_unique.1.representant_legal_ville":
        "representant_legal.ville",

    "formulaire_unique.1.representant_legal_adresse":
        "representant_legal.adresse_postale",

    "formulaire_unique.1.representant_legal_adresse_electronique":
        "representant_legal.adresse_electronique",

    "formulaire_unique.1.representant_legal_contact":
        "representant_legal.contact_telephonique",

    "formulaire_unique.1.representant_legal_autres_contacts":
        "representant_legal.autres_contacts",

    "formulaire_unique.2.origine_donnees":
        "traitement.origine_donnees",

    "formulaire_unique.2.nombre_personnes":
        "traitement.nombre_personnes",

    "formulaire_unique.2.caracteristiques_techniques":
        "traitement.caracteristiques_techniques",

    "formulaire_unique.2.fonctionnalites_systeme":
        "traitement.fonctionnalites_systeme",

    "formulaire_unique.3.duree_conservation":
        "traitement.duree_conservation",

    "formulaire_unique.3.texte_legal_conservation":
        "traitement.texte_legal_conservation",


    # ---------------- ENGAGEMENT CONFORMITÉ ----------------

    "engagement_conformite.page_1.identification_responsable_traitement.nom_prenoms_raison_sociale":
        "responsable_traitement.nom_prenoms_raison_sociale",

    "engagement_conformite.page_1.identification_responsable_traitement.npi_rccm":
        "responsable_traitement.npi_rccm",

    "engagement_conformite.page_1.identification_responsable_traitement.carre_lot":
        "responsable_traitement.carre_lot",

    "engagement_conformite.page_1.identification_responsable_traitement.quartier":
        "responsable_traitement.quartier",

    "engagement_conformite.page_1.identification_responsable_traitement.ville":
        "responsable_traitement.ville",

    "engagement_conformite.page_1.identification_responsable_traitement.adresse_postale":
        "responsable_traitement.adresse_postale",

    "engagement_conformite.page_1.identification_responsable_traitement.adresse_electronique":
        "responsable_traitement.adresse_electronique",

    "engagement_conformite.page_1.identification_responsable_traitement.contact_telephonique":
        "responsable_traitement.contact_telephonique",

    "engagement_conformite.page_1.identification_responsable_traitement.autres_contacts":
        "responsable_traitement.autres_contacts",

    "engagement_conformite.page_1.identification_responsable_traitement.activite":
        "responsable_traitement.activite",

    "engagement_conformite.page_1.representant_legal.nom_prenoms":
        "representant_legal.nom_prenoms",

    "engagement_conformite.page_1.representant_legal.npi":
        "representant_legal.npi",

    "engagement_conformite.page_1.representant_legal.carre_lot":
        "representant_legal.carre_lot",

    "engagement_conformite.page_1.representant_legal.quartier":
        "representant_legal.quartier",

    "engagement_conformite.page_1.representant_legal.ville":
        "representant_legal.ville",

    "engagement_conformite.page_1.representant_legal.adresse_postale":
        "representant_legal.adresse_postale",

    "engagement_conformite.page_1.representant_legal.adresse_electronique":
        "representant_legal.adresse_electronique",

    "engagement_conformite.page_1.representant_legal.contact_telephonique":
        "representant_legal.contact_telephonique",

    "engagement_conformite.page_1.representant_legal.autres_contacts":
        "representant_legal.autres_contacts",

    "engagement_conformite.page_2.donnees_personnelles.origine_donnees":
        "traitement.origine_donnees",

    "engagement_conformite.page_2.personnes_concernees.nombre_personnes":
        "traitement.nombre_personnes",

    "engagement_conformite.page_2.caracteristiques_techniques":
        "traitement.caracteristiques_techniques",

    "engagement_conformite.page_3.type_traitement.caracteristiques_techniques":
        "traitement.caracteristiques_techniques",

    "engagement_conformite.page_3.type_traitement.fonctionnalites_systeme":
        "traitement.fonctionnalites_systeme",

    "engagement_conformite.page_3.conservation_donnees.duree_conservation":
        "traitement.duree_conservation",

    "engagement_conformite.page_3.conservation_donnees.texte_legal_conservation":
        "traitement.texte_legal_conservation",


    # ---------------- ANNEXE 4 ----------------

    "annexe_4.page_2.nombre_personnes":
        "traitement.nombre_personnes",


    # ---------------- CAPTEURS ----------------

    "formulaire_capteurs.page_1.donnees_personnelles.origine_donnees":
        "traitement.origine_donnees",


    # ---------------- SITE WEB ----------------

    "formulaire_site_web.page_1.donnees_personnelles_concernees.origine_donnees":
        "traitement.origine_donnees",
}


# ---------------------------------------------------------------------------
# OUTILS
# ---------------------------------------------------------------------------

def empty_dossier() -> dict[str, Any]:
    """Retourne un dossier APDP vierge."""
    return deepcopy(COMMON_FIELDS)


def get_common_value(dossier: dict[str, Any], common_key: str) -> Any:
    """Lit une donnée commune avec notation pointée."""
    current: Any = dossier

    for part in common_key.split("."):
        if not isinstance(current, dict):
            return None

        current = current.get(part)

    return current


def set_common_value(
    dossier: dict[str, Any],
    common_key: str,
    value: Any,
) -> None:
    """Écrit une donnée commune avec notation pointée."""
    parts = common_key.split(".")
    current = dossier

    for part in parts[:-1]:
        current = current.setdefault(part, {})

    current[parts[-1]] = value


def common_fields_for_document(document_id: str) -> dict[str, str]:
    """Retourne les champs communs utilisés par un document."""
    prefix = f"{document_id}."
    result = {}

    for pdf_field, common_field in FIELD_ALIASES.items():
        if pdf_field.startswith(prefix):
            result[pdf_field] = common_field

    return result


def resolve_document_data(
    document_id: str,
    dossier: dict[str, Any],
    specific_data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Prépare les données destinées à un formulaire.

    Les données communes sont injectées à partir du dossier.
    Les données spécifiques du formulaire sont ensuite ajoutées.
    """
    result = {}

    for pdf_field, common_field in common_fields_for_document(
        document_id
    ).items():
        value = get_common_value(dossier, common_field)

        if value is not None:
            result[pdf_field] = value

    if specific_data:
        result.update(specific_data)

    return result


def documents_using_common_field(common_key: str) -> list[str]:
    """Retourne les documents qui utilisent une donnée commune."""
    documents = []

    for pdf_field, field in FIELD_ALIASES.items():
        if field != common_key:
            continue

        document_id = pdf_field.split(".", 1)[0]

        if document_id not in documents:
            documents.append(document_id)

    return documents


def validate_dossier(dossier: dict[str, Any]) -> list[str]:
    """
    Vérifie uniquement la structure du dossier.
    Ne force aucune donnée métier obligatoire.
    """
    errors = []

    if not isinstance(dossier, dict):
        errors.append("Le dossier APDP doit être un objet.")

    return errors


__all__ = [
    "APDP_DOCUMENTS",
    "COMMON_FIELDS",
    "FIELD_ALIASES",
    "empty_dossier",
    "get_common_value",
    "set_common_value",
    "common_fields_for_document",
    "resolve_document_data",
    "documents_using_common_field",
    "validate_dossier",
]
