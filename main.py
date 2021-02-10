# json to parse the schema string into a dict
import json
# the class we will be serializing
from model.org.kpn.greenbox.ri import CustomerTransaction
# our (de)serialization code
import serde


# the raw data
record = {
        "transaction": "created",
        "customerId": "testId",
        "postalCode": "postcode",
        "houseNumber": 100,
        "timestamp": 1000,
        "products": [
            {
                "productId": "pid",
                "name": "pname",
                "number": 11
            }
        ]
    }

# initialize a CustomerTransaction from the raw data
obj = CustomerTransaction(record)

print(type(obj))
print(obj)

# load the schema that is available on the class
# no dependency on the schema file (example_avro_schema.avsc)
schema = json.loads(CustomerTransaction.schema)

# Serialize
with open('out.avro', 'wb') as out_stream:
    serde.serializer(out_stream, schema, [obj.dict()])

# Deserialize
with open('out.avro', 'rb') as in_stream:
    result = serde.deserializer(in_stream)
    for record in result:
        print(record)
