from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.documents import generer_document, DocumentGenerationError, TEMPLATES

router = APIRouter(tags=["documents"])


def _get_traitement_ou_404(traitement_id: str, db: Session) -> models.Traitement:
    traitement = db.get(models.Traitement, traitement_id)
    if not traitement:
        raise HTTPException(status_code=404, detail="Traitement introuvable")
    return traitement


@router.post("/traitements/{traitement_id}/documents/generer", response_model=schemas.DocumentGenereOut)
def generer(traitement_id: str, type_document: str, db: Session = Depends(get_db)):
    traitement = _get_traitement_ou_404(traitement_id, db)

    if type_document not in TEMPLATES:
        raise HTTPException(status_code=422, detail=f"Type inconnu. Disponibles : {list(TEMPLATES.keys())}")

    score_conformite = (db.query(models.ScoreConformite)
        .filter(models.ScoreConformite.traitement_id == traitement_id)
        .order_by(models.ScoreConformite.date_calcul.desc()).first())
    score_risque = (db.query(models.ScoreRisque)
        .filter(models.ScoreRisque.traitement_id == traitement_id)
        .order_by(models.ScoreRisque.date_calcul.desc()).first())

    try:
        resultat = generer_document(traitement, type_document, score_conformite, score_risque)
    except DocumentGenerationError as e:
        raise HTTPException(status_code=500, detail=str(e))

    document = models.DocumentGenere(
        traitement_id=traitement.id,
        type_document=type_document,
        chemin_fichier=resultat["chemin_fichier"],
        nom_fichier=resultat["nom_fichier"],
        hash_integrite=resultat["hash_integrite"],
        template_version=resultat["template_version"],
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


@router.get("/traitements/{traitement_id}/documents", response_model=list[schemas.DocumentGenereOut])
def lister_documents(traitement_id: str, db: Session = Depends(get_db)):
    _get_traitement_ou_404(traitement_id, db)
    return (db.query(models.DocumentGenere)
            .filter(models.DocumentGenere.traitement_id == traitement_id)
            .order_by(models.DocumentGenere.date_generation.desc()).all())


@router.get("/documents/{document_id}/telecharger")
def telecharger_document(document_id: str, db: Session = Depends(get_db)):
    document = db.get(models.DocumentGenere, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document introuvable")
    return FileResponse(
        path=document.chemin_fichier,
        filename=document.nom_fichier,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
