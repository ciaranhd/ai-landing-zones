from typing import List, Tuple
from credit_decision.domain.ports import ModelTrainingPort, ModelLoggingPort
from credit_decision.domain.models import CreditApplication, RiskAssessment, ModelArtefacts
from .ports import predict_fn
from .result import Result, Err, Ok
from .errors import InsufficientTrainingDataError, EmptyTrainingDataSetError

def create_decisioning_model(
        port: ModelTrainingPort,
        data: List[CreditApplication]
    )  -> Result[Tuple[predict_fn, ModelArtefacts], Exception]:
    '''
    Business logic
    '''

    if not data:
        return Err(EmptyTrainingDataSetError)
    if len(data) < 2:
        return Err(InsufficientTrainingDataError)
    
    result = port.create(
        data=data
    )

    if not isinstance(result, Ok):
        return result.error
    
    return Ok(result.value)

def logging_for_decisioning_model(
        port: ModelLoggingPort,
        model_artefacts: ModelArtefacts
):
    result = port.create(
        model_artefacts=model_artefacts
    )

    if not isinstance(result, Ok): 
        return Err("test")
    
    return Ok(result.value)



