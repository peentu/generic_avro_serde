### Testing avro-to-python and fastavro
#### avro-to-python
https://pypi.org/project/avro-to-python/
#### fastavro
https://pypi.org/project/fastavro/

### Instructions

1. Generate the model from `example_avro_schema.vsc` using `python generate_model.py`

2. Update the generated code to have `model.` as the namespace root.

3. Run `python main.py`

* The (de)serializer is independent from the model