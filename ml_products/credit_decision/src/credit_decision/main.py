from .adaptors.ml_model.sk_forest.sk_forest import ScikitRandomForestAdaptor
from .domain.services import create_decisioning_model
from .domain.models import CreditApplication
from typing import List

def main() -> None:
    data = CreditApplication(
        application_id=123,
        income=100.00,
        debt=50.00,
        employment_years=2
    )

    adaptor = ScikitRandomForestAdaptor()
    result = create_decisioning_model(
        port=adaptor,
        data=List[data]
    )