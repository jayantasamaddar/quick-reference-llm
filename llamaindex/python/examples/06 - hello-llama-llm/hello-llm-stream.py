from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex
from llama_index.llms import OpenAI
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "pangrams.txt"

# Define LLM. By default this has a `temperature` of 0.1 unlike the LangChain version, which has a default of 0.7. You can tweak this.
llm = OpenAI(model="gpt-3.5-turbo")

# Set ServiceContext, which is a utility container for indices and queries
service_context = ServiceContext.from_defaults(llm=llm)

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Index
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Create Query Engine and run Query. Set `streaming=True`.
query_engine = index.as_query_engine(streaming=True)
response = query_engine.query(
    "What is the common link between all the lines? Suggest 10 other pangrams."
)

# Print the stream response
response.print_response_stream()

# Response:
# --------
"""
The common link between all the lines is that they are all examples of pangrams. A pangram is a sentence or phrase that contains every letter of the alphabet at least once. 

Here are 10 other examples of pangrams:
1. The five boxing wizards jump quickly.
2. Jaded zombies acted quaintly but kept driving their oxen forward.
3. How quickly daft jumping zebras vex.
4. Sphinx of black quartz, judge my vow.
5. The quick onyx goblin jumps over the lazy dwarf.
6. Crazy Frederick bought many very exquisite opal jewels.
7. A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent.
8. Jackdaws love my big sphinx of quartz.
9. The five boxing wizards jump quickly.
10. A wizard's job is to vex chumps quickly in fog.
"""
