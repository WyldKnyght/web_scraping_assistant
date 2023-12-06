# \src\user_interface\web_ui.py

import logging
import streamlit as st
from user_interface.ui_functions import validate_url, check_robots_txt, unique_file_name
from web_scraping.scrape_html import scrape_html
from web_scraping.convert_html_to_markdown import convert_to_markdown
from web_scraping.convert_markdown_to_dataset import convert_markdown_to_dataset
from web_scraping.analyze_website_structure import analyze_website_structure
from web_scraping.get_website_elements import get_unique_elements

def handle_submitted_form(url):
    if validate_url(url):
        process_valid_url(url)
    else:
        st.error("Invalid URL. Please enter a valid URL.")

def process_valid_url(url):
    robots_txt = check_robots_txt(url)
    st.write(f"Robots.txt: {robots_txt}")
    unique_name = unique_file_name(url)

    analyze_website_structure(url)

    unique_elements = get_unique_elements(url)
    if unique_elements:
        st.success(f"Unique Elements added to DB: {unique_elements}")

    labels = [label[0] for label in unique_elements]

    html_content = scrape_html(url)  # Use the new scraping module
    markdown_content = convert_to_markdown(html_content, labels)

    if unique_name:
        st.success(f"Markdown file created: {unique_name}.md")
        convert_markdown_to_dataset(unique_name, markdown_content, url)
        st.success(f"CSV dataset file created: {unique_name}.csv")
    else:
        st.error("Failed to scrape and convert to markdown.")

def handle_reset_button():
    if st.button('Reset'):
        st.experimental_rerun()

def run_web_app():
    logging.basicConfig(level=logging.INFO)
    st.set_page_config(page_title="Web Scraping Assistant!")
    st.header("Web Scraping Assistant!")
    st.write("Welcome to the Web Scraping Assistant! Enter a URL and let the tool do the rest.")

    # Get URL from user input
    url_from_user = st.text_input('Enter URL', 'https://')

    with st.form(key="my_form", clear_on_submit=True):
        url = url_from_user
        submitted = st.form_submit_button('Submit')
        if submitted:
            handle_submitted_form(url)

    handle_reset_button()
    return url_from_user
