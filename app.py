import chainlit as cl
from src.llm import ask_bot

@cl.on_message
async def main(message: cl.Message):
    response=ask_bot(message.content)
    
    await cl.Message(
        content=f"{response}",
    ).send()
