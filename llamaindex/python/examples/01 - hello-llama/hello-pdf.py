from llama_index import SimpleDirectoryReader, VectorStoreIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = (
    __dirname.parent.parent.parent / "data" / "accident-benefit-rider-prospectus.pdf"
)

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Index Document
index = VectorStoreIndex.from_documents(documents)

# Create Query Engine and Query
query_engine = index.as_query_engine()
response = query_engine.query("Give me a short summary of the accident rider")
print(response)

"""
The accident rider is an additional benefit that can be added to a life insurance policy. 
It provides coverage in the event of an accident resulting in dismemberment or death. 
If the insured suffers a specified dismemberment, such as the loss of both hands or both feet, the rider pays out a sum assured. 
In the case of death due to an accident, the rider also pays out a sum assured. The rider terminates after a claim is approved.
"""
