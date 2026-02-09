from typing import List
from .ports import ModelTrainingPort
from .models import CreditApplication
from .ports import ModelFn
from .result import Result, Err, Ok
from .errors import InsufficientTrainingDataError, EmptyTrainingDataSetError

def create_decisioning_model(
        port: ModelTrainingPort,
        data: List[CreditApplication]
    )  -> Result[ModelFn, Exception]:
    '''
    Business logic
    '''

    if not data:
        return Err(EmptyTrainingDataSetError)
    if len(data) < 10:
        return Err(InsufficientTrainingDataError)
    
    model_fn = port.create(
        data=data
    )

    return Ok(model_fn)


