# /src/user_interface/web_ui_app.py

import sys
import os
import streamlit as st

# Add the parent directory of 'chatbot' to the Python Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user_interface.ui_functions import validate_url, check_robots_txt
from chatbot.chatbot import initialize_chatbot

def main():
    # Set the webpage title
    st.set_page_config(page_title="Web Scraping Assistant!")

    # Create a header element
    st.header("Web Scraping Assistant!")

    # Prompt the user for a web URL
    web_url = st.text_input("Please enter a web URL:")

    # Prompt the user for a topic
    topic = st.text_input("Please enter a topic:")

    # Add a submit button
    if st.button('Submit'):
        # Validate the URL
        if validate_url(web_url):
            st.write("URL is valid.")
        else:
            st.write("URL is invalid.")
            return

        # Check the robots.txt file
        robots_txt = check_robots_txt(web_url) 
        if robots_txt is not None:
            st.write("Contents of robots.txt:")
            st.write(robots_txt)
        else:
            st.write(f"No robots.txt file found at {web_url}")

        # Initialize the chatbot only once when the app starts
        system_prompt = st.text_area(
            label="System Prompt",
            value="You are a helpful AI assistant who answers questions in short sentences.",
            key="system_prompt"
        )
        initialize_chatbot(system_prompt)

if __name__ == '__main__':
    main()
