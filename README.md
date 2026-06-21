# 📚 AI Document Assistant

AI Document Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF and DOCX documents, build a knowledge base, and ask questions about the uploaded content.

The system uses OpenAI embeddings, ChromaDB vector storage, and GPT-4o-mini to retrieve relevant information and generate accurate answers based only on the uploaded documents.

---

## 🚀 Features

- Upload PDF and DOCX files
- Build a searchable knowledge base
- Ask questions in natural language
- Retrieve relevant document chunks
- AI-powered answer generation
- Source citations for transparency
- Hallucination prevention
- Multi-document support
- Streamlit-based user interface

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python
- LangChain

### AI & RAG
- OpenAI GPT-4o-mini
- OpenAI Embeddings
- ChromaDB

### Document Processing
- PyPDF
- Python-Docx

---

## 📂 Project Structure

```text
document-qa-bot/
│
├── app.py
├── ingest.py
├── rag.py
├── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Dharmendra-Mr/document-qa-bot.git

cd document-qa-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload one or more PDF/DOCX documents.
2. Click **Process Documents**.
3. Documents are split into chunks.
4. Chunks are converted into embeddings.
5. Embeddings are stored in ChromaDB.
6. User asks a question.
7. Relevant chunks are retrieved.
8. GPT-4o-mini generates an answer using retrieved context.
9. Sources are displayed with the response.

---

## 🎯 Example Questions

```text
Which university did Dharmendra study at?

What technical skills are mentioned in the resume?

What projects has the candidate worked on?
```

---

## 🛡️ Hallucination Prevention

The assistant only answers using information found in the uploaded documents.

If information is not available, the system responds:

```text
I couldn't find this information in the uploaded documents.
```

---

## 📸 Screenshots

### Upload Documents

(Add Screenshot)

### Ask Questions

(Add Screenshot)

### Source Citations

(Add Screenshot)

---

## 👨‍💻 Author

Dharmendra Nukella

B.Tech Computer Science & Engineering

Parul University, Vadodara, Gujarat

GitHub:
https://github.com/Dharmendra-Mr