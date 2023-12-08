import os
import logging
from urllib.parse import urlparse
import tldextract

# Set up logging
logging.basicConfig(level=logging.INFO)

class UniqueFilenameManager:
    _instance = None
    _unique_filename = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def set_unique_filename(cls, url):
        base_name = cls._get_base_name_from_url(url)
        website_name = cls._get_website_name(url)
        unique_filename = cls._find_unique_filename(['data', 'scraped_data', 'html_data'], base_name, website_name)
        cls._unique_filename = unique_filename

    @classmethod
    def get_unique_filename(cls):
        return cls._unique_filename

    @staticmethod
    def _get_website_name(url):
        # Extract the domain from the URL
        domain = urlparse(url).netloc
        # Extract the subdomain from the domain
        subdomain = tldextract.extract(domain).subdomain
        # Return the subdomain if it exists, otherwise return the domain
        return subdomain if subdomain else domain

    @staticmethod
    def _get_base_name_from_url(url):
        extracted_info = tldextract.extract(url)
        website_name = extracted_info.domain
        return website_name

    @classmethod
    def _find_unique_filename(cls, directory_list, base_name, website_name):
        # Combine the directory components into a single path
        directory = os.path.join(*directory_list)

        counter = 1

        unique_filename = f"{base_name}-{counter}"

        while os.path.exists(os.path.join(directory, unique_filename)):
            # Increment the counter in every iteration
            counter += 1
            unique_filename = f"{base_name}-{counter}"

        logging.info(f"Unique file name found: {unique_filename}")
        return unique_filename