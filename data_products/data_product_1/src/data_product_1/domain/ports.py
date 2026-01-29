from typing import Protocol, List
from data_product_1.domain.models import CreditApplicationModel, FolderNamesModel
from data_product_1.domain.result import Result

class CreateFolderPort(Protocol):
    def create_folders(
            folder_names: FolderNamesModel
    ) -> Result[None, Exception]: 
        ...

class WriteTablePort(Protocol):
    def write_table(
        catalog: str,
        schema: str, 
        table: str,
        records: List[CreditApplicationModel],
        mode: str = 'overwrite'
        ) -> Result[None, Exception]:
        ...

class DataSourcePort(Protocol):
    def load_raw_credit_applications(
    ) -> Result[List[CreditApplicationModel], Exception]:
        ...