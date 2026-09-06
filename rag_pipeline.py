```python
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()


def build_rag():
    # Load HR knowledge
    try:
        with open("hr_knowledge.txt", "r", encoding="utf-8") as file:
            knowledge = file.read()
    except FileNotFoundError:
        knowledge = "No HR knowledge base found."

    # Get Groq API key
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add GROQ_API_KEY in Render Environment Variables."
        )

    # Create Groq LLM
    llm = ChatGroq(
        api_key=groq_api_key,
        model="llama-3.1-8b-instant",
        temperature=0
    )

    return knowledge, llm
```
