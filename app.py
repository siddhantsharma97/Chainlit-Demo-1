import chainlit as cl
from src.llm import ask_bot
from src.config import instruction
@cl.on_message
async def main(message: cl.Message):
    response=ask_bot(message.content,instruction)
    
    await cl.Message(
        content=f"{response}",
    ).send()
