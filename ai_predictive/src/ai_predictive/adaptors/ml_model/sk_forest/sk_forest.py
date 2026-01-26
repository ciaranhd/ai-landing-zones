import numpy as np
from sklearn.ensemble import RandomForestClassifier
from typing import List
from ai_predictive.domain.models import CreditApplication
from ai_predictive.domain.models import CreditApplication, RiskAssessment
from ai_predictive.domain.ports import ModelFn 
from ai_predictive.adaptors.ml_model.sk_forest.config import RandomForestConfig

class ScikitRandomForestAdaptor: 
    def __init__(self):

        config = RandomForestConfig(n_estimators=100, max_depth=5, threshold=0.4)
        
        #Hyperparameters for the model are stored here, and hidden from the domain 
        self.n_estimators = config.n_estimators
        self.max_depth = config.max_depth

    def train(self, data: List[CreditApplication]) -> ModelFn:
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
            n_estimators=self.n_estimators,
            max_depth=self.max_depth
        )

        clf.fit(
            features, labels
        )

        def predict(
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
        
        return predict
            

