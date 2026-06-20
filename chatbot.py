from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Load Chroma DB
vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

question = input("Ask a question: ")

# Retrieve top chunks
docs = vector_store.similarity_search(question, k=3)

context = "\n\n".join([doc.page_content for doc in docs])

prompt = f"""
You are a document QA assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I couldn't find this information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)

print("\nAnswer:")
print(response.content)