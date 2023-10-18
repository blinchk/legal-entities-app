from sqlalchemy import text, column, Integer, String, Boolean
from sqlalchemy.orm import Session

from db.database import engine
from models.legal_entity import LegalEntityInDB
from models.share.legal_entity_share import LegalEntityShareInDB
from models.share.private_entity_share import PrivateEntityShareInDB
from models.share.share import Share


def get_shareholders(legal_entity_id: int):
    with Session(engine) as session:
        statement = text("""
        select 
            les.owned_legal_entity_id as id,
            'LEGAL_ENTITY' as type,
            le.name as name,
            le.registry_code as code,
            les.is_founder as is_founder,
            les.share as share
        from legal_entity_share les
            join legal_entity le on les.owned_legal_entity_id = le.id
        where les.owned_legal_entity_id = :legal_entity_id
        union 
        select
            pes.owner_private_entity_id as id,
            'PRIVATE_ENTITY' as type,
            pe.name as name,
            pe.personal_code as code,
            pes.is_founder as is_founder,
            pes.share as share
        from private_entity_share pes
            join private_entity pe on pes.owner_private_entity_id = pe.id
        where pes.owned_legal_entity_id = :legal_entity_id
        """).bindparams(legal_entity_id=legal_entity_id).columns(
            column('id', Integer),
            column('type', String),
            column('name', String),
            column('code', String),
            column('is_founder', Boolean),
            column('share', Integer)
        )
        return session.execute(statement).mappings()


def search_shareholder(term: str):
    with Session(engine) as session:
        statement = text("""
            select
                le.id as id,
                'LEGAL_ENTITY' as type,
                le.name as name,
                le.registry_code as code
            from legal_entity le
            where 
                le.name ilike concat('%', :term, '%')
                or le.registry_code = :term
            union 
            select
                pe.id as id,
                'PRIVATE_ENTITY' as type,
                pe.name as name,
                pe.personal_code as code
            from private_entity pe
            where 
                pe.name ilike concat('%', :term, '%')
                or pe.personal_code = :term
        """).bindparams(term=term).columns(
            column('id', Integer),
            column('type', String),
            column('name', String),
            column('code', String)
        )
        return session.execute(statement).mappings()


def create_share(share: Share, _type: str, owner_id: int):
    with Session(engine) as session:
        if _type == 'LEGAL_ENTITY':
            session.add(LegalEntityShareInDB(
                    owner_legal_entity_id=owner_id,
                    owned_legal_entity_id=share.owned_legal_entity_id,
                    is_founder=share.is_founder,
                    share=share.share
                ))
            session.commit()
        elif _type == 'PRIVATE_ENTITY':
            session.add(PrivateEntityShareInDB(
                    owner_private_entity_id=owner_id,
                    owned_legal_entity_id=share.owned_legal_entity_id,
                    is_founder=share.is_founder,
                    share=share.share
            ))
            session.commit()
