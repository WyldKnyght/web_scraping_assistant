# \src\routes\home.py
from flask import Blueprint, render_template, request, flash
from web_scraping.scraper import Scraper
from web_scraping.data_preprocessing import Preprocessor
from markupsafe import Markup
from werkzeug.utils import secure_filename

home_bp = Blueprint('home', __name__)
preprocessor = Preprocessor()

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            website_url = request.form.get('website_url')
            scrape_text = request.values.get('scrape_text') == 'on'

            scraper = Scraper()

            if scrape_text:
                result = scraper.scrape_and_save_data(website_url, scrape_text=True)
                if result:
                    flash(Markup(f'Text scraped and saved to <a href="{result}">{result}</a>.'))
                else:
                    flash('An error occurred during scraping.')
            else:
                scraper.launch_browser(website_url)
                flash('Browser launched in headless mode.')

        except Exception as e:
            flash(f'An error occurred: {str(e)}')

    return render_template('home.html')

@home_bp.route('/preprocess', methods=['POST'])
def preprocess():
    if 'file' in request.files:
        file = request.files['file']
        text = file.read().decode('utf-8')
        
        filename = secure_filename(file.filename)
        result = preprocessor.preprocess_and_save_data(text, filename)
        
        if result:
            flash(Markup(f'File processed and saved to <a href="{result}">{result}</a>.'))
        else:
            flash('An error occurred during preprocessing.')
    else:
        flash('No file uploaded.')

    return render_template('home.html')
