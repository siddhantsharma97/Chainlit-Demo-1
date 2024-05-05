import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

message=[{"role": "system", "content":instruction}]

def ask_bot(user_message,instruction):
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    
    
    respones=model(
    [
        SystemMessage(content=instruction),
        HumanMessage(content=user_message),
    ]
)
    
    return respones.content

