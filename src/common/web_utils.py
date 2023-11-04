import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

session = requests.Session()

def send_get_request(url):
    # Send a GET request to the URL using a session object
    response = session.get(url)
    return response

def parse_html(response):
    # Parse the HTML response using the lxml parser
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def extract_text(soup):
    # Extract all the text from the website
    text = soup.get_text()
    return text

def extract_links(soup):
    # Extract all the links from the website using list comprehension
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    return links

def get_website_name(url):
    # Get the website name from the URL using urlparse library
    website_name = urlparse(url).netloc.split('.')[0]
    return website_name