#/src/routes/home.py

from flask import Blueprint, render_template_string, request, flash
from markupsafe import Markup
from common.file_utils import find_unique_file_name, save_text_to_file
from common.text_preprocessing import preprocess_text
from web_ui import scrape_and_save_data

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
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
