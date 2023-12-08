# \src\user_interface\web_ui.py

import logging
import streamlit as st
from user_interface.ui_functions.validate_url import validate_url
from user_interface.ui_functions.check_robots import check_robots_txt
from web_scraping.scrape_html import scrape_html
from web_scraping.convert_html_to_markdown import convert_to_markdown
from web_scraping.convert_markdown_to_dataset import convert_markdown_to_dataset
from web_scraping.analyze_website_structure import analyze_website_structure
from web_scraping.get_website_elements import get_unique_elements
from common.unique_filename_manager import UniqueFilenameManager 

def run_web_app():
    logging.basicConfig(level=logging.INFO)
    st.set_page_config(page_title="Web Scraping Assistant!")
    st.header("Web Scraping Assistant!")
    st.write("Welcome to the Web Scraping Assistant! Enter a URL and let the tool do the rest.")

    # Define the form using st.form()
    with st.form(key='my_form'):
        # Get URL from user input using the function
        url_from_user = st.text_input('Enter URL', '')

        # Use st.form_submit_button() inside the form block
        form_submitted = st.form_submit_button('Submit')

        if form_submitted:
            handle_submitted_form(url_from_user)

    handle_reset_button()
    
def handle_submitted_form(url):
    # Validate URL
    if validate_url(url):
        st.success("Valid URL!")
        process_valid_url(url)
    else:
        st.error("Invalid URL. Please enter a valid URL.")

def process_valid_url(url):
    # Check robots.txt 
    if check_robots_txt(url):
        st.success("robots.txt check: PASSED")
    else:
        st.error("robots.txt check: FAILED")

    # Set the unique filename
    unique_filename = UniqueFilenameManager.find_unique_file_name(url)

    # Analyze website structure
    if analyze_website_structure(url):
        st.success("Website structure analysis: PASSED")
    else:
        st.error("Website structure analysis: FAILED")

    # Get unique elements
    if get_unique_elements(url, unique_filename):
        st.success("Get unique elements: PASSED")
    else:
        st.error("Get unique elements: FAILED")

    # Scrape HTML
    html_content = scrape_html(url, unique_filename)
    if html_content is not None:
        st.success("Scrape HTML: PASSED")  
    else:
        st.error("Scrape HTML: FAILED")
 
    # Convert HTML to Markdown
    markdown_content = convert_to_markdown(html_content, unique_filename)
    if markdown_content:
        st.success("Convert HTML to Markdown: PASSED")
    else:
        st.error("Convert HTML to Markdown: FAILED")

    # Convert Markdown to CSV
    if convert_markdown_to_dataset(url, unique_filename, markdown_content):
        st.success("Convert Markdown to CSV: PASSED")
    else:
        st.error("Convert Markdown to CSV: FAILED")

def handle_reset_button():
    if st.button('Reset'):
        st.experimental_rerun()
