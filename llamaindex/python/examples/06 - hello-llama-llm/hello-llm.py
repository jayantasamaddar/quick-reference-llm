from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms import OpenAI
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "pangrams.txt"

# Define LLM. By default this has a `temperature` of 0.1 unlike the LangChain version, which has a default of 0.7. You can tweak this.
llm = OpenAI(model="gpt-3.5-turbo")

# Set ServiceContext, which is a utility container for indices and queries
service_context = ServiceContext.from_defaults(llm=llm)

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Index
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Create Query Engine and run Query
query_engine = index.as_query_engine()
response = query_engine.query("What is the common link between all the lines?")
print(response)

# Response:
# --------
"""
The common link between all the lines is that they are all sentences or phrases that contain all 26 letters of the English alphabet.
"""
