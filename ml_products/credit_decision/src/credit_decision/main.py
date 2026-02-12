from credit_decision.adaptors.ml_model.sk_forest.adaptors import (
    ModelTrainingAdaptorRandomForest, 
    ModelLoggingAdaptorMLFlowLocal
    )
from credit_decision.domain.services import (
    create_decisioning_model,
    logging_for_decisioning_model
    )
from credit_decision.domain.models import CreditApplication
from credit_decision.domain.result import Ok

def main() -> None:
    # Data ingestion is a toy use case. Production would ingest from spark dataframe or local data
    # Create a Service for data ingestion, with port + adaptors for local, and remote 
    # We want to be able to decouple from the data ingestion layer, and therefore swap it 
    # at will
    data_1 = CreditApplication(
        application_id=123,
        income=100.00,
        debt=50.00,
        employment_years=2
    )

    data_2 = CreditApplication(
        application_id=124,
        income=200.00,
        debt=10.00,
        employment_years=3
    )

    adaptor = ModelTrainingAdaptorRandomForest()
    result = create_decisioning_model(
        port=adaptor,
        data=[data_1, data_2]
    )

    if not isinstance(result, Ok):
        print("error") # fix

    predict_fn, model_artefacts = result.value

    result = logging_for_decisioning_model(
        port=ModelLoggingAdaptorMLFlowLocal,
        model_artefacts=model_artefacts
    )

    if not isinstance(result, Ok):
        raise result.error
