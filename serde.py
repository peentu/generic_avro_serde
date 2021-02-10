from fastavro import writer, reader, parse_schema


def serializer(stream, schema, records):
    parsed_schema = parse_schema(schema)
    writer(stream, parsed_schema, records)


def deserializer(stream):
    return reader(stream)
