# \src\web_scraping\get_website_elements.py

import os
import requests
import json
from bs4 import BeautifulSoup
import logging
from common.create_directory import create_directory
from common.save_to_file import save_to_file
from .get_labels import get_labels

# Set up logging
logging.basicConfig(level=logging.INFO)

# Function to extract information from HTML and create a list of dictionaries
def extract_html_info(element):
    tag_name = element.name
    attributes = dict(element.attrs)
    sub_elements = [extract_html_info(sub_elem) for sub_elem in element.find_all(recursive=False)]
    return {'tag_name': tag_name, 'attributes': attributes, 'sub_elements': sub_elements}

# Function to write data to a file
def write_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def get_unique_elements(url, unique_filename):
    # Send a GET request to the website and get the HTML response
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract labels and unique elements
    labels = get_labels(soup)

    # Extract information from HTML
    extracted_data = [extract_html_info(top_level_element) for top_level_element in soup.find_all(recursive=False)]

    # Write data to a file
    website_elements_directory = os.path.join('data', 'scraped_data', 'website_elements')
    create_directory(website_elements_directory)
    website_elements_path = os.path.join(website_elements_directory, f"{unique_filename}.json")
    
    # Save extracted_data to JSON file using the new function
    save_to_file(website_elements_path, extracted_data, 'json')

    return labels, extracted_data
