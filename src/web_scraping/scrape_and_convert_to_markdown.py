# \src\web_scraping\scrape_and_convert_to_markdown.py

import requests
import os
import logging
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import AsyncHtmlLoader
from common.file_handling import save_to_file, find_unique_file_name
from user_interface.ui_functions import get_website_name
from transformers import pipeline
import urllib.robotparser

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the NER model
ner_model = pipeline("ner")

def scrape_and_convert_to_markdown(url):
    # Log the start of the function
    logging.info("Starting scrape_and_convert_to_markdown")

    # Check if the URL is allowed by the robots.txt file
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(url)
    rp.read()
    if not rp.can_fetch('*', url):
        logging.error(f"URL is not allowed by robots.txt: {url}")
        return

    # Fetch HTML content from the website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error(f"HTTP Error: {errh}")
        return
    except requests.exceptions.ConnectionError as errc:
        logging.error(f"Error Connecting: {errc}")
        return
    except requests.exceptions.Timeout as errt:
        logging.error(f"Timeout Error: {errt}")
        return
    except requests.exceptions.RequestException as err:
        logging.error(f"Something went wrong: {err}")
        return

    # Convert HTML to Markdown using html2text
    urls = [url]
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    html2text_transformer = Html2TextTransformer()
    docs_transformed = html2text_transformer.transform_documents(docs)

    # Assign the transformed text to the 'transformed_text' variable
    transformed_text = "\n".join(doc.page_content for doc in docs_transformed)

    # Use the NER model to extract entities from the transformed text
    entities = ner_model(transformed_text)
    
    # Get the website name
    website_name = get_website_name(url)

    # Save the markdown content to a file with .md extension
    try:
        unique_file_name = find_unique_file_name('data/raw_data', website_name)
        save_to_file(os.path.join('data', 'raw_data', unique_file_name + ".md"), transformed_text + "\n\n" + str(entities))
    except Exception as e:
        logging.error(f"Failed to save markdown file: {e}")
        return

    # Log the end of the function
    logging.info("Finished scrape_and_convert_to_markdown")
    
    return unique_file_name
