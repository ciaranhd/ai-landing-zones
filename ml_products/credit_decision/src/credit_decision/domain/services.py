from typing import List, Tuple
from credit_decision.domain.ports import (
    ModelTrainingPort,
    ModelLoggingPort,
    predict_fn
    )
from credit_decision.domain.models import CreditApplication, ModelArtefacts
from credit_decision.domain.result import Result, Err, Ok
from credit_decision.domain.errors import InsufficientTrainingDataError, EmptyTrainingDataSetError

def create_decisioning_model(
        port: ModelTrainingPort,
        data: List[CreditApplication]
    )  -> Result[Tuple[predict_fn, ModelArtefacts], Exception]:
    '''
    Business logic
    '''

    if not data:
        return Err(EmptyTrainingDataSetError())
    if len(data) < 2:
        return Err(InsufficientTrainingDataError())
    
    result = port.create(
        data=data
    )

    if not isinstance(result, Ok):
        return Err(result.error)
    
    return Ok(result.value)

def logging_for_decisioning_model(
        port: ModelLoggingPort,
        model_artefacts: ModelArtefacts) -> Result[str, Exception]:
    result = port.create(
        model_artefacts=model_artefacts
    )

    if not isinstance(result, Ok): 
        return Err(Exception())
    
    return Ok(result.value)



