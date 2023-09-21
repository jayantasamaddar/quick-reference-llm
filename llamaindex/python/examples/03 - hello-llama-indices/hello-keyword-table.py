from llama_index import SimpleDirectoryReader, KeywordTableIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Create Documents
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Index
index = KeywordTableIndex.from_documents(documents)

# Create Query Engine and run Query
query_engine = index.as_query_engine()
response = query_engine.query("Who are the people the author has interacted with?")
print(response)

# Response:
# --------
## The author has interacted with Robert, Trevor, and Julian, who provided seed funding for their company Viaweb.
