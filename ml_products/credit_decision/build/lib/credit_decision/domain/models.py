from dataclasses import dataclass 
from credit_decision.adaptors.ml_model.sk_forest.config import RandomForestConfig
from sklearn.ensemble import RandomForestClassifier

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
    config: RandomForestConfig
    ml_model: RandomForestClassifier
