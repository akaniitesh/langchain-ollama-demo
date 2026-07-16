# LangChain + Ollama + Streamlit Chat Application

A simple Generative AI application built using **LangChain**, **Ollama**, **Gemma 4**, and **Streamlit**. The application allows users to ask questions through a web interface while running the Large Language Model locally using Ollama.

---

## Features

- Local LLM inference using Ollama
- Gemma 4 (12B) model
- LangChain Prompt Templates
- Streamlit-based web interface
- LangSmith tracing support (optional)
- Environment variable management using `.env`

---

## Tech Stack

- Python
- LangChain
- Ollama
- Gemma 4
- Streamlit
- python-dotenv

---

## Project Structure

```
OLLAMA/
│
├── .venv/
├── .env
├── .env.example
├── .gitignore
├── app.py
├── requirements.txt
├── README.md
└── demo.ipynb
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/langchain-ollama-demo.git

cd langchain-ollama-demo
```

---

### Create Virtual Environment

Using **uv**

```bash
uv venv
```

Activate

Windows CMD

```cmd
.venv\Scripts\activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama

https://ollama.com/download

Verify Installation

```bash
ollama --version
```

---

## Download Gemma Model

```bash
ollama pull gemma4:12b
```

Verify

```bash
ollama list
```

---

## Environment Variables

Create a `.env` file.

Example

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=LangChain-Ollama-Demo
LANGCHAIN_TRACING_V2=true
```

If you don't use LangSmith, you can leave these variables empty.

---

## Run Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

## Sample UI

- Ask any question
- LangChain creates the prompt
- Ollama runs Gemma locally
- Response is displayed in Streamlit

---

## Requirements

- Python 3.10+
- Ollama Installed
- Gemma4:12b Downloaded

---

## Future Improvements

- Chat History
- Conversation Memory
- RAG with Vector Database
- PDF Question Answering
- Multiple Local Models
- Streaming Responses

---

## Author

Nitesh Kumar