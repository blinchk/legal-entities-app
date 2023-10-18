from pydantic import BaseModel


class ShareholderSearchResult(BaseModel):
    id: int
    type: str
    name: str
    code: str
