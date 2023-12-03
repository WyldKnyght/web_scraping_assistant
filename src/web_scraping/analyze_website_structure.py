# \src\web_scraping\analyze_website_structure.py

import requests
import logging
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO)

def analyze_website_structure(url):
    try:
        # Static scraping using BeautifulSoup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if JavaScript or AJAX elements are present
        if soup.find_all('script') or 'ajax' in str(response.content):
            result = 'Dynamic (Use Selenium or similar tools)'
        else:
            result = 'Static (Use BeautifulSoup)'

    except Exception as e:
        result = 'Failed to analyze structure'
        logging.error(f"Failed to analyze structure: {e}")

    # Log the end of the function
    logging.info(f"Finished analyze_website_structure: {result}")
    return result
