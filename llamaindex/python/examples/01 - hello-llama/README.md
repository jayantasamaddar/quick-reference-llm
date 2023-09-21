# hello-llama

The basic LlamaIndex workflow is of four steps:

1. Load Data into a Document
   - Manually, or
   - Using the `load_data` function
2. Index Data
3. Define Query Engine and Query
4. Receive and take action based on the response received about the query from the LLM

This example is to demonstrate this basic workflow.

---

# Dependencies

**Install the following packages**:

```bash
pip install langchain openai

# Read .pdf
pip install pypdf

# Read .doc
pip install docx2txt ## or have `docutils` installed
```

Declare an environment variable for the OpenAI API in the `examples` folder:

```bash
OPENAI_API_KEY=sk-Tssd7QsrvxmlRoqb+koasjuS4EtqiY5tLPggKpy2LQFJ9wsD
```

---

# Run

```bash
printenv shell
python3 hello-essay.py
python3 hello-sample.py
```

---
