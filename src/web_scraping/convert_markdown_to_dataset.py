# \src\web_scraping\convert_markdown_to_dataset.py

import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_markdown_to_dataset():
    # Log the start of the function
    logging.info("Starting convert_markdown_to_dataset")

    # Load the markdown content from the file
    markdown_file_path = os.path.join('data', 'raw_data', 'scraped_content.md')
    try:
        with open(markdown_file_path, 'r') as file:
            markdown_content = file.read()
    except Exception as e:
        logging.error(f"Failed to read markdown content: {e}")
        return

    # Convert the markdown content into a dataset
    try:
        dataset = pd.DataFrame({
            'text': [markdown_content]
        })
    except Exception as e:
        logging.error(f"Failed to create DataFrame: {e}")
        return

    # Save the dataset to a CSV file
    dataset_file_path = os.path.join('data', 'training_data', 'dataset.csv')
    try:
        dataset.to_csv(dataset_file_path, index=False)
    except Exception as e:
        logging.error(f"Failed to save dataset to CSV: {e}")
        return

    # Log the end of the function
    logging.info("Finished convert_markdown_to_dataset")

if __name__ == '__main__':
    convert_markdown_to_dataset()
