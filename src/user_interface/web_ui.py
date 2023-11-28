# \src\user_interface\web_ui.py

import sys
import os
import streamlit as st

# Add the parent directory of 'src' to the Python Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from user_interface.ui_functions import validate_url, check_robots_txt, get_web_url
from web_scraping.scrape_and_convert_to_markdown import scrape_and_convert_to_markdown
from web_scraping.convert_markdown_to_dataset import convert_markdown_to_dataset

def main():
    # Set the webpage title
    st.set_page_config(page_title="Web Scraping Assistant!")

    # Create a header element
    st.header("Web Scraping Assistant!")

    # Create a form
    with st.form(key="my_form", clear_on_submit=True):
        # Get the URL from the user
        url = st.text_input("Enter website URL", key="website_url_input")

        # Add a submit button
        submitted = st.form_submit_button('Submit')

        if submitted:
            if validate_url(url):
                # Check robots.txt
                robots_txt = check_robots_txt(url)
                st.write(f"Robots.txt: {robots_txt}")

                # Scrape and convert to markdown
                unique_file_name = scrape_and_convert_to_markdown(url)
                if unique_file_name:
                    st.success(f"Markdown file created: {unique_file_name}.md")

                    # Convert markdown to dataset
                    convert_markdown_to_dataset(unique_file_name, url) # Pass the url as an argument
                    st.success(f"CSV dataset file created: {unique_file_name}.csv")
                else:
                    st.error("Failed to scrape and convert to markdown.")

            else:
                st.error("Invalid URL. Please enter a valid URL.")

    # Reset button
    if st.button('Reset'):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
