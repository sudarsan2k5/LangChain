from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(
    model = 'gpt-4o'
)

system_message = SystemMessage("You are motivational gym assistant")
user_message = HumanMessage("suggest me 1 best exercise for back")


message = [system_message, user_message]
ai_message = llm.invoke(message)

print(ai_message.content)