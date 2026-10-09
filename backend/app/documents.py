"""
Génération de documents — Phase 5 du plan de construction.
"""
import hashlib
from datetime import datetime
from pathlib import Path

from docxtpl import DocxTemplate

from app import models

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
DOCUMENTS_DIR = Path(__file__).parent.parent / "documents"
DOCUMENTS_DIR.mkdir(exist_ok=True)


def build_context_fiche_synthese(traitement: models.Traitement, score_conformite, score_risque) -> dict:
    return {
        "organisation_nom": traitement.organisation.nom,
        "traitement_nom": traitement.nom,
        "service_responsable": traitement.service_responsable or "—",
        "finalite": traitement.finalite or "—",
        "base_legale": traitement.base_legale or "—",
        "statut": traitement.statut.value,
        "categories_donnees": [
            {
                "categorie": c.categorie,
                "sensibilite_label": "Sensible" if c.sensible else "Non sensible",
            }
            for c in traitement.categories_donnees
        ],
        "score_conformite": score_conformite.score_global if score_conformite else "non calculé",
        "score_risque": score_risque.score_global if score_risque else "non calculé",
        "niveau_risque": score_risque.niveau if score_risque else "—",
        "date_generation": datetime.now().strftime("%d/%m/%Y"),
    }


TEMPLATES = {
    "fiche_synthese": ("fiche_synthese_v1.docx", "v1", build_context_fiche_synthese),
}


class DocumentGenerationError(Exception):
    pass


def generer_document(traitement: models.Traitement, type_document: str,
                      score_conformite=None, score_risque=None) -> dict:
    if type_document not in TEMPLATES:
        raise DocumentGenerationError(
            f"Type de document inconnu : {type_document}. Disponibles : {list(TEMPLATES.keys())}"
        )

    nom_template, version, context_builder = TEMPLATES[type_document]
    chemin_template = TEMPLATES_DIR / nom_template
    if not chemin_template.exists():
        raise DocumentGenerationError(f"Template introuvable : {chemin_template}")

    context = context_builder(traitement, score_conformite, score_risque)

    doc = DocxTemplate(str(chemin_template))
    doc.render(context)

    horodatage = datetime.now().strftime("%Y%m%d%H%M%S")
    nom_fichier = f"{type_document}_{traitement.id}_{horodatage}.docx"
    chemin_sortie = DOCUMENTS_DIR / nom_fichier
    doc.save(str(chemin_sortie))

    hash_integrite = hashlib.sha256(chemin_sortie.read_bytes()).hexdigest()

    return {
        "chemin_fichier": str(chemin_sortie),
        "nom_fichier": nom_fichier,
        "hash_integrite": hash_integrite,
        "template_version": version,
    }
