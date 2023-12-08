# \src\common\create_directory.py

import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def create_directory(directory):
    # Create the directory if it doesn't exist
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory: {e}")