# \src\user_interface\ui_functions.py

import streamlit as st
import requests
import urllib.parse
from urllib.parse import urlparse
import urllib.robotparser

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def get_user_input_url():
    url = st.text_input("Enter website URL", key="website_url_input")
    return url

def get_website_name(url):
    parsed_url = urlparse(url)
    website_name = parsed_url.netloc
    return website_name

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

