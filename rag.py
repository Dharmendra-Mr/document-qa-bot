from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def build_vector_store(chunks):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

def get_answer(vector_store, question):
    docs = vector_store.similarity_search(
        question,
        k=3
    )
    context = "\n\n".join(
        doc.page_content for doc in docs
    )
    prompt = f"""
Answer only from the provided context.
If the answer is not available, say:
I couldn't find this information in the uploaded documents.
Context:
{context}
Question:
{question}
"""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    response = llm.invoke(prompt)
    return response.content, docs