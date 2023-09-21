from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.output_parsers import LangchainOutputParser
from llama_index.llm_predictor import StructuredLLMPredictor
from llama_index.prompts import PromptTemplate
from llama_index.prompts.default_prompts import (
    DEFAULT_TEXT_QA_PROMPT_TMPL,
    DEFAULT_REFINE_PROMPT_TMPL,
)
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from helpers import strip
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# load documents, build index
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
index = VectorStoreIndex.from_documents(documents)
llm_predictor = StructuredLLMPredictor()

# define output schema
response_schemas = [
    ResponseSchema(
        name="Education",
        description="Describes the author's educational experience/background.",
    ),
    ResponseSchema(
        name="Work", description="Describes the author's work experience/background."
    ),
]

# define output parser
lc_output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
output_parser = LangchainOutputParser(lc_output_parser)

# format each prompt with output parser instructions
fmt_qa_tmpl = output_parser.format(DEFAULT_TEXT_QA_PROMPT_TMPL)
fmt_refine_tmpl = output_parser.format(DEFAULT_REFINE_PROMPT_TMPL)
qa_prompt = PromptTemplate(fmt_qa_tmpl, output_parser=output_parser)
refine_prompt = PromptTemplate(fmt_refine_tmpl, output_parser=output_parser)

# query index
query_engine = index.as_query_engine(
    service_context=ServiceContext.from_defaults(llm_predictor=llm_predictor),
    text_qa_template=qa_prompt,
    refine_template=refine_prompt,
)
response = query_engine.query(
    "What are a few things the author?",
)

# Response 1
print(response)

# Response 2
print(strip(str(response)))

# Response 1
"""
```json
{
        "Education": "The author initially planned to study philosophy in college but switched to AI.",
        "Work": "The author has worked on building the infrastructure of the web, publishing essays online, spam filters, and painting."
}
```
"""

# Response 2
"""
{"Education": "The author initially planned to study philosophy in college but switched to AI.", "Work": "The author worked on building the infrastructure of the web, wrote essays, worked on spam filters, and did some painting."}
"""
