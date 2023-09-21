from llama_index import PromptTemplate, SimpleDirectoryReader, VectorStoreIndex
from llama_index.response_synthesizers import get_response_synthesizer
from llama_index.llms import OpenAI
from rag_query_engine import RAGQueryEngine, RAGStringQueryEngine
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# ------------------
# Phase 1: Load Data
# ------------------
## Load Documents
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

## Create Index
index = VectorStoreIndex.from_documents(documents)

## Modify retriever
retriever = index.as_retriever()

# -------------------------------------------------------------------------------
# Phase 2: Simulates a RAG pipeline. First perform retrieval, and then synthesis.
# -------------------------------------------------------------------------------

## (2a) Retrieval
qa_prompt = PromptTemplate(
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, "
    "answer the query.\n"
    "Query: {query_str}\n"
    "Answer: "
)

response_synthesizer = get_response_synthesizer(response_mode="compact", verbose=True)

llm = OpenAI(model="gpt-3.5-turbo")

query_engine = RAGStringQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
    llm=llm,
    qa_prompt=qa_prompt,
)

# query_engine = RAGQueryEngine(
#     retriever=retriever, response_synthesizer=response_synthesizer
# )

response = query_engine.query("Who are the people mentioned")

# # Response
print(response)

# Option 1
"""
Traceback (most recent call last):
  File "/Users/jayanta/Work/quick-reference-llm/llamaindex/examples-python/10- hello-query-engine/hello-custom-qe.py", line 49, in <module>
    response = query_engine.query("Who are the people mentioned")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jayanta/.local/share/virtualenvs/10-_hello-query-engine-QsvNZDng/lib/python3.11/site-packages/llama_index/query_engine/custom.py", line 36, in query
    with self.callback_manager.as_trace("query"):
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'FieldInfo' object has no attribute 'as_trace'
"""

# Option 2
"""
Traceback (most recent call last):
  File "/Users/jayanta/Work/quick-reference-llm/llamaindex/examples-python/10- hello-query-engine/hello-custom-qe.py", line 38, in <module>
    query_engine = RAGStringQueryEngine(
                   ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jayanta/.local/share/virtualenvs/10-_hello-query-engine-QsvNZDng/lib/python3.11/site-packages/pydantic/main.py", line 165, in __init__
    __pydantic_self__.__pydantic_validator__.validate_python(data, self_instance=__pydantic_self__)
TypeError: BaseModel.validate() takes 2 positional arguments but 3 were given
"""
