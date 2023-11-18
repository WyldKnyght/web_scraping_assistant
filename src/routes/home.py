from flask import Blueprint, render_template, request, flash
from web_scraping.scraper import Scraper
from web_scraping.data_preprocessing import Preprocessor
from web_scraping.data_transformation import DataTransformer 
from common.file_handling import create_directory, save_text_to_file
from markupsafe import Markup
from werkzeug.utils import secure_filename

home_bp = Blueprint('home', __name__)
preprocessor = Preprocessor()
data_transformer = DataTransformer()  # Change the name here

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            website_url = request.form.get('website_url')
            scrape_text = request.values.get('scrape_text') == 'on'

            scraper = Scraper()

            if scrape_text:
                if result := scraper.scrape_and_save_data(
                    website_url, scrape_text=True
                ):
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
        if result := preprocessor.preprocess_and_save_data(text, filename):
            flash(Markup(f'File processed and saved to <a href="{result}">{result}</a>.'))
        else:
            flash('An error occurred during preprocessing.')
    else:
        flash('No file uploaded.')

    return render_template('home.html')

@home_bp.route('/transform', methods=['POST'])
def transform():
    if 'file' in request.files:
        file = request.files['file']
        text = file.read().decode('utf-8')

        filename = secure_filename(file.filename)
        
        # Call the transform_and_save_data method from the DataTransformer class
        if result := data_transformer.transform_and_save_data(text, filename):
            flash(Markup(f'Transformed data saved to <a href="{result}">{result}</a>.'))
        else:
            flash('An error occurred during transformation.')
    else:
        flash('No file uploaded for transformation.')

    return render_template('home.html')