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

def find_unique_file_name(directory, base_name):
    file_name = base_name
    counter = 1

    while os.path.exists(os.path.join(directory, f"{file_name}.md")):
        file_name = f"{base_name}-{counter}"
        counter += 1
        logging.info(f"Checking for file {file_name}.md")

    logging.info(f"Unique file name found: {file_name}")
    return file_name

def save_to_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Content saved to file {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save content to file: {e}")
