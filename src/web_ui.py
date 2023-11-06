# \src\web_ui.py

import secrets
from flask import Flask
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

secret_key = secrets.token_hex(16)
app = Flask(__name__)
app.secret_key = secret_key

def launch_browser_and_scrape(website_url):
    # Launch the browser in the main thread
    webdriver_service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=webdriver_service)

    # Navigate to the website URL
    browser.get(website_url)

    # Scrape the text from the page
    text = browser.page_source

    # Close the browser
    browser.quit()

    return text
