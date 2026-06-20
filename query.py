from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)
query = "Which university did Dharmendra study at?"
results = vector_store.similarity_search(
    query,
    k=3
)
for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 50)
    print(doc.page_content[:500])