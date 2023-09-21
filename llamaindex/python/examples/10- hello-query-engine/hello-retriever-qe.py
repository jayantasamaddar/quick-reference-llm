from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    KeywordTableIndex,
    ServiceContext,
    get_response_synthesizer,
)
from llama_index.llms import OpenAI
from llama_index.retrievers import VectorIndexRetriever, KeywordTableSimpleRetriever
from llama_index.query_engine import RetrieverQueryEngine
from custom_retriever import CustomRetriever
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Load Data
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Index Documents
vector_index = VectorStoreIndex.from_documents(documents)
keyword_index = KeywordTableIndex.from_documents(documents)

# Service Context
llm = OpenAI("gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

# Retriever
vector_retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=2)
keyword_retriever = KeywordTableSimpleRetriever(index=keyword_index)
custom_retriever = CustomRetriever(vector_retriever, keyword_retriever)

# Response Synthesizer
response_synthesizer = get_response_synthesizer()

# Query Engine
vector_query_engine = RetrieverQueryEngine(vector_retriever, response_synthesizer)
keyword_query_engine = RetrieverQueryEngine(keyword_retriever, response_synthesizer)
custom_query_engine = RetrieverQueryEngine(custom_retriever, response_synthesizer)

# Queries
vector_query_response = vector_query_engine.query("Name the people mentioned")
keyword_query_response = keyword_query_engine.query("Name the people mentioned")
custom_query_response = keyword_query_engine.query("Name the people mentioned")

print(vector_query_response)
print(keyword_query_response)
print(custom_query_response)

# Responses (may vary)
## (1) vector_query_response
"""
Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar.
"""

## (2) keyword_query_response
"""
The context does not provide any specific names of people mentioned.
"""
## (3) custom_query_response
"""
The people mentioned in the context are Julian, Robert, and Trevor Blackwell. Julian provided $10,000 in seed funding for Viaweb. Robert is Paul Graham's partner in starting Viaweb and working on building online stores. Trevor Blackwell was recommended by Robert and turned out to be a frighteningly effective hacker.
"""
