
import os 
import ipdb
from data_product_1.domain.result import Ok, Err, Result 
from data_product_1.domain.models import FolderNamesModel
from data_product_1.adaptors.common import get_spark


class CreateFolderDatabricksAdapter:
    def create(
            self,
            folder_names: FolderNamesModel,
        ) -> Result[None, Exception]:

        result = get_spark(
            app_name='data-product',
        )

        if not isinstance(result, Ok):
            return Err(result.error)

        result.value.sql(
            f"CREATE VOLUME IF NOT EXISTS `{folder_names.root_folder_name}`."
            f"`{folder_names.sub_folder_raw_name}`."
            f"`{folder_names.sub_folder_raw_name}`"  
        )
        return Ok(None)
    
class CreateFolderLocalAdaptor:
    def create(
            self
    ):
        ipdb.set_trace()
        
        environment = 'dev'
        
        root_folder_name=f'{environment}_risk',
        sub_folder_raw_name='1_raw',
        sub_folder_curated_name='2_curated',
        sub_folder_published_name='3_published'

        os.makedirs("data", exist_ok=True)
        os.makedirs('data/{root_folder_name}', exist_ok=True)
        os.makedirs("data/{root_folder_name}/{sub_folder_raw_name}", exist_ok=True)
        
    


class CreateFolderSnowflake:
    pass


