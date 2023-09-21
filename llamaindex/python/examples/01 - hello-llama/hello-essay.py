from llama_index import SimpleDirectoryReader, VectorStoreIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# ---------------------------------------------------------------------------
# Create Document, Index Document, Query Document, Publish Response from LLM
# ---------------------------------------------------------------------------
## Create Document using `load_data()`
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

## Index data. GPTVectorStoreIndex converts the text data into corresponding vector embeddings and store them in the memory.
index = VectorStoreIndex.from_documents(documents)

## Define Query Engine and Query
query_engine = index.as_query_engine()

response = query_engine.query("What kind of a student was the author?")
print(response)

"""
Version 1
---------
The author was a student who had a strong interest in programming and writing. 
They enjoyed programming on microcomputers and wrote simple games and programs. 
They also had a passion for writing and wrote short stories. 
However, they did not find their college courses in philosophy and painting fulfilling and felt disappointed with the lack of learning opportunities in those subjects.
"""

"""
Version 2
---------
The author was a student who had a strong interest in programming and writing. 
They enjoyed programming on microcomputers and wrote simple games and a word processor. 
However, they did not plan to study programming in college and initially intended to study philosophy. 
They later switched to AI due to their fascination with intelligent computers. 
Additionally, the author attended the Accademia, where they studied painting. 
However, they found that the faculty did not teach much, and the students spent their time chatting or imitating things they had seen in American art magazines.
"""
