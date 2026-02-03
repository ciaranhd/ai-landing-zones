# Databricks Notebook Source

from data_product_1.domain.services import create_folders_service
from data_product_1.adaptors.adaptors import  CreateFolderDatabricksAdapter
from data_product_1.domain.result import Ok

# ------------

# ------------
def main(environment: str) -> None: 
    '''
    Composition Root
    Notes: Only pass in objects. There is to be no business logic
    '''
    adaptor = CreateFolderDatabricksAdapter()
    #Service 
    result = create_folders_service(
        port=adaptor,
        environment=environment,
        )

    if isinstance(result, Ok):
        print(result.value)


    
    



    
    