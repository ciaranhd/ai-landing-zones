from dataclasses import dataclass
from typing import Sequence, Literal

FieldType = Literal["Edm.String", "Edm.Int32", "Edm.Boolean"]

@dataclass(frozen=True)
class SearchFieldDef:
    name: str
    type: FieldType
    searchable: bool = False
    filterable: bool = False
    sortable: bool = False
    facetable: bool = False
    key: bool = False


@dataclass(frozen=True)
class SearchIndexDef:
    name: str
    fields: Sequence[SearchFieldDef]
