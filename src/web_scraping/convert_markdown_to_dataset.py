# \src\web_scraping\convert_markdown_to_dataset.py

import os
import sys
import pandas as pd
import logging
import model_handler.model_handler as llm_chain
from common.file_handling import save_to_file
from model_handler.text_classification import TextClassifier

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_markdown_to_dataset(unique_file_name, url):
    # Log the start of the function
    logging.info("Starting convert_markdown_to_dataset")

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

    # Create an instance of the TextClassifier class
    classifier = TextClassifier(str(llm_chain))

    # Classify the content
    categories = classifier.predict(markdown_content)

    # Add the categories to the dataset
    dataset['categories'] = categories

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
    print("Finished convert_markdown_to_dataset")
    logging.info("Finished convert_markdown_to_dataset")
