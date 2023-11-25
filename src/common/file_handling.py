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

def find_unique_file_name(directory, website_name):
    # Find a unique file name
    file_name = f"{website_name}-1.txt"
    i = 1
    while os.path.exists(os.path.join(directory, file_name)):
        i += 1
        file_name = f"{website_name}-{i}.txt"
    return file_name

def save_text_to_file(file_path, text):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        logging.info(f"Text saved to file {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save text to file: {e}")
