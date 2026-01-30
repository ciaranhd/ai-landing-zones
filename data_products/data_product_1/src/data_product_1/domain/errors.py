class MissingInputError(BaseException):
    ...

class NoCatalogNameProvidedError(MissingInputError):
    def __str__(self) -> str:
        return (
            "Must provide databricks unity catalog name"
        )

class NoSchemaNameProvidedError(BaseException):
    def __str__(self) -> str:
        return(
            "Must provide databricks unity catalog schema name"
        )