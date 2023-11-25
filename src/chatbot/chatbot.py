# /src/chatbot/chatbot.py

import logging
from model_handler.model_handler import create_model_chain
from langchain.callbacks.base import BaseCallbackHandler

class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)

    def handle_user_input(self, user_input):
        # Handle user input
        pass

    def handle_assistant_response(self, assistant_response):
        # Handle assistant response
        pass

    def handle_error(self, error):
        # Handle error
        pass

def initialize_chatbot(system_prompt):
    try:
        llm_chain = create_model_chain(system_prompt)
    except Exception as e:
        logging.error(f"Failed to initialize chatbot: {e}")
        return
    return llm_chain

def handle_chatbot_interaction(user_input, llm_chain):
    try:
        response = llm_chain.invoke({"question": user_input})
    except Exception as e:
        logging.error(f"Failed to get response from chatbot: {e}")
        return None
    return response