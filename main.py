from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(
    model = 'gpt-4o'
)

ai_message = llm.invoke("hi how are you ?")

print(ai_message.content)