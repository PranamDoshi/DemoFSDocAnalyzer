from typing import List, Optional
import logging
from fastapi import Depends, APIRouter, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.api.deps import get_db
from app.api import crud
from app import schema

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
async def get_documents(
    document_ids: Optional[List[UUID]] = Query(None),
    db: AsyncSession = Depends(get_db),
) -> List[schema.Document]:
    """
    Get all documents or documents by their ids
    """
    if document_ids is None:
        # If no ids provided, fetch all documents
        docs = await crud.fetch_documents(db)
    else:
        # If ids are provided, fetch documents by ids
        docs = await crud.fetch_documents(db, ids=document_ids)

    if len(docs) == 0:
        raise HTTPException(status_code=404, detail="Document(s) not found")

    return docs


@router.get("/{document_id}")
async def get_document(
    document_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> schema.Document:
    """
    Get all documents
    """
    docs = await crud.fetch_documents(db, id=document_id)
    if len(docs) == 0:
        raise HTTPException(status_code=404, detail="Document not found")

    return docs[0]

# @router.delete("/{document_id}")
# async def delete_document(
#     document_id: UUID,
#     db: AsyncSession = Depends(get_db)
# ) -> None:
#     """
#     Delete a document.
#     """
#     deleted = await crud.delete_document(db, document_id)
#     return deleted

@router.delete("/delete_all_documents")
async def delete_all_documents_api(db: AsyncSession = Depends(get_db))-> None:
    """ Deletes all documents """
    deleted_docs_count = await crud.delete_all_documents(db)
    return deleted_docs_count
