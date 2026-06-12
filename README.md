# 🎓 Department FAQ Bot

> An AI-powered Retrieval-Augmented Generation (RAG) chatbot. Get instant, accurate answers to all your college-related queries — from departments and admissions to campus life and placements.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Adding Knowledge Documents](#adding-knowledge-documents)
  - [Vectorizing Documents](#vectorizing-documents)
  - [Running the App](#running-the-app)
- [Configuration](#configuration)
- [Pages & Navigation](#pages--navigation)
- [Architecture](#architecture)
- [License](#license)

---

## Overview

The **FAQ Bot** is a multi-page Streamlit web application that leverages **Retrieval-Augmented Generation (RAG)** to answer frequently asked questions about Sri Eshwar College of Engineering. The bot ingests college PDF documents (brochures, handbooks, department info, etc.), stores them in a vector database, and uses a LLM (Groq's LLaMA 3.1) to generate contextually accurate answers grounded in real college data.

The app features:
- A **landing/home page** with college information, stats, accreditations, and campus life highlights.
- A **Departments page** with detailed information about all engineering departments.
- A **Chatbot page** powered by RAG for interactive Q&A.

---

## Features

- 🤖 **RAG-Powered Chatbot** — Answers are grounded in real PDF documents from the college, not hallucinated.
- 🏛️ **Multi-Department Coverage** — Explore details for all engineering departments at SECE.
- 📄 **PDF Knowledge Ingestion** — Add any college PDF documents and the bot learns from them automatically.
- 💬 **Conversational Memory** — The chatbot remembers the conversation history for contextual follow-ups.
- 🎨 **Premium Dark UI** — Glassmorphism design with animated hero, gradient text, and smooth hover effects.
- ⚙️ **Customizable Prompts** — System and negative prompts are configurable from the settings sidebar.
- 📤 **PDF Export** — Export chat responses as PDF files.
- 🔒 **Scoped Responses** — The bot strictly responds only to college-related queries.

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) 1.38.0 |
| **LLM** | [Groq](https://groq.com/) — `llama-3.1-8b-instant` |
| **Embeddings** | [HuggingFace Embeddings](https://huggingface.co/) (default `all-MiniLM-L6-v2`) |
| **Vector Store** | [ChromaDB](https://www.trychroma.com/) (persisted locally) |
| **RAG Framework** | [LangChain](https://www.langchain.com/) |
| **PDF Parsing** | PyPDF2, Pytesseract (OCR fallback) |
| **PDF Export** | fpdf2 |
| **Text Splitting** | LangChain `RecursiveCharacterTextSplitter` |
| **Fonts** | Google Fonts — Inter & Outfit |

---

## Project Structure

```
College_RAG_Chatbot/
│
├── main.py                    # Home / landing page (Streamlit entrypoint)
├── app.py                     # App configuration / helpers
├── rag.py                     # RAG chain setup (vectorstore + LLM + memory)
├── vectorize_documents.py     # Script to ingest PDFs and build vector DB
├── prompts.py                 # Default system & negative prompt templates
├── sidebar.py                 # Shared sidebar component
├── settings.py                # Settings/config loader
├── utils.py                   # Utility functions
├── pdf_export.py              # PDF export functionality
├── config.py                  # Config file parser
├── config.json                # API keys and settings (gitignored)
│
├── pages/
│   ├── 1_🏛️_Departments.py    # Departments info page
│   └── 2_🤖_Chatbot.py        # RAG chatbot page
│
├── data/                      # 📂 Place your college PDF documents here
├── vector_db_dir/             # 🗄️ Chroma vector DB (auto-generated)
├── images/                    # Static image assets
│
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- **Python 3.9+**
- **[Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)** installed at `C:\Program Files\Tesseract-OCR\tesseract.exe` (Windows). Required only for image-based PDFs.
- A **[Groq API Key](https://console.groq.com/)** (free tier available).

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd College_RAG_Chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**

   Create (or edit) `config.json` in the project root:
   ```json
   {
     "GROQ_API_KEY": "your_groq_api_key_here"
   }
   ```

---

### Adding Knowledge Documents

Place your college PDF files (department handbooks, brochures, fee structures, syllabi, placement reports, etc.) inside the `data/` directory:

```
data/
├── sece_departments.pdf
├── admission_handbook.pdf
├── placement_report_2024.pdf
└── ...
```

---

### Vectorizing Documents

Run the ingestion script **once** (or whenever you add/update PDFs) to build the vector database:

```bash
python vectorize_documents.py
```

This will:
1. Load all `.pdf` files from `data/`.
2. Extract text (with OCR fallback via Tesseract for scanned PDFs).
3. Split text into overlapping chunks (2000 chars, 500 overlap).
4. Generate embeddings using HuggingFace.
5. Persist the Chroma vector DB to `vector_db_dir/`.

---

### Running the App

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Configuration

The app reads settings from `config.json`:

```json
{
  "GROQ_API_KEY": "your_groq_api_key_here"
}
```

> ⚠️ **Never commit `config.json` to version control.** It is already listed in `.gitignore`.

You can also customize the chatbot's **system prompt** and **negative prompt** directly from the sidebar within the app at runtime.

---

## Pages & Navigation

| Page | Route | Description |
|---|---|---|
| 🏠 Home | `main.py` | College overview, stats, accreditations, campus life |
| 🏛️ Departments | `pages/1_🏛️_Departments.py` | Detailed info on all engineering departments |
| 🤖 Chatbot | `pages/2_🤖_Chatbot.py` | Interactive RAG-powered FAQ chatbot |

Navigate using the **sidebar** or the **CTA buttons** on the home page.

---

## Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────┐
│         Streamlit Frontend          │
│  (main.py / Departments / Chatbot)  │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│        LangChain RAG Pipeline       │
│                                     │
│  1. Query → HuggingFace Embeddings  │
│  2. Similarity Search → ChromaDB    │
│  3. Top-K Chunks Retrieved          │
│  4. Prompt + Context + History →    │
│     Groq LLaMA 3.1 (8B Instant)     │
│  5. Grounded Answer Generated       │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│         ChromaDB Vector Store       │
│  (persisted in vector_db_dir/)      │
│  built from PDFs in data/           │
└─────────────────────────────────────┘
```

**RAG Flow:**
1. **Ingestion** — PDFs are parsed, chunked, embedded, and stored in ChromaDB.
2. **Retrieval** — On each query, the top 3 most relevant chunks are retrieved via similarity search.
3. **Generation** — The retrieved context, conversation history, and user question are passed to the Groq LLM, which generates a grounded, contextual response.

---


