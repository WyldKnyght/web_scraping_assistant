# \src\user_interface\web_ui.py

import sys
import os
import streamlit as st

# Add the parent directory of 'src' to the Python Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user_interface.ui_functions import validate_url, check_robots_txt
from web_scraping.scrape_and_convert_to_markdown import scrape_and_convert_to_markdown
from web_scraping.convert_markdown_to_dataset import convert_markdown_to_dataset

def main():
    # Set the webpage title
    st.set_page_config(page_title="Web Scraping Assistant!")

    # Create a header element
    st.header("Web Scraping Assistant!")

    # Initialize session state for web URL and topic
    if 'web_url' not in st.session_state:
        st.session_state['web_url'] = ''

    # Function to clear the inputs
    def clear_inputs():
        st.session_state['web_url'] = ''

    # Prompt the user for a web URL
    st.session_state['web_url'] = st.text_input("Please enter a web URL:", value=st.session_state['web_url'])

    # Add a submit button
    if st.button('Submit'):
        # Validate the URL
        if validate_url(st.session_state['web_url']):
            st.write("URL is valid.")
        else:
            st.write("URL is invalid.")
            return

        # Check the robots.txt file
        robots_txt = check_robots_txt(st.session_state['web_url']) 
        if robots_txt is not None:
            st.write("Contents of robots.txt:")
            st.write(robots_txt)
        else:
            st.write(f"No robots.txt file found at {st.session_state['web_url']}")

        # Call the web scraping function
        unique_file_name = scrape_and_convert_to_markdown(st.session_state['web_url'])
        st.session_state['unique_file_name'] = unique_file_name

        # Convert the markdown content into a dataset
        convert_markdown_to_dataset(st.session_state['unique_file_name'])

    # Add a reset button
    st.button('Reset', on_click=clear_inputs)

if __name__ == '__main__':
    main()
