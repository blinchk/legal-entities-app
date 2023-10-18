from sqlalchemy import insert
from sqlalchemy.orm import Session

from db.database import engine
from models.legal_entity import LegalEntityInDB
from models.private_entity import PrivateEntityInDB
from models.share.legal_entity_share import LegalEntityShareInDB
from models.share.private_entity_share import PrivateEntityShareInDB


# Genereeritud väärtused
def insert_private_entities(session: Session):
    statement = insert(PrivateEntityInDB).values(
        [
            {"name": "Nikolas Laus", "personal_code": "50309030254"},
            {"name": "Priit Smirnov", "personal_code": "39811175703"},
            {"name": "Igor Saar", "personal_code": "38102210280"},
            {"name": "Malle Põder", "personal_code": "48703235716"},
            {"name": "Dmitri Sokolov", "personal_code": "36103044713"}
        ]
    )
    session.execute(statement)


def insert_legal_entities(session: Session):
    statement = insert(LegalEntityInDB).values(
        [
            {"name": "Swedbank", "registry_code": "1006071", "capital": 85000000, "created": "1996-07-11"},
            {"name": "Realnowaynetwork", "registry_code": "1032345", "capital": 2500, "created": "2022-01-03"},
            {"name": "Rahaprinter", "registry_code": "7772345", "capital": 2500, "created": "2019-10-15"},
            {"name": "Progemisbüroo", "registry_code": "3401433", "capital": 3500, "created": "2021-01-03"},
            {"name": "IT mehed", "registry_code": "1481644", "capital": 4777, "created": "2011-01-03"}
        ]
    )
    session.execute(statement)


def insert_legal_entity_shares(session: Session):
    statement = insert(LegalEntityShareInDB).values(
        [
            {"owned_legal_entity_id": 3, "is_founder": True, "owner_legal_entity_id": 1, "share": 2500},
            {"owned_legal_entity_id": 4, "is_founder": True, "owner_legal_entity_id": 1, "share": 1000},
            {"owned_legal_entity_id": 2, "is_founder": True, "owner_legal_entity_id": 4, "share": 2500},
            {"owned_legal_entity_id": 5, "is_founder": True, "owner_legal_entity_id": 4, "share": 4777}
        ]
    )
    session.execute(statement)


def insert_private_entity_shares(session: Session):
    statement = insert(PrivateEntityShareInDB).values(
        [
            {"owned_legal_entity_id": 4, "is_founder": True, "owner_private_entity_id": 1, "share": 2500},
            {"owned_legal_entity_id": 1, "is_founder": True, "owner_private_entity_id": 3, "share": 85000000},
        ]
    )
    session.execute(statement)


def insert_initial_data():
    with Session(engine) as session:
        insert_private_entities(session)
        insert_legal_entities(session)
        insert_legal_entity_shares(session)
        insert_private_entity_shares(session)
        session.commit()
