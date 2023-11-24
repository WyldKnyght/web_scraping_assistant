# /src/web_scraping/scrape_and_convert.py

import requests
from bs4 import BeautifulSoup
from langchain.document_transformers import Html2TextTransformer
from langchain.document_loaders import AsyncHtmlLoader

def scrape_and_convert_to_markdown(url):
    # Fetch HTML content from the website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the webpage. Status code: {response.status_code}")
    html_content = response.text

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup.prettify())  # print the whole HTML structure
    print(soup.title)  # print the title tag of the HTML

    # Convert HTML to Markdown using html2text
    urls = [url]  # Correct the variable name and create a list
    loader = AsyncHtmlLoader(urls)
    docs = loader.load()
    html2text_transformer = Html2TextTransformer()
    docs_transformed = html2text_transformer.transform_documents(docs)
    for doc in docs_transformed:
        print(doc.page_content)

    return "".join(doc.page_content + "\n" for doc in docs_transformed)