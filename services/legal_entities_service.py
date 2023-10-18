import datetime

from error.not_found_error import NotFoundError
from models.legal_entity import LegalEntityInDB, ShortLegalEntity, LegalEntity
from models.share.share import Share
from repositories import legal_entity_repository as repository
from repositories.share_repository import get_shareholders, create_share
from schemas.legal_entity_create import LegalEntityCreate
from utils import legal_entities_utils as utils


def search(term: str):
    return map(to_short_legal_entity_model, repository.search(term))


def create(schema: LegalEntityCreate):
    legal_entity_in_db = LegalEntityInDB(name=schema.name.strip() + " OÜ",
                                         capital=schema.capital,
                                         created=datetime.date.today(),
                                         registry_code=generate_registry_code())
    schema.validate_capital()
    result = repository.create(legal_entity_in_db)
    for shareholder in schema.shareholders:
        create_share(
            Share(
                id=None,
                owned_legal_entity_id=result.id,
                is_founder=True,
                share=shareholder.share
            ),
            shareholder.type,
            shareholder.id
        )
    return to_legal_entity_model(result)


def find_by_id(legal_entity_id: int):
    result = repository.find_by_id(legal_entity_id)
    if result is None:
        raise NotFoundError("Legal entity not found")
    return to_legal_entity_model(result)


def to_short_legal_entity_model(row: LegalEntityInDB) -> ShortLegalEntity:
    return ShortLegalEntity(
        id=row.id,
        name=row.name,
        registry_code=row.registry_code,
        capital=row.capital,
        created=row.created
    )


def to_legal_entity_model(row: LegalEntityInDB):
    return LegalEntity(
        id=row.id,
        name=row.name,
        registry_code=row.registry_code,
        capital=row.capital,
        created=row.created,
        shareholders=get_shareholders(row.id)
    )


def exists_by_registry_code(registry_code: str):
    return repository.exists_by_registry_code(registry_code)


def generate_registry_code():
    while True:
        registry_code = utils.generate_registry_code()
        if exists_by_registry_code(registry_code):
            continue
        return registry_code


def exists_by_name(name: str):
    return repository.exists_by_name(name)
