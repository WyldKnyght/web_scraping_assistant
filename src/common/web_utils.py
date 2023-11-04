import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

session = requests.Session()

def send_get_request(url):
    """
    Sends a GET request to the given URL using a session object.

    Args:
        url (str): The URL to send the request to.

    Returns:
        requests.Response: The response object containing the server's response to the request.
    """
    with requests.Session() as session:
        response = session.get(url)
    return response

def parse_html(response):
    """
    Parses the HTML response using the lxml parser.

    Args:
        response (requests.Response): The response object containing the server's response to the request.

    Returns:
        bs4.BeautifulSoup: The BeautifulSoup object representing the parsed HTML.
    """
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def extract_text(soup):
    """
    Extracts all the text from the website.

    Args:
        soup (bs4.BeautifulSoup): The BeautifulSoup object representing the parsed HTML.

    Returns:
        str: The extracted text from the website.
    """
    text = soup.get_text()
    return text

def extract_links(soup):
    """
    Extracts all the links from the website using a generator expression.

    Args:
        soup (bs4.BeautifulSoup): The BeautifulSoup object representing the parsed HTML.

    Returns:
        generator: A generator object containing the links extracted from the website.
    """
    links = (link.get('href') for link in soup.find_all('a') if link.get('href'))
    return links

def get_website_name(url):
    """
    Gets the website name from the URL using urlsplit library.

    Args:
        url (str): The URL to extract the website name from.

    Returns:
        str: The extracted website name.
    """
    website_name = urlsplit(url).hostname.split('.')[0]
    return website_name