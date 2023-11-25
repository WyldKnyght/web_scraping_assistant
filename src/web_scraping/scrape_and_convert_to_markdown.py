# /src/web_scraping/scrape_and_convert_to_markdown.py

import requests
import os
import logging
from bs4 import BeautifulSoup
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import AsyncHtmlLoader
from common.file_handling import save_text_to_file

# Set up logging
logging.basicConfig(level=logging.INFO)

def scrape_and_convert_to_markdown(url):
    # Log the start of the function
    logging.info("Starting scrape_and_convert_to_markdown")

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

    html_content = response.text

    # Parse HTML content using BeautifulSoup
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
    except Exception as e:
        logging.error(f"Failed to parse HTML: {e}")
        return

    # Convert HTML to Markdown using html2text
    urls = [url] # Correct the variable name and create a list
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    html2text_transformer = Html2TextTransformer()
    docs_transformed = html2text_transformer.transform_documents(docs)

    # Assign the transformed text to the 'transformed_text' variable
    transformed_text = ""
    for doc in docs_transformed:
        transformed_text += doc.page_content + "\n"

    # Save the markdown content to a file
    markdown_file_path = os.path.join('data', 'raw_data', 'scraped_content.md')
    try:
        save_text_to_file(markdown_file_path, transformed_text)
    except Exception as e:
        logging.error(f"Failed to save markdown content to file: {e}")
        return

    # Log the end of the function
    logging.info("Finished scrape_and_convert_to_markdown")

    return transformed_text

