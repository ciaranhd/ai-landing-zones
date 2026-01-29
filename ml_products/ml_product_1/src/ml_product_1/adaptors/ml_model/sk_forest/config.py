from dataclasses import dataclass 

@dataclass(frozen=True)
class RandomForestConfig:
    n_estimators: int 
    max_depth: int 
    threshold: float 