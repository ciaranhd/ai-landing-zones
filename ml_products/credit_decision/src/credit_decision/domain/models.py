from dataclasses import dataclass 
from typing import Any

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

@dataclass(frozen=True)
class DatasetStats:
    sample_count: int
    positive_rate: float

@dataclass(frozen=True)
class TrainingMetrics:
    positive_class_probability_mean: float

@dataclass
class ModelArtefacts:
    dataset_stats: DatasetStats
    metrics: TrainingMetrics
    config: Any
    ml_model: Any
