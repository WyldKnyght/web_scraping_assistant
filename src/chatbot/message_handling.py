# /src/chatbot/message_handling.py

import streamlit as st
import logging
from chatbot.chatbot import initialize_chatbot

# Set up logging
logging.basicConfig(level=logging.INFO)

system_prompt = st.text_area(
    label="System Prompt",
    value="You are a helpful AI assistant specialized in providing information related to web scraping.",
    key="system_prompt"
)

try:
    llm_chain = initialize_chatbot(system_prompt)
except Exception as e:
    logging.error(f"Failed to initialize chatbot: {e}")
    st.error("Failed to initialize chatbot. Please try again.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I help you today?"}
    ]

if "current_response" not in st.session_state:
    st.session_state.current_response = ""

def append_and_display_message(role, content):
    st.session_state.messages.append(
        {"role": role, "content": content}
    )
    with st.chat_message(role):
        st.markdown(content)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("Your message here", key="user_input"):
    append_and_display_message("user", user_prompt)
    try:
        response = llm_chain.invoke({"question": user_prompt})
    except Exception as e:
        logging.error(f"Failed to get response from chatbot: {e}")
        st.error("Failed to get response from chatbot. Please try again.")
    append_and_display_message("assistant", response)

    st.session_state.current_response = response