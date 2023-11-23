# /src/chatbot/message_handling.py

import streamlit as st
from chatbot.chatbot import initialize_chatbot

system_prompt = st.text_area(
    label="System Prompt",
    value="You are a helpful AI assistant who answers questions in short sentences.",
    key="system_prompt"
)

llm_chain = initialize_chatbot(system_prompt)

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
    response = llm_chain.invoke({"question": user_prompt})
    append_and_display_message("assistant", response)
