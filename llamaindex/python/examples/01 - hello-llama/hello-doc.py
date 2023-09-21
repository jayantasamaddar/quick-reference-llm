from llama_index import SimpleDirectoryReader, VectorStoreIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "delhivery-miles.doc"

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Index Document
index = VectorStoreIndex.from_documents(documents)

# Create Query Engine and Query
query_engine = index.as_query_engine()
response = query_engine.query(
    'Who is the "Service Provider" and who is the "Merchant"?'
)
print(response)

# The "Service Provider" is Delhivery Private Limited and the "Merchant" is Kollab Lifestyle Private Limited.
