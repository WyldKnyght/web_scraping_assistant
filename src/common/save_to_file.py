

import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def setup_logging():
    return logging.getLogger(__name__)

logger = setup_logging()

def save_to_file(file_path, content, file_extension):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            if file_extension.lower() == 'json':
                json.dump(content, file, ensure_ascii=False, indent=4)
            else:
                # Explicitly handle Markdown content as plain text
                file.write(content)

            logger.info(f"Content saved to {file_extension.upper()} file {file_path} successfully.")
    except Exception as e:
        logger.error(f"Failed to save content to {file_extension.upper()} file: {e}")
        raise
