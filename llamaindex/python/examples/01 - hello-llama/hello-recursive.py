from llama_index import SimpleDirectoryReader, VectorStoreIndex
from pathlib import Path

__dirname = Path(__file__).resolve().parent
folder_path = __dirname.parent.parent.parent / "data-with-subfolders"


# Load files recursively. `filename_as_id` ensures that doc_ids are not randomly generated and use the filename as id
def recursive_file_load(input_dir):
    documents = SimpleDirectoryReader(
        input_dir=input_dir, recursive=True, filename_as_id=True
    ).load_data()

    # index = VectorStoreIndex.from_documents(documents)

    for doc in documents:
        print(doc.doc_id)


# Run
recursive_file_load(folder_path)

# Output.
## Note: The PDFs are loaded in parts or chunks due to the token limitation which is overcome by Node Parsers.
"""
data-with-subfolders/doc/delhivery-miles.doc
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_0
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_1
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_2
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_3
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_4
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_5
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_6
data-with-subfolders/pdf/accident-benefit-rider-prospectus.pdf_part_7
data-with-subfolders/txt/alliterations.txt
data-with-subfolders/txt/pangrams.txt
"""
