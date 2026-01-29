from dataclasses import dataclass 
from data_product_1.domain.result import Result, Err, Ok 

@dataclass(frozen=True)
class CreditApplicationModel:
    application_id: str
    income: float
    debt: float
    employment_years: int 

    
    @classmethod
    def create(
        cls,
        application_id: str,
        income: float, 
        debt: float, 
        employment_years: int
     ) -> Result["CreditApplicationModel", Exception]:
        
        if not isinstance(application_id, str):
            return Err(TypeError("application_id must be of type str"))
        if not isinstance(income, float):
            return Err(TypeError("income must be of type float"))
        if not isinstance(debt, float):
            return Err(TypeError("debt must be of type of float"))
        if not isinstance(employment_years, int):
            return Err(TypeError("employment_years must be of type int"))
        
        return Ok(cls(
            application_id=application_id,
            income=income, debt=debt,
            employment_years=employment_years
            ))
        
    
@dataclass(frozen=True)
class FolderNamesModel:
    root_folder_name: str
    sub_folder_raw_name: str
    sub_folder_curated_name: str
    sub_folder_published_name: str

    @classmethod
    def create(
        cls,
        root_folder_name,
        sub_folder_raw_name,
        sub_folder_curated_name, 
        sub_folder_published_name
     ) -> Result[Ok["FolderNamesModel"], Exception]:
        
        if not isinstance(root_folder_name, str):
            return Err(TypeError("Root folder name must of type str"))
        if not isinstance(sub_folder_raw_name, str):
            return Err(TypeError("Sub folder name must be of type str"))
        if not isinstance(sub_folder_curated_name, str):
            return Err(TypeError("Sub folder name must be of type str"))
        if not isinstance(sub_folder_published_name, str):
            return Err(TypeError("Sub folder name must be of type of str"))

        return Ok(cls(root_folder_name, sub_folder_raw_name, sub_folder_curated_name, sub_folder_published_name))