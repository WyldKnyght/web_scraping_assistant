# \src\web_scraping\get_website_elements.py

import os
import requests
from bs4 import BeautifulSoup
import logging
from common.unique_filename_manager import UniqueFilenameManager
from common.create_directory import create_directory
from common.save_to_file import save_to_json

# Set up logging
logging.basicConfig(level=logging.INFO)

labels = None


def extract_labels(soup):
    global labels
    labels = [tuple(element.get('class')) for element in soup.find_all() if element.get('class') is not None]
    return list(set(labels))

def get_labels(soup):
    labels = [tuple(element.get('class')) for element in soup.find_all() if element.get('class') is not None]
    return list(set(labels))

def get_unique_elements(url, unique_filename):
    # Log the start of the function
    logging.info(f"Starting get_unique_elements for URL: {url}")
    
    # Send a GET request to the website and get the HTML response
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract labels and unique elements
    labels = extract_labels(soup)

    # Get all the elements on the page
    all_elements = soup.find_all()

    # Create an empty list to store the unique elements
    unique_elements = []

    # Loop through all the elements and check if the element class is already in the list
    for element in all_elements:
        class_name = element.get('class')

        # Check if class_name is not None before processing
        if class_name is not None:
            # If the element class is not in the list, add it and the first element data to the list
            if tuple(class_name) not in set(element[0] for element in unique_elements):
                unique_elements.append((tuple(class_name), element.text))

    # Save the dataset to a JSON file
    website_elements_directory = os.path.join('data', 'scraped_data', 'website_elements')
    create_directory(website_elements_directory)
    website_elements_path = os.path.join(website_elements_directory, f"{unique_filename}.json")

    try:
        with open(website_elements_path, 'w') as f:
            save_to_json(website_elements_path, unique_elements)
    except Exception as e:
        logging.error(f"Failed to save elements to JSON: {e}")

    return labels, unique_elements

    # Log the end of the function
    logging.info(f"Finished get_unique_elements for URL: {url}")