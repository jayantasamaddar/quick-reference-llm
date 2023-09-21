from llama_index import SimpleDirectoryReader, VectorStoreIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Index
index = VectorStoreIndex.from_documents(documents)

# Create Chat Engine and start Chat
## `chat_mode` can be any of the following: `best`, `condense_question`, `simple`, `react`, `openai`, `context`
## `condense_question` always queries the knowledge base and cannot contextualize conversation as such except for the last message.
## `verbose=True` lets us know how the engine is thinking, i.e. the actual query it sends after modifying our prompt.
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)


# Create a mini chat messenger
def prompt():
    question = input("Prompt: ")
    while question.lower() != "exit":
        streaming_response = chat_engine.stream_chat(question)
        for token in streaming_response.response_gen:
            print(token, end="")
        print("\n")
        return prompt()
    return chat_engine.reset()


if __name__ == "__main__":
    prompt()

# Prompts
"""
Prompt: Name the people mentioned
Querying with: Who are the people mentioned in the conversation?
The people mentioned in the conversation are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar.

Prompt: How are they related to the author?
Querying with: How are Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar related to the author?
The author mentions Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar in the context of thanking them for reading drafts of the text. Therefore, it can be inferred that these individuals are acquaintances or colleagues of the author.

Prompt: Who is the closest acquaintance or friend to the author?
Querying with: Who among Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar is the closest acquaintance or friend to the author?
Based on the given context information, it is not possible to determine who among Trevor Blackwell, John Collison, Patrick Collison, Daniel Gackle, Ralph Hazell, Jessica Livingston, Robert Morris, and Harj Taggar is the closest acquaintance or friend to the author.
"""
