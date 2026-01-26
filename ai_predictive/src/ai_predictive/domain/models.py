from dataclasses import dataclass 
from .errors import Result, Ok, Err

@dataclass(frozen=True)
class CreditApplication:
    application_id: str
    income: float
    debt: float
    employment_years: int 

    
    @classmethod
    def create(
        cls,
        application_id,
        income, 
        debt, 
        employment_years
     ) -> Result["CreditApplication", Exception]:
        
        if not isinstance(application_id, str):
            return Err(TypeError("application_id must be of type str"))
        if not isinstance(income, float):
            return Err(TypeError("income must be of type float"))
        if not isinstance(debt, float):
            return Err(TypeError("debt must be of type of float"))
        if not isinstance(employment_years, int):
            return Err(TypeError("employment_years must be of type int"))
        
        return Ok(cls(application_id, income, debt, employment_years))
        
    


@dataclass(frozen=True)
class RiskAssessment:
    score: float 
    is_high_risk: bool 

    @classmethod
    def create(
        cls,
        score, 
        is_high_risk
    ) -> Result["RiskAssessment", Exception]:
        
        if not isinstance(score, float): 
            return Err(ValueError("sore must be of type float"))
        if not isinstance(is_high_risk, bool):
            return Err(ValueError("is_high_risk must be of type bool"))