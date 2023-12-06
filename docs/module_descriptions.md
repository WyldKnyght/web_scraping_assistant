# Module Descriptions

## Introduction
The project is composed of several Python modules that work together to create a web scraping assistant. Here is a brief description of each module:

## Entry Point

### main.py
main.py is the entry point of the application. It initializes the model and runs the web application [source code].


## user_interface

### web_ui.py
web_ui.py in the user_interface package is responsible for the user interface of the web application. It uses the Streamlit library to create the web page where users can input a URL to be scraped. It also displays the results of the scraping process, and allows users to download the resulting CSV dataset [source code].

### ui_functions.py
ui_functions.py in the user_interface package includes several utility functions used in the user interface, such as URL validation, URL input retrieval, and robots.txt checking [source code].

## common

### file_handling.py
file_handling.py in the common package contains functions for creating directories and handling files. It's used throughout the project for tasks such as saving scraped data and creating unique file names [source code].


## web_scraping

### analyze_website_structure.py
analyze_website_structure.py in the web_scraping package is used to analyze the structure of a website. It checks whether the website is static or dynamic [source code].

### get_website_elements.py
get_website_elements.py in the web_scraping package extracts unique elements from a website and saves them to a JSON file [source code].

### text_classification.py
text_classification.py in the model_handler package contains the TextClassifier class, which uses the LlamaCpp library to classify text [source code].

### preprocess_markdown_for_text_classification.py
preprocess_markdown_for_text_classification.py in the web_scraping package tokenizes and vectorizes markdown content, then trains and evaluates a logistic regression model for text classification [source code].

### scrape_html.py
scrape_html.py in the web_scraping package is responsible for fetching HTML content from a website [source code].

### convert_html_to_markdown.py
convert_html_to_markdown.py in the web_scraping package is responsible for converting it to Markdown, classifying the content, and saving it to a file [source code].

### convert_markdown_to_dataset.py
convert_markdown_to_dataset.py in the web_scraping package converts the Markdown content into a Pandas DataFrame, classifies the content, and saves the dataset to a CSV file [source code].

## Summary
Each of these modules play a specific role in the overall functionality of the project, and they work together to accomplish the goal of the web scraping assistant: to automatically scrape websites, classify the content, and generate a CSV dataset for further analysis.
