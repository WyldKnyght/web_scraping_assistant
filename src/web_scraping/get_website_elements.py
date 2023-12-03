# \src\web_scraping\get_website_elements.py

import os
import requests
from bs4 import BeautifulSoup
import logging
from common.file_handling import create_directory, save_to_json, find_unique_file_name

# Set up logging
logging.basicConfig(level=logging.INFO)

def extract_labels(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    labels = [tuple(element.get('class')) for element in soup.find_all() if element.get('class') is not None]
    return list(set(labels))  # Return unique labels

def get_unique_elements(url):
    labels, unique_elements = extract_labels_and_elements(url)

    # Send a GET request to the website and get the HTML response
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

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
    website_elements_file_directory = os.path.join('data', 'raw_data', 'web_site_elements')
    create_directory(website_elements_file_directory)
    website_elements_file_name = find_unique_file_name(url, labels)
    website_elements_file_path = os.path.join(website_elements_file_directory, website_elements_file_name + '.json')

    try:
        save_to_json(website_elements_file_path, unique_elements)
    except Exception as e:
        logging.error(f"Failed to save elements to JSON: {e}")

    # Log the end of the function
    logging.info("Finished gathering elements")
    return labels, unique_elements
