from data_product_1.domain.services import create_folders_service

from data_product_1.domain.models import FolderNamesModel
from data_product_1.adaptors.adaptors import CreateFolderDatabricksAdapter, CreateFolderLocalAdapter
from data_product_1.domain.result import Err, Ok, Result


def main(environment): 

    #Service 
    result = create_folders_service(
        folder_names=FolderNamesModel,
        port=CreateFolderDatabricksAdapter,
        environment=environment
    )
    



    
    