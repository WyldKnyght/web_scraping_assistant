# \src\user_interface\ui_functions\check_robots.py

import streamlit as st
import requests
import urllib.parse
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