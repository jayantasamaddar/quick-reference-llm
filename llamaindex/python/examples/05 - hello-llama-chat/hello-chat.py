from llama_index import SimpleDirectoryReader, SummaryIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"

# Create Document
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create Index
index = SummaryIndex.from_documents(documents)

# Create Chat Engine and start Chat
## `chat_mode` can be any of the following: `best`, `condense_question`, `simple`, `react`, `openai`, `context`
## `condense_question` always queries the knowledge base and cannot contextualize conversation as such except for the last message.
## `verbose=True` lets us know how the engine is thinking, i.e. the actual query it sends after modifying our prompt.
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)


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
