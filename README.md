# 🤖 Nineleaps HR Knowledge Assistant

An AI-powered HR Knowledge Assistant built using Retrieval-Augmented Generation (RAG).

The application allows users to ask questions about HR policies and receive answers grounded in the uploaded HR Policy Manual.

---

## 🚀 Features

* PDF-based knowledge base
* Text chunking for large documents
* Semantic search using embeddings
* FAISS vector database for retrieval
* Google Gemini integration for answer generation
* Conversation memory for follow-up questions
* Streamlit web interface
* Source page citations

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* Google Gemini
* Sentence Transformers
* FAISS

### Data Processing

* pdfplumber
* NumPy
* Pickle

---

## 📂 Project Structure

```text
HR-Knowledge-Assistant/
│
├── app.py
│
├── data/
│   └── HR-Policy-Manual.pdf
│
├── src/
│   ├── chatbot.py
│   ├── retriever.py
│   ├── embeddings.py
│   ├── vector_db.py
│   ├── pdf_loader.py
│   ├── text_chunker.py
│   
│  
│
│
├── vector_store/
│   ├── chunks.pkl
│   └── hr_policy.index
│
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd HR-Knowledge-Assistant
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

## 💬 Example Questions

* What is the leave policy?
* What is the attendance policy?
* What is the absence policy?
* What employee benefits are available?
* Explain the appraisal policy.
* How often is it conducted?
* What is the recruitment process?

---

## 🧠 Conversation Memory

The assistant supports follow-up questions.

Example:

User:

```text
Explain the appraisal policy.
```

User:

```text
How often is it conducted?
```

The assistant uses previous conversation context to understand that "it" refers to the appraisal policy.

---

## 🔍 Retrieval Pipeline

```text
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS Vector Store
 ↓
Semantic Retrieval
 ↓
Gemini
 ↓
Final Answer
```

---

## 📌 Future Enhancements

* Multi-PDF support
* Role-based access control
* Feedback collection
* Chat history persistence
* Meeting preparation integration
* HR document upload from UI

---


