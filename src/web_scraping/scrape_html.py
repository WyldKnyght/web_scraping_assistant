# \src\web_scraping\scrape_html.py

import logging
import os
import requests
import urllib.robotparser
from common.save_to_file import save_to_file
from common.create_directory import create_directory

# Set up logging
logging.basicConfig(level=logging.INFO)

def scrape_html(url, unique_filename):
    # Log the start of the function
    logging.info(f"Starting scrape_html for URL: {url}")

    try:
        # Check if the URL is allowed by the robots.txt file
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(url)
        rp.read()
        if not rp.can_fetch('*', url):
            logging.error(f"URL is not allowed by robots.txt: {url}")
            return None

        # Fetch HTML content from the website
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Save the data to an HTML file
        html_file_directory = os.path.join('data', 'scraped_data', 'html_data')
        html_file_name = unique_filename
        html_file_path = os.path.join(html_file_directory, f'{html_file_name}.html')

        try:
            create_directory(html_file_directory)
            save_to_file(html_file_path, response.text, 'html')
        except Exception as e:
            logging.error(f"Failed to save data to HTML: {e}")
            return None

        return response.text

    except Exception as e:
        logging.error(f"Error in scrape_html: {e}")
        return None
