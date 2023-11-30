# \src\user_interface\ui_functions.py

import streamlit as st
import validators
import requests
import urllib.parse
from urllib.parse import urlparse
import urllib.robotparser

def get_web_url(key):
    # Get user input
    website_url = st.text_input("Enter website URL", key=key)
    return website_url

def get_website_name(website_url):
    parsed_url = urlparse(website_url)
    hostname = parsed_url.hostname if parsed_url.hostname else None
    return hostname.replace('www.', '').replace('.com', '') if hostname else None


def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


import urllib.robotparser

def check_robots_txt(url):
    try:
        robots_url = urllib.parse.urljoin(url, "/robots.txt")
        response = requests.get(robots_url)
        if response.status_code == 200:
            # Create a RobotFileParser object
            rp = urllib.robotparser.RobotFileParser()

            # Set the user agent
            rp.set_url(robots_url)
            rp.read()

            # Check if the URL is allowed
            return rp.can_fetch('*', url)
    except Exception as e:
        st.error(f"Error checking robots.txt: {str(e)}")
    return False

