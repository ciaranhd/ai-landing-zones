from dataclasses import dataclass
from data_product_1.domain.result import Result, Err, Ok 
from data_product_1.domain.models import SubFolderNamesModel


def folder_names_cfg(
        ) -> Result[Ok[SubFolderNamesModel], Err]:
    
    result = SubFolderNamesModel.create(
                raw_folder_name='1_raw',
                curated_folder_name='2_curated',
                published_folder_name='3_published' 
                )
    return result
        