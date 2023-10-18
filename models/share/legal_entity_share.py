from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from models.share.share import ShareBase, Share
from models.legal_entity import ShortLegalEntity


class LegalEntityShareInDB(ShareBase):
    __tablename__ = "legal_entity_share"

    owner_legal_entity_id = mapped_column(ForeignKey("legal_entity.id"))


class LegalEntityShare(Share):
    owner_legal_entity: ShortLegalEntity
