from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from langchain.chat_models import ChatOpenAI
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"


# Initialize
def initialize():
    global index
    try:
        # load index if already exists
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(storage_context)
    except:
        # otherwise, load documents and create index

        # Create Document
        documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

        # Create LLM Predictor
        llm_predictor = LLMPredictor(
            llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        )

        #
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

        # Create Index
        index = VectorStoreIndex.from_documents(
            documents=documents,
            service_context=service_context,
            llm_predictor=llm_predictor,
        )


initialize()

# Create Chat Engine and start Chat
## `chat_mode` can be any of the following: `best`, `condense_question`, `simple`, `react`, `openai`, `context`
## `condense_question` always queries the knowledge base and cannot contextualize conversation as such except for the last message.
## `verbose=True` lets us know how the engine is thinking, i.e. the actual query it sends after modifying our prompt.
chat_engine = index.as_chat_engine(chat_mode="react", verbose=True)


# Create a mini chat messenger
def prompt():
    question = input("Prompt: ")
    while question.lower() != "exit":
        response = chat_engine.chat(question)
        print(response)
        return prompt()
    return chat_engine.reset()


if __name__ == "__main__":
    prompt()


# Prompts
"""
Prompt: Name the people mentioned        
Response: Sure, could you please provide me with the context or any specific information related to the people you want me to identify?
Sure, could you please provide me with the context or any specific information related to the people you want me to identify?
Prompt: Use the tool and name the people mentioned
Thought: I need to use a tool to help me identify the people mentioned.
Action: query_engine_tool
Action Input: {'input': 'Who are the people mentioned?'}
Observation: The people mentioned in the context are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar.
Response: The people mentioned in the context are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar.
The people mentioned in the context are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar.

Prompt: What country are these people from?                                                                                                     
Thought: I need to use a tool to help me answer the question.
Action: query_engine_tool
Action Input: {'input': 'What country are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar from?'}
Observation: The context information does not provide any information about the country of origin of Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar.
Response: The country of origin for Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar is not provided in the given context.
The country of origin for Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar is not provided in the given context.

Prompt: Do not use the tool and try to find where those surnames originate from
Response: The surnames Blackwell, Collison, Hazell, and Morris are of English origin, the surname Livingston is of Scottish origin, and the surnames Gackle and Taggar do not have a specific origin listed.
The surnames Blackwell, Collison, Hazell, and Morris are of English origin, the surname Livingston is of Scottish origin, and the surnames Gackle and Taggar do not have a specific origin listed.
"""
