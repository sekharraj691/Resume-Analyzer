from langchain_groq import ChatGroq
import os

from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def build_rag():

    with open("hr_knowledge.txt", "r", encoding="utf-8") as file:
        knowledge = file.read()

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant"
    )

    return knowledge, llm