from typing import Protocol, List, Callable
from .models import CreditApplication, RiskAssessment

# The Model is treated as a functoin
ModelFn = Callable[[ CreditApplication ], RiskAssessment]

class ModelTrainingPort(Protocol):
    def create(
            self, 
            data: List[CreditApplication]
    ) -> ModelFn:
        '''
        Model Training Port for training decisioning models
        '''

        ...
