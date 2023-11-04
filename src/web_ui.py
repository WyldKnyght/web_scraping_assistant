# \src\web_ui.py

import os
import threading
import webbrowser
import secrets
from urllib.parse import urlsplit
from flask import Flask, request, redirect, render_template_string, flash
from webdriver_manager.chrome import ChromeDriverManager
from common.file_utils import find_unique_file_name, save_text_to_file
from common.text_preprocessing import preprocess_text
from markupsafe import Markup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
