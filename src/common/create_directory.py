# \src\common\create_directory.py

import os
import logging

def create_directory(directory):
    """
    Create the directory and its parent directories if they don't exist.

    Args:
        directory (str): The path of the directory to be created.

    Returns:
        None
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory: {e}")
        raise
