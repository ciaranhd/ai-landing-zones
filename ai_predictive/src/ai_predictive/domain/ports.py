from typing import Protocol, List, Callable
from .models import CreditApplication, RiskAssessment

import pandas as pd


# The Model is treated as a functoin
ModelFn = Callable[[ CreditApplication ], RiskAssessment]


class ModelTrainerPort(Protocol):
    def train(self, data: List[CreditApplication]) -> ModelFn:
        '''
        The technical implementation of how we get the function
        '''
        ...