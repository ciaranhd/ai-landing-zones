from typing import List
from .ports import ModelTrainerPort
from .models import CreditApplication
from .ports import ModelFn
from .errors import Result, Err, Ok, InsufficientTrainingDataError, EmptyTrainingDataSetError

def train_model(
        train: ModelTrainerPort,
        data: List[CreditApplication]
) -> ModelFn:
    '''
    Business logic
    '''

    if not data:
        return Err(Result(EmptyTrainingDataSetError))
    if len(data) < 10:
        return Err(Result(InsufficientTrainingDataError))
    
    model_fn = Ok(train(data))

    return model_fn