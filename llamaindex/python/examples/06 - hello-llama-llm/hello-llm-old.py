from llama_index import (
    SimpleDirectoryReader,
    ServiceContext,
    VectorStoreIndex,
    LLMPredictor,
)
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "pangrams.txt"

# This required the langchain library. Check the `hello-llm2.py` for the update as per 0.7.0
from langchain.chat_models import ChatOpenAI

# Define LLM
llm_predictor = LLMPredictor(llm=ChatOpenAI(model="gpt-3.5-turbo"))

# Set ServiceContext, which is a utility container for indices and queries
service_context = ServiceContext.from_defaults(llm_predictor)

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Index
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Create Query Engine and run Query
query_engine = index.as_query_engine()
response = query_engine.query("What is the common link between all the lines?")
print(response)

# Running twice:
# --------------
# Response 1:
"""
The common link between all the lines is that they are all sentences or phrases that contain all the letters of the English alphabet.
"""

# Response 2:
"""
The common link between all the lines is that they are all examples of pangrams.
"""

# Response 3:
"""
All the lines in the context are examples of pangrams, which are sentences or phrases that contain every letter of the alphabet at least once.
"""
