from typing import Protocol, List
from data_product_1.domain.models import CreditApplicationModel, FolderNamesModel
from data_product_1.domain.result import Result, Err, Ok

class CreateFolderPort(Protocol):
    def create(
            self,
            model: FolderNamesModel
    ) -> Result[None, Exception]: 
        ...


