# hello-llama-store

The default `VectorStoreIndex` creates an in-memory index. In-memory index is a quick way to setup however it doesn't provide data persistence. LlamaIndex provides us a way to persist data to various data stores including local storage.

With persistent storage we can:

1. Ingest documents an create the index once.
2. Persist the index to a storage. (We need to only do it once, unless the documents are updated)
3. Use the `StorageContext` to load the index from the storage everytime we query instead of doing Step 1 and 2 again and again.
4. Query as many times as we want.

This example demonstrates the use of persistent storage for indices and documents.

---

# Run

```bash
pipenv shell
# Run once
python3 store_local.py

# Run a prompt (without remembering context) that asks for a query to answer based on the indexed documents. Type `exit` to exit.
python3 prompt.py

# Run as many times for single execution query
python3 query.py
```

---
