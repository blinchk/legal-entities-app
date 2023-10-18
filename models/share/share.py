from typing import Union

from pydantic import BaseModel
from sqlalchemy import Column, Boolean, Integer, ForeignKey
from sqlalchemy.orm import mapped_column

from db.base import Base


class ShareBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    owned_legal_entity_id = mapped_column(ForeignKey("legal_entity.id"))
    is_founder = Column(Boolean)
    share = Column(Integer)


class Share(BaseModel):
    id: Union[int, None]
    owned_legal_entity_id: int
    is_founder: bool
    share: int
