from azure.search.documents.indexes.models import SearchIndex, SearchField
from .models import SearchIndexDef, SearchFieldDef

def build_search_field(field: SearchFieldDef) -> SearchField:
    return SearchField(
        name=field.name,
        type=field.type,
        key=field.key,
        searchable=field.searchable,
        filterable=field.filterable,
        sortable=field.sortable,
        facetable=field.facetable,
    )


def build_search_index(definition: SearchIndexDef) -> SearchIndex:
    return SearchIndex(
        name=definition.name,
        fields=[build_search_field(f) for f in definition.fields],
    )
