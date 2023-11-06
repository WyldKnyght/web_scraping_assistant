from flask import Blueprint, render_template, request
from web_scraping.scraper import scrape_and_save_data
from web_ui import launch_browser_and_scrape
from urllib.parse import urlsplit
from common.file_utils import find_unique_file_name, create_directory

def get_website_name(website_url):
    # Split the URL into components
    url_components = urlsplit(website_url)

    # The second component of the split URL is the network location (www.edureka.co)
    network_location = url_components[1]

    # Split the network location into parts separated by dots
    location_parts = network_location.split('.')

    # The website name is the second to last part of the network location (edureka)
    website_name = location_parts[-2]

    return website_name

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the website URL from the form submission
        website_url = request.form.get('website_url')

        # Get the website name from the website URL
        website_name = get_website_name(website_url)
        
        # Define the directory variable
        directory = "data/preprocessed_data"

        # Call the find_unique_file_name function with the website name
        file_name = find_unique_file_name(directory, website_name)

        # Get the checkbox's value from the form submission
        scrape_text = request.values.get('scrape_text') == 'on'

        # Perform the scraping and saving logic based on the checkbox's value
        if scrape_text:
            text = launch_browser_and_scrape(website_url)
            scrape_and_save_data(website_url, scrape_text)

    # Render the home.html template for the initial page load
    return render_template('home.html')
