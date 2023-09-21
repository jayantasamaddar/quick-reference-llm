from llama_index import (
    SimpleDirectoryReader,
    SummaryIndex,
    ServiceContext,
    StorageContext,
)
from llama_index.indices.list import SummaryIndexEmbeddingRetriever
from llama_index.llms import OpenAI
from llama_index.storage.storage_context import DEFAULT_PERSIST_DIR
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Load Documents and Create Index
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
index = SummaryIndex.from_documents(documents)

# Store
index.storage_context.persist(DEFAULT_PERSIST_DIR)

# Define llm
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

# Store
storage_context = StorageContext.from_defaults(persist_dir=DEFAULT_PERSIST_DIR)

# Specify parameters
service_context = ServiceContext.from_defaults(llm=llm)

# Initialize retriever and use retriever to retrieve nodes using the Low-Level Composition API
retriever = SummaryIndexEmbeddingRetriever(
    index=index,
    ## Depends on the type of index. For a SummaryIndex, specifying `retriever_mode` has no effect (silently ignored).
    similarity_top_k=1,
)
nodes = retriever.retrieve("Describe the personality of the author")

# Response: Return List of nodes with score
print(nodes)
