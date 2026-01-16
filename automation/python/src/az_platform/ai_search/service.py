from .models import SearchIndexDef
from .builders import build_search_index
from .client import create_index

def provision_index(
    endpoint: str,
    api_key: str,
    definition: SearchIndexDef,
) -> None:
    index = build_search_index(definition)
    create_index(endpoint, api_key, index)
