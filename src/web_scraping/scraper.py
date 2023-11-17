# \src\web_scraping.py\scraper.py
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from common.file_handling import create_directory, find_unique_file_name, save_text_to_file
from selenium.webdriver.chrome.options import Options
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

# Create global variables for stopwords and stemmer to avoid reinitializing them for every text
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

class Scraper:
    def __init__(self):
        self.session = requests.Session()
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")

    def send_get_request(self, url):
        return self.session.get(url)

    def parse_html(self, response):
        return BeautifulSoup(response.text, "lxml")

    def extract_text(self, soup):
        return soup.get_text()

    @staticmethod
    def preprocess_text(text):
        # Lowercase the text
        text = text.lower()
    
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Tokenize the text
        tokens = word_tokenize(text)
    
        # Remove stopwords and stem the tokens
        processed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    
        # Join the processed tokens back into a single string
        processed_text = ' '.join(processed_tokens)
    
        return processed_text

    def get_website_name(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc.split('.')[-2]

    def scrape_and_save_data(self, website_url, scrape_text=False):
        try:
            response = self.send_get_request(website_url)
            soup = self.parse_html(response)
            text = self.extract_text(soup)

            if scrape_text:
                preprocessed_text = self.preprocess_text(text)
                website_name = self.get_website_name(website_url)
                directory = "data/raw_data"
                create_directory(directory)
                file_name = find_unique_file_name(directory, website_name)
                file_path = os.path.join(directory, file_name)
                save_text_to_file(file_path, preprocessed_text)
                return file_path  
        except Exception as e:
            return str(e)
