# \src\routes\home.py
from flask import Blueprint, render_template, request, flash
from web_scraping.scraper import Scraper
from markupsafe import Markup

home_bp = Blueprint('home', __name__)

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
