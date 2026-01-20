# Resources


# https://github.com/ciaranhd/book/blob/master/introduction.asciidoc


Feature transformation

We control the logic — the functions that create, clean, and transform features.

Example:

def feature_engineer(df, config):
    # deterministic mapping
    for f in config.features:
        df = df.withColumn(f"{f}_squared", df[f] * df[f])
    return df


Deterministic, pure in the functional sense: given the same input DataFrame, it always produces the same output.

Can be unit-tested fully, no side effects, no external systems.

This is our business logic, so it belongs in builders.py.

Model fitting (fit)

fit is a method provided by an external library (e.g., scikit-learn, xgboost).

It mutates internal state inside the model object.

Implementation is opaque: we cannot reason about its internals, only about its interface.

Often, fit may include randomness (unless seeded), numerical optimizations, etc.

Side effects occur: objects are mutated, external calls may happen (logging in some frameworks, caching, etc.).

Because of these reasons, it crosses the boundary from pure functional logic → effectful operation.

Even if you wrap fit in a pure function, internally it’s not fully deterministic without careful seeding.

Logging the trained model to MLflow is an additional side effect that can’t live in a pure functional layer.

2️⃣ Guiding principle in functional architecture

Anything you fully control and can make deterministic belongs in the functional core (builders.py).
Anything that is external, mutates state, or has side effects belongs in the orchestration layer (service.py) or adapters (client.py).

Feature transformations = core logic we control → builders.py

Model fitting and logging = external operation → service.py

SDK calls, database writes, MLflow logs = side effects → client.py


| Step             | Who controls it? | Pure/Effectful       | Layer          |
| ---------------- | ---------------- | -------------------- | -------------- |
| Chop vegetables  | You              | Pure                 | Builders       |
| Bake in the oven | Oven             | Effectful (external) | Service/Client |
| Serve to guest   | You              | Effectful            | Service/Client |
