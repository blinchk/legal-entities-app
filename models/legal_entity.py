from datetime import date
from typing import List, Any

from pydantic import BaseModel, Field
from sqlalchemy import Integer, Column, String, Date

from db.base import Base
from models.share.shareholder import Shareholder


class LegalEntityInDB(Base):
    __tablename__ = "legal_entity"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, unique=True, nullable=False)
    registry_code = Column(String(7), nullable=False, name="registry_code", index=True, unique=True)
    created = Column(Date, nullable=False)
    capital = Column(Integer, nullable=False)


class ShortLegalEntity(BaseModel):
    id: int
    name: str
    registry_code: str = Field(serialization_alias="registryCode")
    created: date
    capital: int


class LegalEntity(ShortLegalEntity):
    def __init__(self, **data: Any):
        super().__init__(**data)

    shareholders: List[Shareholder]
