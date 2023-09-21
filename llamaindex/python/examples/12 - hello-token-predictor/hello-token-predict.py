from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import MockLLM
from llama_index import MockEmbedding
from llama_index.callbacks import CallbackManager, TokenCountingHandler
import tiktoken
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Create a token_counter and add it to the callback_manager
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
)
callback_manager = CallbackManager([token_counter])

# Load Documents
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Index Documents
index = VectorStoreIndex.from_documents(documents)

# Create Predictors
llm = MockLLM(max_tokens=256)
embed_model = MockEmbedding(embed_dim=1536)

# Service Context
service_context = ServiceContext.from_defaults(
    # llm_predictor=llm_predictor,
    llm=llm,
    embed_model=embed_model,
    callback_manager=callback_manager,
)

# Query Engine
query_engine = index.as_query_engine(service_context=service_context)

# Run Query
response = query_engine.query("Describe the author's activities")

# Response
print("LLM Prompt Tokens: ", token_counter.prompt_llm_token_count)
print("LLM Completion Tokens: ", token_counter.completion_llm_token_count)
print("Total LLM Token Count: ", token_counter.total_llm_token_count)
print("Total Embedding Token Usage: ", token_counter.total_embedding_token_count)

"""
LLM Prompt Tokens:  1982
LLM Completion Tokens:  256
Total LLM Token Count:  2238
Total Embedding Token Usage:  0
"""
