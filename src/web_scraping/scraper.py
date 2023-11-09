# \src\web_scraping\scraper.py

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from common.file_utils import find_unique_file_name, save_text_to_file, create_directory
from markupsafe import Markup
from flask import flash
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from langchain import LangChain, Pipeline
from langchain.tasks import Lowercase, RemovePunctuation, RemoveWhitespace, Tokenize, RemoveStopwords, Stem

# Define the pipeline for text preprocessing
preprocessing_pipeline = Pipeline([
    Lowercase(),
    RemovePunctuation(),
    RemoveWhitespace(),
    Tokenize(),
    RemoveStopwords(),
    Stem()
])

# Create global variables for stopwords and stemmer to avoid reinitializing them for every text
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Create a global session object
session = requests.Session()

# Sends a GET request to the given URL using the global session object.
def send_get_request(url):
    return session.get(url)

# Parses the HTML response using the lxml parser.
def parse_html(response):
    return BeautifulSoup(response.text, "lxml")

# Extracts all the text from the website.
def extract_text(soup):
    return soup.get_text()

# Gets the website name from the URL using urlsplit library.
def get_website_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc.split('.')[-2]

def preprocess_text(text):
    return preprocessing_pipeline.process(text)

def scrape_and_save_data(website_url, scrape_text):
    # Send a GET request to the website URL
    response = send_get_request(website_url)

    # Parse the HTML response
    soup = parse_html(response)

    # Extract the text from the website
    text = extract_text(soup)

    # Save the text to a file
    if scrape_text:
        preprocessed_text = preprocess_text(text)
        website_name = get_website_name(website_url)
        directory = "data/preprocessed_data"
        create_directory(directory)
        file_name = find_unique_file_name(directory, website_name)
        file_path = os.path.join(directory, file_name)
        save_text_to_file(file_path, preprocessed_text)
        flash(Markup(f'Text scraped and saved to <a href="{file_path}">{file_path}</a>.'))
