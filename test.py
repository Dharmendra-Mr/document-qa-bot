from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

response = llm.invoke("Say hello")

print(response.content)