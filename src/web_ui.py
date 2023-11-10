# \src\web_ui.py
import os
from dotenv import load_dotenv
from flask import Flask
from web_scraping.scraper import Scraper

load_dotenv()

secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = secret_key

scraper = Scraper()
