from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

from models.share.share import ShareBase, Share
from models.private_entity import PrivateEntity


class PrivateEntityShareInDB(ShareBase):
    __tablename__ = "private_entity_share"

    owner_private_entity_id = mapped_column(ForeignKey("legal_entity.id"))


class PrivateEntityShare(Share):
    owned_private_entity: PrivateEntity
