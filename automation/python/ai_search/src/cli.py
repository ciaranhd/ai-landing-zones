import argparse
from .models import SearchIndexDef, SearchFieldDef
from .service import provision_index

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--api-key", required=True)

    args = parser.parse_args()

    index_def = SearchIndexDef(
        name="customers",
        fields=[
            SearchFieldDef(
                name="id",
                type="Edm.String",
                key=True,
                searchable=False,
            ),
            SearchFieldDef(
                name="name",
                type="Edm.String",
                searchable=True,
            ),
        ],
    )

    provision_index(
        endpoint=args.endpoint,
        api_key=args.api_key,
        definition=index_def,
    )


if __name__ == "__main__":
    main()
