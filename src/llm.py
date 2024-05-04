import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

message=[{"role": "system", "content":instruction}]

def ask_bot(user_message):
    messages=[{"role": "system", "content":instruction }, 
            {"role": "user", "content": user_message}]  

    llm = ChatGoogleGenerativeAI(model="gemini-pro")
        
    response = llm.invoke(messages)
    
    return response.content

