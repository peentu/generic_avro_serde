from avro_to_python.reader import AvscReader
from avro_to_python.writer import AvroWriter

# initialize the reader object
reader = AvscReader(file='example_avro_schema.avsc')

# generate the acyclic tree object
reader.read()

# initialize the writer object
writer = AvroWriter(reader.file_tree)

# generated python files will have 'model as the namespace root'
writer.write(root_dir='model')
