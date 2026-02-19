from typing import Protocol, List, Callable, Tuple, runtime_checkable
from credit_decision.domain.models import (
    CreditApplication,
    RiskAssessment,
    ModelArtefacts
    )
from credit_decision.domain.result import Result

# The Model is treated as a functoin
predict_fn = Callable[[ CreditApplication ], RiskAssessment]

@runtime_checkable
class ModelTrainingPort(Protocol):
    def create(
            self, 
            data: List[CreditApplication]
    ) ->  Result[Tuple[predict_fn, ModelArtefacts], Exception]:
        '''
        Model Training Port for training decisioning models
        '''

        ...
@runtime_checkable
class ModelLoggingPort(Protocol):
    def create(
            self,
            model_artefacts: ModelArtefacts
    ) -> Result[str, Exception]:
        '''
        
        '''
        ...

