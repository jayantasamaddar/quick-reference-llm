from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = (
    __dirname.parent.parent.parent / "data" / "accident-benefit-rider-prospectus.pdf"
)

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Index Document
index = VectorStoreIndex.from_documents(documents)

# Configure Retriever. Default `similarity_top_k` = 2
retriever = VectorIndexRetriever(index, similarity_top_k=2)

# Apply a `similarity_cutoff`
node_postprocessors = [SimilarityPostprocessor(similarity_cutoff=0.7)]

# Create Query Engine and Query
query_engine = RetrieverQueryEngine(retriever, node_postprocessors=node_postprocessors)
response = query_engine.query("Give me a short summary of the accident rider")
print(response)

"""
The accident rider is an additional benefit that can be added to a life insurance policy. 
It provides coverage in the event of an accident resulting in dismemberment or death. 
If the insured suffers a covered dismemberment, a lump sum payment is made immediately. 
If the insured dies due to injuries from an accident, a lump sum payment is made to the beneficiary. The rider terminates after a claim is approved.
"""
