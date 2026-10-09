from fastapi import APIRouter, HTTPException

from app.apdp_documents import get_document, list_documents

router = APIRouter(
    prefix="/documents-apdp",
    tags=["documents APDP"],
)


@router.get("")
def get_documents(category: str | None = None):
    return {
        "documents": list_documents(category)
    }


@router.get("/{document_id}")
def get_document_by_id(document_id: str):
    try:
        return get_document(document_id)
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"Document APDP inconnu : {document_id}",
        )
