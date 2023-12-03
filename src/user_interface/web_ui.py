# \src\user_interface\web_ui.py

import os
import logging
from langchain.document_loaders import web_base
import streamlit as st
from user_interface.ui_functions import validate_url, check_robots_txt, get_user_input_url
from web_scraping.scrape_and_convert_to_markdown import scrape_and_convert_to_markdown
from web_scraping.convert_markdown_to_dataset import convert_markdown_to_dataset
from web_scraping.analyze_website_structure import analyze_website_structure
from web_scraping.get_website_elements import get_unique_elements

def run_web_app():
    logging.basicConfig(level=logging.INFO)

    # Set the webpage title in the main script
    st.set_page_config(page_title="Web Scraping Assistant!")

    url_from_user = get_user_input_url()
    # Create a header element
    st.header("Web Scraping Assistant!")

    # Short introduction
    st.write("Welcome to the Web Scraping Assistant! Enter a URL and let the tool do the rest.")

    # Create a form
    with st.form(key="my_form", clear_on_submit=True):
        # Use the URL obtained from the user
        url = url_from_user

        # Add a submit button
        submitted = st.form_submit_button('Submit')

        if submitted:
            if validate_url(url):
                # Check robots.txt
                robots_txt = check_robots_txt(url)
                st.write(f"Robots.txt: {robots_txt}")

                # Analyze website structure
                analyze_website_structure(url)

                # Get Website Elements
                unique_elements = get_unique_elements(url)
                if unique_elements:
                    st.success(f"Unique Elements added to DB: {unique_elements}")

                # After extracting unique elements, extract labels
                unique_elements = get_unique_elements(url)
                labels = [label[0] for label in unique_elements]


                # Scrape and convert to markdown
                unique_name = scrape_and_convert_to_markdown(url, labels)
                if unique_name:
                    st.success(f"Markdown file created: {unique_name}.md")

                    # Convert markdown to dataset
                    convert_markdown_to_dataset(unique_name, url)  # Pass the URL as an argument
                    st.success(f"CSV dataset file created: {unique_name}.csv")
                else:
                    st.error("Failed to scrape and convert to markdown.")
            else:
                st.error("Invalid URL. Please enter a valid URL.")

    # Reset button
    if st.button('Reset'):
        st.experimental_rerun()

    # Add a download button for the CSV file
    if 'unique_name' in locals():
        csv_file_path = os.path.join('data', 'training_data', f"{unique_name}.csv")
        if os.path.exists(csv_file_path):
            with open(csv_file_path, 'rb') as file:
                st.download_button(
                    label="Download CSV",
                    data=file.read(),
                    file_name=f"{unique_name}.csv",
                    mime="text/csv"
                )
        else:
            st.warning("CSV file not found.")
            
    return url_from_user
