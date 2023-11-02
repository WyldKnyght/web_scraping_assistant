#\src\common\web_utils.py

import requests
from bs4 import BeautifulSoup

def send_get_request(url):
    # Send a GET request to the URL
    response = requests.get(url)
    return response

def parse_html(response):
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def extract_text(soup):
    # Extract all the text from the website
    text = soup.get_text()
    return text

def extract_links(soup):
    # Extract all the links from the website
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

def get_website_name(url):
    # Get the website name from the URL
    website_name = url.split("//")[-1].split("/")[0]
    return website_name
