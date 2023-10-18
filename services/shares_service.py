from typing import List

from models.share.search.shareholder_search_result import ShareholderSearchResult
from repositories import share_repository as repository


def search_shareholder(term: str) -> List[ShareholderSearchResult]:
    result = repository.search_shareholder(term)
    return result

