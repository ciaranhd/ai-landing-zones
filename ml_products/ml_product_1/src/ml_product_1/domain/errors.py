from typing import Generic, TypeVar, Union

T = TypeVar("T")
E = TypeVar("E", bound=Exception)

class Ok(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value
    
    def ok(self) -> T:
        return self._value
    
class Err(Generic[E]):
    def __init__(self, e: E) -> None:
        self._e = e
    
    def err(self) -> E:
        return self._e 
    
Result = Union[ Ok[T], Err[E] ]

class TrainingError(Exception):
    '''Base class for training related domain errors'''

class InsufficientTrainingDataError(TrainingError):
    minimum_required: int
    actual: int

    def __str__(self) -> str:
        return (
            f"Insufficient data: required at least"
            f"{self.minimum_required}, got {self.actual}"
        )
    
class EmptyTrainingDataSetError(Exception):
    def __str__(self) -> str:
        return (
            f"Cannot train data with empty data set"
        )