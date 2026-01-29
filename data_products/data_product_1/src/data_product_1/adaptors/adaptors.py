from data_product_1.domain.result import Ok, Err, Result 
from data_product_1.domain.models import FolderNamesModel
from data_product_1.adaptors.common import get_spark


class CreateFolderDatabricksAdapter:
    def create_folders(
            folder_names: FolderNamesModel
        ) -> Result[Ok[None], Exception]:

        spark = get_spark()

        spark.sql(
            f"CREATE VOLUME IF NOT EXISTS `{folder_names.root_folder_name}`."
            f"`{folder_names.sub_folder_raw_name}`."
            f"`{folder_names.sub_folder_raw_name}`"  
        )

        return Ok(None)
    
class CreateFolderLocalAdapter:
    def create_folders(
            folder_names: FolderNamesModel
    ) -> Result[Ok[None], Exception]:
        pass


    
    
    


