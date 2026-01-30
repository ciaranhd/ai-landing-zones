from data_product_1.domain.services import create_folders_service
from data_product_1.domain.models import FolderNamesModel
from data_product_1.adaptors.adaptors import CreateFolderDatabricksAdapter
from data_product_1.domain.result import Err, Ok, Result


def main(environment: str) -> None: 
    '''
    Composition Root
    Notes: Only pass in objects. There is to be no business logic
    '''
    adaptor = CreateFolderDatabricksAdapter()
    #Service 
    result = create_folders_service(
        port=adaptor,
        environment=environment
    )
    



    
    