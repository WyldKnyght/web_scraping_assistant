# \src\web_scraping\convert_markdown_to_dataset.py

import os
import pandas as pd
import logging
from common.file_handling import save_to_csv
from web_scraping.text_classification import TextClassifier

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_markdown_to_dataset(unique_filename, url):
    # Log the start of the function
    logging.info("Starting convert_markdown_to_dataset")

    # Load the markdown content from the file
    markdown_file_path = os.path.join('data', 'raw_data', unique_filename + '.md')

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

    # Create an instance of the TextClassifier class
    classifier = TextClassifier(str(), unique_filename)

    # Classify the content
    categories = classifier.predict(markdown_content)

    # Add the categories to the dataset
    dataset['categories'] = categories

    # Save the dataset to a CSV file using the save_to_csv function
    dataset_file_directory = os.path.join('data', 'training_data')
    dataset_file_path = os.path.join(dataset_file_directory, unique_filename + '.csv')

    try:
        save_to_csv(dataset_file_path, dataset.to_csv(index=False))
    except Exception as e:
        logging.error(f"Failed to save dataset to CSV: {e}")
        return

    # Log the end of the function
    print("Finished convert_markdown_to_dataset")
    logging.info("Finished convert_markdown_to_dataset")
