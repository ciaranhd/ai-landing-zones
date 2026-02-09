import numpy as np
from sklearn.ensemble import RandomForestClassifier
from typing import List
from credit_decision.domain.models import CreditApplication, RiskAssessment
from credit_decision.domain.ports import ModelFn 
from .config import RandomForestConfig

class ModelTrainingAdaptorRandomForest: 
    def __init__(self) -> None:
        self.config = RandomForestConfig(n_estimators=100, max_depth=5, threshold=0.4)

    def create(self, data: List[CreditApplication]) -> ModelFn:
        # 1. Transform domain objects to technical inputs 
        # This keeps the domain free of 'import numpy' etc
        features = np.array(
            [
                [app.income, app.debt, app.employment_years] for app in data
            ]
        )

        labels = np.array(
            [
                1 if (app.debt / app.income ) > 0.4 else 0 for app in data
            ]
        )

        clf = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            max_depth=self.config.max_depth
        )

        clf.fit(
            features, labels
        )

        def model_fn(
                app: CreditApplication) -> RiskAssessment:
            
            X_test = np.array(
                [
                    [app.income, app.debt, app.employment_years]
                ]
            )

            prob = float(
                clf.predict_proba(X_test)[0][1]
            )

            return RiskAssessment(
                score=prob,
                is_high_risk=prob > 0.5
            )
        
        return model_fn
            

