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
    
class CreateFolderLocally:
    pass


class CreateFolderSnowflake:
    pass
    
    
    


