from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.scoring import calculer_score_conformite, calculer_score_risque, CriteresRisque

router = APIRouter(prefix="/traitements/{traitement_id}/scores", tags=["scores"])


def _get_traitement_ou_404(traitement_id: str, db: Session) -> models.Traitement:
    traitement = db.get(models.Traitement, traitement_id)
    if not traitement:
        raise HTTPException(status_code=404, detail="Traitement introuvable")
    return traitement


@router.post("/calculer", response_model=schemas.ScoresCalcules)
def calculer_scores(traitement_id: str, db: Session = Depends(get_db)):
    traitement = _get_traitement_ou_404(traitement_id, db)

    champs_manquants = [
        c for c in ("sensibilite_donnees", "niveau_mesures_securite",
                    "sous_traitance_transferts", "exposition", "volume")
        if getattr(traitement, c) is None
    ]
    if champs_manquants:
        raise HTTPException(
            status_code=422,
            detail=f"Critères de risque manquants : {champs_manquants}. "
                   f"Renseigne-les via PATCH /traitements/{{id}}.",
        )

    traitement_data = {
        "nom": traitement.nom,
        "service_responsable": traitement.service_responsable,
        "finalite": traitement.finalite,
        "base_legale": traitement.base_legale,
        "justification_base_legale": traitement.justification_base_legale,
        "categories_donnees": [c.categorie for c in traitement.categories_donnees],
    }
    resultat_conformite = calculer_score_conformite(traitement_data)

    score_conformite = models.ScoreConformite(
        traitement_id=traitement.id,
        score_global=resultat_conformite["score_global"],
        version_grille=resultat_conformite["version_grille"],
        details=resultat_conformite["details"],
    )
    db.add(score_conformite)

    criteres = CriteresRisque(
        sensibilite_donnees=traitement.sensibilite_donnees,
        niveau_mesures_securite=traitement.niveau_mesures_securite,
        sous_traitance_transferts=traitement.sous_traitance_transferts,
        exposition=traitement.exposition,
        volume=traitement.volume,
        score_conformite=resultat_conformite["score_global"],
    )
    resultat_risque = calculer_score_risque(criteres)

    score_risque = models.ScoreRisque(
        traitement_id=traitement.id,
        score_global=resultat_risque["score_global"],
        niveau=resultat_risque["niveau"],
        composantes=resultat_risque["composantes"],
    )
    db.add(score_risque)

    db.commit()
    db.refresh(score_conformite)
    db.refresh(score_risque)

    return schemas.ScoresCalcules(conformite=score_conformite, risque=score_risque)


@router.get("/conformite", response_model=list[schemas.ScoreConformiteOut])
def historique_conformite(traitement_id: str, db: Session = Depends(get_db)):
    _get_traitement_ou_404(traitement_id, db)
    return (db.query(models.ScoreConformite)
            .filter(models.ScoreConformite.traitement_id == traitement_id)
            .order_by(models.ScoreConformite.date_calcul.desc()).all())


@router.get("/risque", response_model=list[schemas.ScoreRisqueOut])
def historique_risque(traitement_id: str, db: Session = Depends(get_db)):
    _get_traitement_ou_404(traitement_id, db)
    return (db.query(models.ScoreRisque)
            .filter(models.ScoreRisque.traitement_id == traitement_id)
            .order_by(models.ScoreRisque.date_calcul.desc()).all())
