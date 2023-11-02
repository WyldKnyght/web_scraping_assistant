#\src\web_ui.py

import os
import webbrowser
from flask import Flask, render_template, request, redirect
from common.file_utils import create_directory, find_unique_file_name, save_text_to_file, save_links_to_file
from common.web_utils import send_get_request, parse_html, extract_text, extract_links, get_website_name
from common.text_preprocessing import preprocess_text

app = Flask(__name__, template_folder='../templates')
scraping_finished = False

@app.route('/', methods=['GET', 'POST'])
def home():
    global scraping_finished
    
    if request.method == 'POST':
        # Get the website URL from the form submission
        website_url = request.form['website_url']
        
        # Get the checkboxes' values from the form submission
        scrape_text = 'scrape_text' in request.form
        scrape_links = 'scrape_links' in request.form
        
        # Perform the scraping and saving logic based on the checkboxes' values
        if scrape_text:
            response = send_get_request(website_url)
            soup = parse_html(response)
            text = extract_text(soup)
            preprocessed_text = preprocess_text(text)  
            website_name = get_website_name(website_url)
            directory = "data/preprocessed_data"  
            create_directory(directory)
            file_name = find_unique_file_name(directory, website_name)
            file_path = os.path.join(directory, file_name)
            save_text_to_file(file_path, preprocessed_text)  
        
        if scrape_links:
            response = send_get_request(website_url)
            soup = parse_html(response)
            links = extract_links(soup)
            website_name = get_website_name(website_url)
            directory = "data/links"
            create_directory(directory)
            file_name = find_unique_file_name(directory, website_name)
            file_path = os.path.join(directory, file_name)
            save_links_to_file(file_path, links)
        
        # Set scraping_finished to True to show the "End" button
        scraping_finished = True
    
    # Render the home.html template for the initial page load
    return render_template('home.html', show_end_button=scraping_finished)

@app.route('/end', methods=['GET'])
def end():
    # Redirect to a blank page to simulate closing the web page
    return redirect("about:blank")

if __name__ == '__main__':
    # Open the browser automatically
    webbrowser.open('http://localhost:5000/')
    
    # Run the Flask server in production mode
    app.run(debug=False)
