from typing import Protocol
from data_product_1.domain.models import FolderNamesModel
from data_product_1.domain.result import Result

class CreateFolderPort(Protocol):
    def create(
            self,
            model: FolderNamesModel
    ) -> Result[None, Exception]: 
        ...


