from llama_index import SimpleDirectoryReader, SummaryIndex
from llama_index.indices.postprocessor import KeywordNodePostprocessor
from llama_index.query_engine import RetrieverQueryEngine
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = (
    __dirname.parent.parent.parent / "data" / "accident-benefit-rider-prospectus.pdf"
)

# Load Documents
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Summary Index
index = SummaryIndex.from_documents(documents)

# Filters nodes by required_keywords and exclude_keywords
node_postprocessors = [
    KeywordNodePostprocessor(
        required_keywords=["accident"], exclude_keywords=["vibgyor"]
    )
]

# Configure `retriever_mode="embedding"`, i.e. SummaryIndexEmbeddingRetriever (Other options: `default`, `embedding`, `llm`)
retriever = index.as_retriever(retriever_mode="embedding")

# Create Query Engine and Query
query_engine = RetrieverQueryEngine(retriever, node_postprocessors=node_postprocessors)
response = query_engine.query("Give me a short summary of the accident rider")
print(response)

"""
The accident rider is an additional benefit that can be added to an insurance policy. It provides coverage in the event of dismemberment or death due to an accident. 
If the insured person suffers a covered dismemberment, a lump sum amount is paid out immediately. 
In the case of death due to an accident, the rider also pays out a lump sum amount. 
However, once a claim is made under the rider, the rider contract terminates. The base policy, on the other hand, continues to provide its benefits.
"""
