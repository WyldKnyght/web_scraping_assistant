# \src\user_interface\ui_functions\get_website_name.py

from urllib.parse import urlparse

def get_website_name(url):
    parsed_url = urlparse(url)
    website_name = parsed_url.netloc
    return website_name