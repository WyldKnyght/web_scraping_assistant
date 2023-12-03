# \src\web_scraping\scrape_and_convert_to_markdown.py

import logging
import os
import requests
import urllib.robotparser
from common.file_handling import save_to_file
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import AsyncHtmlLoader
from model_handler.text_classification import TextClassifier
from model_handler.model_handler import llm_chain
from user_interface.ui_functions import unique_file_name   

# Set up logging
logging.basicConfig(level=logging.INFO)

def scrape_and_convert_to_markdown(url, labels):
    # Log the start of the function
    logging.info("Starting scrape_and_convert_to_markdown")

    try:
        # Check if the URL is allowed by the robots.txt file
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(url)
        rp.read()
        if not rp.can_fetch('*', url):
            logging.error(f"URL is not allowed by robots.txt: {url}")
            return None

        # Fetch HTML content from the website
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Convert HTML to Markdown using html2text
        urls = [url]
        loader = AsyncHtmlLoader(urls)
        docs = loader.load()
        html2text_transformer = Html2TextTransformer()
        docs_transformed = html2text_transformer.transform_documents(docs)

        # Assign the transformed text to the 'transformed_text' variable
        transformed_text = "\n".join(doc.page_content for doc in docs_transformed)

    # Use the TextClassifier to classify the transformed text
    classifier = TextClassifier(llm_chain)

    # Train the classifier with the extracted labels
    classifier.train(transformed_text, labels)

    # Predict the class
    predicted_class = classifier.predict(transformed_text)

    if predicted_class is not None:
        # Save the markdown content to a file with .md extension
        unique_name = unique_file_name(url)
        save_to_file(os.path.join('data', 'raw_data', unique_name + ".md"), transformed_text + "\n\n" + str(predicted_class))
        return unique_name
    else:
        print("Failed to predict class.")
        logging.error("Failed to predict class.")
        return None