from data_product_1.domain.result import Ok, Err, Result 
from pyspark.sql import SparkSession

# mypy: disable-error-code=misc

def get_spark(app_name: str = "data-product") -> Result[SparkSession, Exception]:
    """
    Returns a SparkSession that works in:
    - Databricks workspace
    - Local machine via Databricks Connect v2
    - Azure DevOps agent via Databricks Connect v2

    No environment branching required.
    """
    

    spark = (
        SparkSession.builder.appName(app_name).getOrCreate()
    ) 

    

    if not spark:
        return Err(ValueError(spark)) # Complete this
    return Ok(spark)
    