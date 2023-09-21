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

# SummaryIndexRetriever (retriever_mode="default")
retriever = index.as_retriever(retriever_mode="default")

# Create Query Engine and Query
query_engine = RetrieverQueryEngine(retriever)
response = query_engine.query("Give me a short summary of the accident rider")
print(response)

"""
The accident rider provided by Max Life Insurance is an additional coverage option that can be added to a life insurance policy. 
It offers extra protection in the unfortunate event of an accident resulting in dismemberment or death. 
The rider has a specified term, which can range from 10 to 40 years, and is available for individuals between the ages of 18 and 60. 
Premiums for the rider can be paid annually, semi-annually, quarterly, or monthly, with different modal factors applied for non-annual modes. 
It's important to note that the accident rider does not offer surrender or maturity benefits, and there is no cash value associated with it. 
The rider can only be attached to specific base policies offered by Max Life Insurance. 
In the event of death or dismemberment due to an accident, the rider provides an additional sum assured in addition to the base plan benefits. 
Once a claim is made, the rider terminates.
"""
