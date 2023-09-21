from llama_index import SimpleDirectoryReader, TreeIndex, StorageContext
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import PrevNextNodePostprocessor
from pathlib import Path

__dirname = Path(__file__).resolve().parent
file_path = (
    __dirname.parent.parent.parent / "data" / "accident-benefit-rider-prospectus.pdf"
)

# Create Documents
documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

# Create a Tree Index
index = TreeIndex.from_documents(documents)

# By default data is stored in-memory. To persist to dist under `./storage`
index.storage_context.persist()

# Create PostProcessor
storage_context = StorageContext.from_defaults(persist_dir="./storage")
docstore = storage_context.docstore
node_postprocessors = [PrevNextNodePostprocessor(docstore=docstore, mode="both")]

# Configure `retriever_mode="all_leaf"`, i.e. TreeAllLeafRetriever (Other options: `select_leaf`, `select_leaf_embedding`, `all_leaf`, `root`)
retriever = index.as_retriever(retriever_mode="all_leaf")

# Create Query Engine and run Query
query_engine = RetrieverQueryEngine(retriever, node_postprocessors=node_postprocessors)
response1 = query_engine.query("Create a 'Table of Contents' for the policy.")
response2 = query_engine.query(
    "Create a 'Table of Contents' for the policy. Can have nesting."
)
print(response1)
print(response2)

# `response1`
"""
1. Introduction
2. About Max Life Insurance
3. Max Life Comprehensive Accident Benefit Rider: Protect your family's future
4. Max Life Comprehensive Accident Benefit Rider at a Glance
5. Premium Modes
6. Minimum and Maximum Sum Assured
7. Premium Rate
8. Lapse and Revival
9. Surrender Benefit
10. Maturity Benefit
11. Cash Value
12. Base Policy with which Rider can be attached
13. Benefits Payable
14. How does the Max Life Comprehensive Accident Benefit Rider work for you?
15. Important Notes
16. Few important terms and conditions
17. Statutory impositions
18. Exclusions
19. Full Disclosure & Incontestability
20. Prohibition of Rebates
21. Free Look Period
22. Grace Period
23. Nomination
24. Assignment
25. Contact Details of the Company
26. Disclaimers
27. Beware of Spurious/Fraud Phone Calls
"""

# response2
"""
1. Max Life - Comprehensive Accident Benefit Rider
   1.1 About Max Life Insurance
   1.2 Max Life Comprehensive Accident Benefit Rider: Protect your family's future
   1.3 Max Life Comprehensive Accident Benefit Rider at a Glance
2. Premium Modes
3. Minimum and Maximum Sum Assured
4. Premium Rate
5. Lapse and Revival
6. Surrender Benefit
7. Maturity Benefit
8. Cash Value
9. Base Policy with which Rider can be attached
10. Benefits Payable
   10.1 Death due to an accident
   10.2 Dismemberment due to an accident
11. How does the Max Life Comprehensive Accident Benefit Rider work for you?
   11.1 Scenario 1: Mr. Kumar meets with a road accident and unfortunately loses both his limbs
   11.2 Scenario 2: Mr. Kumar meets with a road accident and dies due to injuries suffered in it
   11.3 Scenario 3: Mr. Kumar meets with a road accident and unfortunately loses both his limbs, then dies due to another accident
12. Important Notes
   12.1 Tax Benefits
   12.2 Extra premium for substandard lives
13. Few important terms and conditions
   13.1 Statutory impositions
   13.2 Exclusions
"""
