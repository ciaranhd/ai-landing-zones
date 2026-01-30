from dataclasses import dataclass 
from data_product_1.domain.result import Result, Err, Ok 

@dataclass(frozen=True)
class CreditApplicationModel:
    application_id: str
    income: float
    debt: float
    employment_years: int 

    
@dataclass(frozen=True)
class FolderNamesModel:
    root_folder_name: str
    sub_folder_raw_name: str
    sub_folder_curated_name: str
    sub_folder_published_name: str