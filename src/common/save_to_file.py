# \src\common\save_to_file.py

import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def setup_logging():
    return logging.getLogger(__name__)

logger = setup_logging()

def save_to_html(file_path, html):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html)
        logger.info(f"Content saved to HTML file {file_path} successfully.")
    except Exception as e:
        logger.error(f"Failed to save content to HTML file: {e}")
        raise
       
def save_to_text(file_path, text):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        logger.info(f"Content saved to text file {file_path} successfully.")
    except Exception as e:
        logger.error(f"Failed to save content to text file: {e}")
        raise

def save_to_csv(file_path, content):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logger.info(f"Content saved to CSV {file_path} successfully.")
    except Exception as e:
        logger.error(f"Failed to save content to CSV file: {e}")
        raise

def save_to_json(file_path, data):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if hasattr(data, 'read'):
            # If data is a file-like object, read it and then dump to JSON
            data = data.read()

        if isinstance(data, (str, bytes, os.PathLike)):
            # If data is already a string or bytes, write it directly
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(data)
        else:
            # Otherwise, assume it is a Python object and dump it to JSON
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        logging.info(f"Content saved to JSON file {file_path} successfully.")
    except Exception as e:
        logging.error(f"Failed to save content to JSON file: {e}")
        raise
