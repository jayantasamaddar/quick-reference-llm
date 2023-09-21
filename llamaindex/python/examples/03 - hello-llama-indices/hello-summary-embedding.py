from llama_index import SimpleDirectoryReader, SummaryIndex
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

# Configure `retriever_mode="embedding"`, i.e. SummaryIndexEmbeddingRetriever (Other options: `default`, `embedding`, `llm`)
retriever = index.as_retriever(retriever_mode="embedding")

# Create Query Engine and Query
query_engine = RetrieverQueryEngine(retriever)
response = query_engine.query("Give me a short summary of the accident rider")
print(response)

"""
The accident rider, known as the Max Life Comprehensive Accident Benefit Rider, provides additional protection against accidents for policyholders. 
In the event of dismemberment or death due to a covered accident, the rider pays out a sum assured to the policyholder or their nominee. 
The rider terminates after a claim is approved. 
The rider can be added to an existing insurance policy at a nominal incremental price.
"""
