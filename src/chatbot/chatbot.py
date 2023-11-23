# /src/chatbot/chatbot.py

from model_handler.model_handler import create_model_chain
from langchain.callbacks.base import BaseCallbackHandler

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

def initialize_chatbot(system_prompt):
    llm_chain = create_model_chain(system_prompt)
    return llm_chain
