
from sqlalchemy.orm import Session

from db.database import engine
from models.private_entity import PrivateEntityInDB


def exists_by_id(private_entity_id: int):
    with Session(engine) as session:
        return session.query(PrivateEntityInDB).filter_by(id=private_entity_id).scalar() is not None
