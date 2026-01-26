from typing import List
from .ports import ModelTrainerPort
from .models import CreditApplication
from .ports import ModelFn


def train_credit_risk_model(
        train: ModelTrainerPort,
        data: List[CreditApplication]
) -> ModelFn:
    '''
    Business logic
    '''

    if not data:
        raise ValueError('Cannot train risk model with empty data set')
    if len(data) < 10:
        raise ValueError('Insufficient Data: Must have more than 10 records')
    
    model_fn = train(data)

    return model_fn