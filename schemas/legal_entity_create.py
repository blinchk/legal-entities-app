from typing import List

from pydantic import BaseModel, field_validator, Field

from schemas.legal_entity_create_shareholder import LegalEntityCreateShareholder


class LegalEntityCreate(BaseModel):
    name: str = None
    registry_code: str = Field(validation_alias="registryCode", min_length=7, max_length=7)
    capital: int = None
    shareholders: List[LegalEntityCreateShareholder]

    @field_validator('registry_code')
    def check_registry_code(cls, v: str):
        if len(v) != 7:
            raise ValueError('Registry code must contain 7 numbers')

    @field_validator('capital')
    def check_capital(cls, v: int):
        if v < 2500:
            raise ValueError('Capital should be at least 2500')
        return v

    @field_validator('name')
    def check_name_length(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError('Legal entity name must be longer than 3 characters')
        if len(v) > 100:
            raise ValueError('Legal entity name must be shorter than 100 characters')
        return v

    @field_validator('name')
    def check_name_is_alphanumeric(cls, v: str) -> str:
        if isinstance(v, str):
            is_alphanumeric = v.replace(' ', '').isalnum()
            if not is_alphanumeric:
                raise ValueError('Legal entity name must be alphanumeric')
        return v

    @field_validator('capital')
    def check_required_capital(cls, v: int) -> int:
        if v < 2500:
            raise ValueError('Legal entity capital should be at least 2500 euros')
        return v

    def validate_capital(self):
        sum_of_shareholders_shares = sum([shareholder.share for shareholder in self.shareholders])
        if sum_of_shareholders_shares != self.capital:
            raise ValueError('Shareholders share must be equal with capital')
