from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
    Prompt,
    get_response_synthesizer,
)
from llama_index.llms import OpenAI
from llama_index.prompts import PromptType
from llama_index.query_engine import RetrieverQueryEngine
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Load Documents
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Define Custom LLM
llm = OpenAI("gpt-3.5-turbo")
service_context = ServiceContext.from_defaults(llm=llm)

# Define Custom Prompt
CUSTOM_QA_TEMPLATE_STR = (
    "Context information is below. "
    "---------------------\n"
    "{context_str}"
    "---------------------\n"
    "Given the context information, and not the prior knowledge,"
    "Answer the question: {query_str}\n"
)
QA_TEMPLATE = Prompt(CUSTOM_QA_TEMPLATE_STR, prompt_type=PromptType.QUESTION_ANSWER)

CUSTOM_REFINE_TEMPLATE_STR = (
    "The original query is as follows: {query_str}\n"
    "We have provided an existing answer: {existing_answer}\n"
    "We have the opportunity to refine the existing answer "
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "Given the new context, refine the original answer to better "
    "answer the query. "
    "If the context isn't useful, return the original answer.\n"
    "Refined Answer: "
)
REFINE_TEMPLATE = Prompt(CUSTOM_REFINE_TEMPLATE_STR, prompt_type=PromptType.REFINE)

service_context = ServiceContext.from_defaults(llm=llm)

index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Option 1: Using High-Level, `index.as_query_engine` with `text_qa_template` and `refine_template` passed as **kwargs
# query_engine = index.as_query_engine(
#     text_qa_template=QA_TEMPLATE, refine_template=REFINE_TEMPLATE, verbose=True
# )

# ------------------------------------------------
# Option 2: Using Low-Level `RetrieverQueryEngine`
# ------------------------------------------------

## (2a) Using `RetrieverQueryEngine` and declaring some additional **kwargs
retriever = index.as_retriever()
# query_engine = RetrieverQueryEngine.from_args(
#     retriever,
#     text_qa_template=QA_TEMPLATE,
#     refine_template=REFINE_TEMPLATE,
#     verbose=True,
# )

## (2b): Using Low-Level `get_response_synthesizer with `RetrieverQueryEngine`. No additional `**kwargs` declaration needed. Fully typed.
response_synthesizer = get_response_synthesizer(
    text_qa_template=QA_TEMPLATE, refine_template=REFINE_TEMPLATE, verbose=True
)
query_engine = RetrieverQueryEngine.from_args(retriever, response_synthesizer)

response = query_engine.query("Name the people mentioned")
print(response)

# Response
"""
The people mentioned in the context are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, Harj Taggar, Cezanne, and professor Ulivi.
"""
