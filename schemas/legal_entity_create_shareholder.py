from pydantic import BaseModel, field_validator

from repositories import private_entity_repository, legal_entity_repository


class LegalEntityCreateShareholder(BaseModel):
    id: int
    type: str
    share: int

    @field_validator('id')
    def check_id(cls, v: int):
        if v is None or v == 0:
            raise ValueError('ID must be not null')
        return v

    @field_validator('type')
    def check_type(cls, v: str):
        if v not in ['LEGAL_ENTITY', 'PRIVATE_ENTITY']:
            raise ValueError('Shareholder type must be LEGAL_ENTITY or PRIVATE_ENTITY')
        return v

    @field_validator('share')
    def check_share(cls, v: int):
        if v < 1:
            raise ValueError('Share must be at least 1 euro')
        return v
