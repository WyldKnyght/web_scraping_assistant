#\src\common\file_handling.py

import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def create_directory(directory):
    # Create the directory if it doesn't exist
    try:
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Directory {directory} created successfully.")
    except Exception as e:
        logging.error(f"Failed to create directory: {e}")

def find_unique_filename_from_url(directory, base_name):
    unique_filename = base_name
    counter = 1

    while os.path.exists(os.path.join(directory, f"{unique_filename}.md")):
        if counter > 1:
            # If it's not the first iteration, append the counter to the base name
            unique_filename = f"{base_name}-{counter}"

        logging.info(f"Checking for file {unique_filename}.md")
        counter += 1

    logging.info(f"Unique file name found: {unique_filename}")
    return unique_filename

def save_to_csv(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Content saved to CSV {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save content to CSV: {e}")

def save_text_to_file(file_path, text):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        logging.info(f"Text saved to file {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save text to file: {e}")
        
def save_to_json(file_path, json):
    try:
        with open(file_path, 'w') as json_file:
            json_file.write(json)
        logging.info(f"Data saved to JSON file {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save json to file: {e}")

def save_to_html(file_path, html):
    try:
        with open(file_path, 'w') as html:
            html.write(html)
        logging.info(f"Data saved to HTML file {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save HTML to file: {e}")
