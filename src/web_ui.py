# \src\web_ui.py

import os
import threading
import webbrowser
from urllib.parse import urlsplit
from flask import Flask, request, redirect, render_template_string, flash
from markupsafe import Markup
from requests_html import HTMLSession
from common.file_utils import find_unique_file_name, save_text_to_file
from common.text_preprocessing import preprocess_text
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import secrets

secret_key = secrets.token_hex(16)
app = Flask(__name__)
app.secret_key = secret_key


def scrape_and_save_data(website_url, scrape_text):
    # Launch the browser in the main thread
    webdriver_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=webdriver_service)

    # Navigate to the website URL
    browser.get(website_url)

    # Scrape the text from the page
    text = browser.page_source

    # Save the text to a file
    if scrape_text:
        preprocessed_text = preprocess_text(text)
        website_name = urlsplit(website_url).netloc
        directory = "data/preprocessed_data"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_name = find_unique_file_name(directory, website_name)
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:  # Specify 'utf-8' encoding
            f.write(preprocessed_text)
        flash(Markup(f'Text scraped and saved to <a href="{file_path}">{file_path}</a>.'))

    # Close the browser
    browser.quit()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the website URL from the form submission
        website_url = request.values.get('website_url')

        # Get the checkbox's value from the form submission
        scrape_text = request.values.get('scrape_text') == 'on'

        # Perform the scraping and saving logic based on the checkbox's value
        if scrape_text:
            scrape_and_save_data(website_url, scrape_text)
            
    # Render the home.html template for the initial page load
    return render_template_string('''
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul class=flashes>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        <form method="post">
        <label for="website_url">Website URL:</label>
        <input type="text" id="website_url" name="website_url" required>
        <br>
        <input type="checkbox" id="scrape_text" name="scrape_text">
        <label for="scrape_text">Scrape Text</label>
        <br>
        <button type="submit">Scrape</button>
        </form>
    ''')