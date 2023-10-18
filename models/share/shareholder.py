from pydantic import BaseModel, Field


class Shareholder(BaseModel):
    id: int
    type: str
    name: str
    code: str
    is_founder: bool = Field(serialization_alias="founder")
    share: int
