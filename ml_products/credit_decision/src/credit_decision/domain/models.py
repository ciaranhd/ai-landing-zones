from dataclasses import dataclass 

@dataclass(frozen=True)
class CreditApplication:
    application_id: int
    income: float
    debt: float
    employment_years: int 


@dataclass(frozen=True)
class RiskAssessment:
    score: float 
    is_high_risk: bool 