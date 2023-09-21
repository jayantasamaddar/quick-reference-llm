from llama_index import SimpleDirectoryReader, Document
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = __dirname.parent.parent.parent / "data" / "sample.txt"

# ------------------
# Create a Document
# ------------------
## Auto-create Document using load_data() function
documents1 = SimpleDirectoryReader(input_files=[file_path]).load_data()
print(documents1)
### [Document(id_='80bcc1c6-ec82-4a87-bc95-961780476cb5', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, hash='4ff002687be59b78f2cd5e793f706bd7c709f052edfee2ff7c8b02b89e3da984', text='The quick brown fox jumps over a lazy dog\nPack my box with five dozen liquor jugs\nMr. Jock, TV quiz PhD, bags few lynx', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')]

## Manually create Document
text_list = ["This is first sentence", "This is second sentence"]
documents2 = [Document(text=t) for t in text_list]
print(documents2)
### [Document(id_='78f49172-3ecd-4bf6-80f2-cc237b8b5a0b', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, hash='2aeee108600f2dbac3a8425fec4b84f7eb44a3fc6bb73cdfbc8c0932c356a148', text='This is first sentence', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n'), Document(id_='2fd7c7f6-bc0c-44b2-b1eb-ef0f59cbe838', embedding=None, metadata={}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, hash='d6a5ccbbf84f94a3d72aed767518a3ded3f06cfeebefd2bac90a4115bebe7c26', text='This is second sentence', start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')]
