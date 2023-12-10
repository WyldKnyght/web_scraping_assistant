# \src\web_scraping\get_labels.py

import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def extract_labels(soup):
    labels = [tuple(element.get('class')) for element in soup.find_all() if element.get('class') is not None]
    return list(set(labels))

def get_labels(soup):
    labels = [tuple(element.get('class')) for element in soup.find_all() if element.get('class') is not None]
    return list(set(labels))
