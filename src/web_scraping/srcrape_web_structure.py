# /src/web_scraping/srcrape_web_structure.py

import requests
from bs4 import BeautifulSoup
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import AsyncHtmlLoader

def scrape_and_convert_to_markdown(website_url):
    # Fetch HTML content from the website
    response = requests.get(website_url)
    html_content = response.text

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Convert HTML to Markdown using html2text
    urls = [website_url]
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    html2text_transformer = Html2TextTransformer()
    docs_transformed = html2text_transformer.transform_documents(docs)

    # Return the transformed text instead of printing
    transformed_text = ""
    for doc in docs_transformed:
        transformed_text += doc.text + "\n"

    return transformed_text
