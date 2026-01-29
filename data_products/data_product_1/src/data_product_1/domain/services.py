from data_product_1.domain.ports import CreateFolderPort
from data_product_1.domain.models import FolderNamesModel
from data_product_1.domain.result import Ok, Err, Result 



def create_folders_service(
        folder_names: FolderNamesModel,
        port: CreateFolderPort,
        environment: str,  
    ) -> Result[None, Exception]:

    '''
    Notes: Service is the Business Logic. 
    NEVER import from adaptors (strictly no coupling). Only import from domain. 
    
    :param folder_names: Description
    :type folder_names: FolderNamesModel
    :param port: Description
    :type port: CreateFolderPort
    :param environment: Description
    :type environment: str
    :return: Description
    :rtype: Result[Ok[None], Exception]
    '''
    
    #Model
    folder_result = folder_names.create(
        root_folder_name=f'{environment}_risk',
        sub_folder_raw_name='1_raw',
        sub_folder_curated_name='2_curated',
        sub_folder_published_name='3_published'  
    )

    if not isinstance(folder_result, Ok):
        return Err(folder_result.error)  # propagate the original error
    
    #Port/Adaptor
    result = port.create_folders(
        folder_names = result.value
    )

    if not isinstance(result, Ok):
        return Err(TypeError('fix'))
    
    return Ok(None)

    

    
    
    
