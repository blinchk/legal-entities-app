from typing import Type

from sqlalchemy import text
from sqlalchemy.orm import Session

from db.database import engine
from models.legal_entity import LegalEntityInDB


def search(term: str):
    with Session(engine) as session:
        statement = text("""
        select distinct
            le.id,
            le.name,
            le.registry_code,
            le.created,
            le.capital
        from legal_entity le
            left join legal_entity_share les on les.owned_legal_entity_id = le.id
            left join private_entity_share pes on pes.owned_legal_entity_id = le.id
            left join private_entity pe on pe.id = pes.owner_private_entity_id
        where
            le.name ilike concat('%', :term, '%')
            or le.registry_code = :term
            or pe.name = :term
            or pe.personal_code = :term
        """).bindparams(term=term)
        return session.execute(statement).mappings()


def create(legal_entity_in_db: LegalEntityInDB) -> LegalEntityInDB:
    with Session(engine) as session:
        session.add(legal_entity_in_db)
        session.commit()
        session.refresh(legal_entity_in_db)
        return legal_entity_in_db


def find_by_id(legal_entity_id: int) -> Type[LegalEntityInDB] | None:
    with Session(engine) as session:
        return session.query(LegalEntityInDB).filter_by(id=legal_entity_id).first()

def exists_by_id(legal_entity_id: int) -> bool:
    with Session(engine) as session:
        return session.query(LegalEntityInDB).filter_by(id=legal_entity_id).scalar() is not None


def exists_by_registry_code(registry_code: str) -> bool:
    with Session(engine) as session:
        return session.query(LegalEntityInDB).filter_by(registry_code=registry_code).scalar() is not None


def exists_by_name(name: str) -> bool:
    with Session(engine) as session:
        return session.query(LegalEntityInDB).filter_by(name=name).scalar() is not None
