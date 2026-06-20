import streamlit as st
from dotenv import load_dotenv

from ingest import load_documents, create_chunks
from rag import build_vector_store, get_answer

load_dotenv()

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📚",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "db" not in st.session_state:
    st.session_state.db = None

if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

with st.sidebar:
    st.header("📊 Project Info")
    st.metric(
        "Documents",
        len(st.session_state.get("uploaded_files", []))
    )
    st.metric(
        "Chunks",
        st.session_state.chunk_count
    )
    st.write("Model: GPT-4o-mini")
    st.write("Vector DB: ChromaDB")
    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
st.title("📚 AI Document Assistant")
st.write(
    "Upload PDF/DOCX files and ask questions about them."
)

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.session_state.uploaded_files = uploaded_files
    st.success(
        f"{len(uploaded_files)} file(s) selected"
    )
    st.subheader("Uploaded Files")
    for file in uploaded_files:
        st.write(f"📄 {file.name}")

if st.button("📄 Process Documents"):
    if not uploaded_files:
        st.warning(
            "Please upload at least one document."
        )

    else:
        with st.spinner(
            "Reading documents and building vector database..."
        ):
            documents = load_documents(
                uploaded_files
            )
            chunks = create_chunks(
                documents
            )
            st.session_state.db = (
                build_vector_store(chunks)
            )
            st.session_state.chunk_count = (
                len(chunks)
            )
        st.success(
            f"Successfully processed {len(uploaded_files)} document(s) and created {len(chunks)} chunks."
        )
st.divider()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input(
    "Ask a question about your documents..."
)

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)
    if st.session_state.db is None:
        answer = (
            "Please upload documents and click 'Process Documents' first."
        )
    else:
        with st.spinner(
            "Searching documents..."
        ):
            answer, docs = get_answer(
                st.session_state.db,
                question
            )

    with st.chat_message("assistant"):
        st.write(answer)
        if st.session_state.db is not None:
            st.markdown("### 📌 Sources")
            shown = set()
            for doc in docs:
                source = doc.metadata.get(
                    "source",
                    "Unknown"
                )
                page = (
                    doc.metadata.get(
                        "page",
                        0
                    ) + 1
                )
                citation = (
                    f"{source} (Page {page})"
                )
                if citation not in shown:
                    shown.add(citation)
                    st.write(
                        f"• {citation}"
                    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )