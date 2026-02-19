class TrainingError(Exception):
    '''Base class for training related domain errors'''

class InsufficientTrainingDataError(TrainingError):
    minimum_required: int
    actual: int

    def __str__(self) -> str:
        return (
            "Insufficient data: required at least"
            f"{self.minimum_required}, got {self.actual}"
        )
    
class EmptyTrainingDataSetError(TrainingError):
    def __str__(self) -> str:
        return (
            "Cannot train data with empty data set"
        )
    
class TrainingDataLabelError(TrainingError):
    def __str__(self) -> str:
        return (
            "Only one label class present in the training data"
        )
    
class ModelLoggingError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)