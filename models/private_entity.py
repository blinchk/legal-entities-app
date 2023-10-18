from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from db.base import Base


class PrivateEntityInDB(Base):
    __tablename__ = "private_entity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    personal_code = Column(String(11), nullable=False, index=True, unique=True)


class PrivateEntity(BaseModel):
    id: int
    name: str
    personal_code: str
