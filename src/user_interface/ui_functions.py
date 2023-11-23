# /src/user_interface/ui_functions.py

import streamlit as st
from common.file_handling import save_text_to_file
import validators
import requests
import urllib.parse

def get_web_url():
    # Get user input
    website_url = st.text_input("Enter website URL", "https://example.com")
    scrape_text = st.checkbox("Scrape text", value=True)
    return website_url, scrape_text

def get_main_topic():
    # Get the main topic (label) from the user
    return st.text_input("Add a main topic (label):")

def validate_url(url):
    return validators.url(url)

def check_robots_txt(url):
    try:
        robots_url = urllib.parse.urljoin(url, "/robots.txt")
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        st.error(f"Error checking robots.txt: {str(e)}")
    return None

def trigger_scraping(website_url, scrape_text, main_topic, main_topic_directory):
    # Add a button to trigger scraping
    if st.button("Scrape Data"):
        st.session_state.messages.append(
            {"role": "assistant", "content": "Let me fetch the data for you..."}
        )

        # Call your web scraping functions here
        # scraped_data_path = scraper.scrape_and_save_data(website_url, scrape_text)
        # TODO Modify this part to perform your actual scraping logic
        # For now, let's display a test message
        st.success("Scraped Data Test Done")
       

        # Save the main topic, you can use the save_text_to_file function
        main_topic_file_path = save_text_to_file(main_topic_directory, main_topic)
        st.session_state.messages.append(
            {"role": "assistant", "content": f"Main topic saved to {main_topic_file_path}"}
        )

        # Display the scraped data using Streamlit elements
        st.text("Display scraped data here") # You can modify this to show the actual scraped data
