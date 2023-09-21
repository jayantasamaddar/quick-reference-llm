from store_local import query_index


# Ask something about the essay in `data/essay.txt`. Type `exit` to exit.
def prompt():
    question = input("Ask something based on the essay: ")
    while question.lower() != "exit":
        answer = query_index(question)
        print(answer)
        return prompt()


if __name__ == "__main__":
    prompt()

"""
P1. Who is Jessica?
Ans: Jessica is a woman who the author met at a party and later asked out. She was in charge of marketing at a Boston investment bank and later decided to compile a book of interviews with startup founders. She was also offered a marketing job at a Boston VC firm.

P2. Who is Robert Morris?
Ans: Robert Morris is a person mentioned in the given context. However, the context does not provide enough information to determine who Robert Morris is.

P3. Describe the author's overall experience in 160 characters or less
Ans: The author's overall experience involved working on a challenging project, moving to another country, finishing a significant task, and writing essays.
"""
