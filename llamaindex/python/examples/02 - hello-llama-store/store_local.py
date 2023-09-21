from typing import Dict, List
from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.readers.base import BaseReader
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "essay.txt"


def construct_index(
    input_dir: str | None = None,
    input_files: List | None = None,
    exclude: List | None = None,
    exclude_hidden: bool = True,
    errors: str = "ignore",
    recursive: bool = False,
    encoding: str = "utf-8",
    filename_as_id: bool = False,
    required_exts: List[str] | None = None,
    file_extractor: Dict[str, BaseReader] | None = None,
    num_files_limit: int | None = None,
):
    documents = SimpleDirectoryReader(
        input_dir,
        input_files,
        exclude,
        exclude_hidden,
        errors,
        recursive,
        encoding,
        filename_as_id,
        required_exts,
        file_extractor,
        num_files_limit,
    ).load_data()
    index = VectorStoreIndex.from_documents(documents)

    # By default data is stored in-memory. To persist to dist under `./storage`
    index.storage_context.persist()

    return index


def query_index(query):
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")

    # load index
    index = load_index_from_storage(storage_context)

    # query
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)


if __name__ == "__main__":
    construct_index(input_files=[file_path])
