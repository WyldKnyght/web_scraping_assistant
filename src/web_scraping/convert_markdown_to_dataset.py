# \src\web_scraping\convert_markdown_to_dataset.py

import os
import sys
import pandas as pd
import logging
from common.file_handling import find_unique_file_name
from .scrape_and_convert_to_markdown import scrape_and_convert_to_markdown

# Add the parent directory of 'src' to the Python Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from common.file_handling import save_to_file, find_unique_file_name
from user_interface.ui_functions import get_web_url, get_website_name

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_markdown_to_dataset(unique_file_name):
    # Log the start of the function
    logging.info("Starting convert_markdown_to_dataset")

    # Get the website name
    website_name = get_website_name(get_web_url()) 

    # Load the markdown content from the file
    markdown_file_path = os.path.join('data', 'raw_data', unique_file_name + '.md')

    with open(markdown_file_path, 'r') as file:
        markdown_content = file.read()

    # Convert the markdown content into a dataset
    try:
        dataset = pd.DataFrame({
            'text': [markdown_content]
        })
    except Exception as e:
        logging.error(f"Failed to create DataFrame: {e}")
        return

    # Save the dataset to a CSV file using the save_text_to_file function
    dataset_file_directory = os.path.join('data', 'training_data')
    dataset_file_name = unique_file_name # Use the same file name as the Markdown file
    dataset_file_path = os.path.join(dataset_file_directory, dataset_file_name + '.csv')

    try:
        save_to_file(dataset_file_path, dataset.to_csv(index=False))
    except Exception as e:
        logging.error(f"Failed to save dataset to CSV: {e}")
        return

    # Log the end of the function
    logging.info("Finished convert_markdown_to_dataset")

if __name__ == '__main__':
    url = get_web_url()
    unique_file_name = scrape_and_convert_to_markdown(url)
    convert_markdown_to_dataset(unique_file_name)

