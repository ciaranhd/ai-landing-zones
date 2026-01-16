from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes.models import SearchIndex

def create_index(
    endpoint: str,
    api_key: str,
    index: SearchIndex,
) -> None:
    client = SearchIndexClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(api_key),
    )

    client.create_or_update_index(index)
