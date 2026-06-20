import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(uploaded_files):
    documents = []
    for file in uploaded_files:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:
            temp_file.write(file.read())
        pages = PyPDFLoader(temp_file.name).load()
        for page in pages:
            page.metadata["source"] = file.name
        documents.extend(pages)
    return documents

def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(documents)