from typing import List

from fastapi import APIRouter

from models.legal_entity import ShortLegalEntity
from models.share.search.shareholder_search_result import ShareholderSearchResult
from services import legal_entities_service as service
from services import shares_service as shares_service
from schemas.legal_entity_create import LegalEntityCreate
from utils import legal_entities_utils

router = APIRouter(
    prefix="/legal-entity"
)


@router.get("/search", tags=["legal-entities"], response_model=List[ShortLegalEntity])
def search_legal_entities(
        term: str
):
    return service.search(term)


@router.get("/registry-code", tags=["legal-entities"])
def generate_registry_code():
    return legal_entities_utils.generate_registry_code()


@router.get("/name/{name}", tags=["legal-entities"])
def check_name_is_available(name: str):
    return service.exists_by_name(name) is False


@router.get("/new/shareholder/search", tags=["legal-entities"], response_model=List[ShareholderSearchResult])
def search_shareholder(term: str):
    return shares_service.search_shareholder(term)


@router.get("/{id}", tags=["legal-entities"])
def get_legal_entity(
        id: int
):
    return service.find_by_id(id)


@router.post("/", tags=["legal-entities"], response_model=ShortLegalEntity)
def create_legal_entity(
        schema: LegalEntityCreate
):
    return service.create(schema)
