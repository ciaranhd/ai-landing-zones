from data_product_1.domain.services import create_folders_service
from data_product_1.domain.models import FolderNamesModel
from data_product_1.adaptors.adaptors import CreateFolderDatabricksAdapter
from data_product_1.domain.result import Err, Ok, Result


def main(environment) -> None: 
    '''
    Composition Root
    Notes: Only pass in objects. There is to be no business logic
    '''


    #adaptor/port
    adaptor_port = CreateFolderDatabricksAdapter()

    #Service 
    result = create_folders_service(
        folder_names=FolderNamesModel,
        port=adaptor_port,
        environment=environment
    )
    



    
    