import os
from dotenv import load_dotenv

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env
load_dotenv()

# LangSmith (optional)
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain + Ollama (Gemma 4)")

input_text = st.text_input("Ask your question")

# LLM
llm = OllamaLLM(model="gemma4:12b")

# Chain
chain = prompt | llm | StrOutputParser()

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)