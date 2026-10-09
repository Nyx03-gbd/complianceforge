from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.apdp_generator import render_apdp_pdf
from app.services.apdp_form_schema_builder import build_form_schema
from app.services.apdp_overlay_builder_generic import build_apdp_overlays
from app.services.apdp_global_engine import resolve_document_data
from app.apdp_form_mapping import FORMULAIRE_UNIQUE_MAPPING
from app.apdp_annexe1_mapping import ANNEXE_1_SOUS_TRAITANCE_MAPPING
from app.apdp_annexe2_mapping import ANNEXE_2_COMMUNICATION_MAPPING
from app.apdp_annexe3_mapping import ANNEXE_3_INTERCONNEXION_MAPPING
from app.apdp_annexe4_mapping import APDP_ANNEXE4_MAPPING
from app.apdp_capteurs_mapping import APDP_CAPTEURS_MAPPING
from app.apdp_site_web_mapping import APDP_SITE_WEB_MAPPING
from app.apdp_engagement_conformite_mapping import APDP_ENGAGEMENT_CONFORMITE_MAPPING

router = APIRouter(
    prefix="/apdp",
    tags=["APDP génération"],
)


class APDPOverlay(BaseModel):
    type: str = "text"

    x: float
    y: float
    width: float
    height: float

    value: str | None = None
    checked: bool = False

    font_name: str | None = None
    font_size: float | None = None
    leading: float | None = None

    clear_before: bool = False
    clear_zones: list[dict[str, Any]] = Field(default_factory=list)


class APDPGenerationRequest(BaseModel):
    document_id: str
    output_name: str
    data: dict[str, Any] | None = None
    dossier: dict[str, Any] | None = None
    page_overlays: dict[int, list[APDPOverlay]] | None = None


@router.get("/formulaires/{document_id}/schema")
def get_formulaire_schema(document_id: str):

    mappings = {
        "formulaire_unique": FORMULAIRE_UNIQUE_MAPPING,
        "annexe_1_sous_traitance": ANNEXE_1_SOUS_TRAITANCE_MAPPING,
        "annexe_2_communication": ANNEXE_2_COMMUNICATION_MAPPING,
        "annexe_3_interconnexion": ANNEXE_3_INTERCONNEXION_MAPPING,
        "annexe_4_transfert": APDP_ANNEXE4_MAPPING,
        "formulaire_capteurs": APDP_CAPTEURS_MAPPING,
        "formulaire_site_web": APDP_SITE_WEB_MAPPING,
        "engagement_conformite": APDP_ENGAGEMENT_CONFORMITE_MAPPING,
    }

    if document_id not in mappings:
        raise HTTPException(
            status_code=404,
            detail=f"Formulaire inconnu : {document_id}",
        )

    return build_form_schema(mappings[document_id])

@router.post("/generer")
def generer_formulaire_apdp(
    payload: APDPGenerationRequest,
):
    """
    Génère un formulaire APDP par superposition
    sur le PDF officiel.

    Le PDF source APDP n'est jamais modifié.
    """

    if not payload.output_name.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=422,
            detail="Le nom du fichier doit se terminer par .pdf",
        )

    if payload.data is not None:
        try:
            data = resolve_document_data(
                document_id=payload.document_id,
                dossier=payload.dossier or {},
                specific_data=payload.data or {},
            )

            overlays = build_apdp_overlays(
                document_id=payload.document_id,
                data=data,
            )
        except ValueError as exc:
            raise HTTPException(
                status_code=422,
                detail=str(exc),
            )
    elif payload.page_overlays is not None:
        overlays = {
            int(page): [
                zone.model_dump(exclude_none=True)
                for zone in zones
            ]
            for page, zones in payload.page_overlays.items()
        }
    else:
        raise HTTPException(
            status_code=422,
            detail="Fournir soit 'data', soit 'page_overlays'.",
        )
    try:
        output_path, source_hash, output_hash = render_apdp_pdf(
            document_id=payload.document_id,
            page_overlays=overlays,
            output_name=payload.output_name,
        )

    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=422,
            detail=f"Paramètre de mapping invalide : {exc}",
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la génération du PDF APDP : {exc}",
        )

    return {
        "document_id": payload.document_id,
        "nom_fichier": output_path.name,
        "chemin_fichier": str(output_path),
        "source_hash": source_hash,
        "output_hash": output_hash,
        "official_source_preserved": True,
    }
