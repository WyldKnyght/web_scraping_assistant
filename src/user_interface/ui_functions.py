# \src\user_interface\ui_functions.py

import streamlit as st
import validators
import requests
import urllib.parse
from urllib.parse import urlparse

def get_web_url(key):
    # Get user input
    website_url = st.text_input("Enter website URL", key=key)
    return website_url

def get_website_name(website_url):
    parsed_url = urlparse(website_url)
    hostname = parsed_url.hostname if parsed_url.hostname else None
    return hostname.replace('www.', '').replace('.com', '') if hostname else None

def validate_url(url):
    if not url:
        st.error("Please enter a URL.")
        return False
    elif validators.url(url):
        return True
    else:
        st.error("Invalid URL. Please enter a valid URL.")
        return False

def check_robots_txt(url):
    try:
        robots_url = urllib.parse.urljoin(url, "/robots.txt")
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        st.error(f"Error checking robots.txt: {str(e)}")
    return None
