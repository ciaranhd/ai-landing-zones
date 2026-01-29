from data_product_1.domain.ports import CreateFolderPort
from data_product_1.domain.result import Ok, Err, Result
from data_product_1.domain.models import FolderNamesModel



def create_folders_service(
     create_folders: CreateFolderPort,
     folder_names: FolderNamesModel
) -> Result[None, Exception]:
    
    result = create_folders(folder_names)

    if not isinstance(result, Ok):
        raise KeyError # Complete

    

    
    
    
