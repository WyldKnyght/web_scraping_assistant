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
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error sending request: {e}")
            return None

    def parse_html(self, response):
        try:
            return BeautifulSoup(response.text, "lxml")
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return None

    def extract_text(self, soup):
        try:
            return soup.get_text()
        except Exception as e:
            print(f"Error extracting text: {e}")
            return None

    @staticmethod
    def preprocess_text(text):
        try:
            # Lowercase the text
            text = text.lower()

            # Remove punctuation
            text = text.translate(str.maketrans('', '', string.punctuation))

            # Tokenize the text
            tokens = word_tokenize(text)

            # Remove stopwords and stem the tokens
            processed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]

            return ' '.join(processed_tokens)
        except Exception as e:
            print(f"Error preprocessing text: {e}")
            return None

    def get_website_name(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc.split('.')[-2]

    def scrape_and_save_data(self, website_url, scrape_text=False):
        response = self.send_get_request(website_url)
        if response is None:
            return None

        soup = self.parse_html(response)
        if soup is None:
            return None

        text = self.extract_text(soup)
        if text is None:
            return None

        if scrape_text:
            preprocessed_text = self.preprocess_text(text)
            if preprocessed_text is None:
                return None

            website_name = self.get_website_name(website_url)
            directory = "data/raw_data"
            create_directory(directory)
            file_name = find_unique_file_name(directory, website_name)
            file_path = os.path.join(directory, file_name)

            try:
                with open(file_path, "w") as file:
                    file.write(preprocessed_text)
                return file_path
            except Exception as e:
                print(f"Error saving text to file: {e}")
                return None