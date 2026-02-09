import numpy as np
from sklearn.ensemble import RandomForestClassifier
from typing import List
from credit_decision.domain.models import CreditApplication, RiskAssessment, ModelArtefacts, DatasetStats, TrainingMetrics
from credit_decision.domain.ports import predict_fn 
from credit_decision.adaptors.ml_model.sk_forest.config import RandomForestConfig
from credit_decision.domain.result import Result, Ok, Err
from credit_decision.domain.errors import TrainingDataLabelError
import mlflow

class ModelTrainingAdaptorRandomForest: 
    def __init__(self) -> None:
        self.config = RandomForestConfig(n_estimators=100, max_depth=5, threshold=0.4)

    def create(self, data: List[CreditApplication]) -> Result[(predict_fn, ModelArtefacts), Exception]:
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

        if len(set(labels)) < 2:
            return Err(TrainingDataLabelError)

        clf = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            max_depth=self.config.max_depth
        )

        clf.fit(
            features, labels
        )

        model_artefacts = ModelArtefacts(
                dataset_stats=DatasetStats(
                    sample_count=len(data),
                    positive_rate=float(labels.mean())
                ),
                config=self.config,
                ml_model=clf,
                metrics=TrainingMetrics(
                    positive_class_probability_mean=float(labels.mean())
                )
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
        
        return Ok((predict, model_artefacts))
            


class ModelLoggingAdaptorMLFlowLocal:
    def create(
        self,
        model_artefacts: ModelArtefacts
    ) -> None:
        mlflow.log_params(vars(model_artefacts.dataset_stats.sample_count))
        mlflow.log_metric("samples", model_artefacts.dataset_stats.sample_count)
        mlflow.log_metric("postitive_rate", model_artefacts.dataset_stats.positive_rate)
        mlflow.log_metric("positive_class_probability_mean", model_artefacts.metrics.positive_class_probability_mean)

        mlflow.sklearn.log_model(model_artefacts.ml_model, artifact_path="model")

        return Ok("Success: Logging")