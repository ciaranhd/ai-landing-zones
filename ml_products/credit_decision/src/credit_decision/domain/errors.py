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