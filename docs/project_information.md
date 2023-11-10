# Web Scraping Assistant

The Web Scraping Assistant is a comprehensive project designed to streamline web data extraction and preprocessing for training Language Model Models (LLMs). This project offers a well-organized directory structure, clear separation of responsibilities, and a user-friendly web interface for effortless data acquisition. The system is equipped with essential components, including HTML templates, route handling, text preprocessing, and efficient data management. This document delves into the details of each component, providing an in-depth understanding of the project's architecture and functionality.

## Project Directory Structure

This project follows a well-organized directory structure to enhance maintainability and collaboration. The directories are structured as follows:

- **data:** This directory is dedicated to storing extracted data.
- **preprocessed_data:** Here, you can find preprocessed data ready for use.
- **training_data:** This directory houses data intended for training purposes.
- **src:** The project's source code is located in this directory.

This organization ensures a clear separation of data, source code, and other project-related files, making it easier to manage and collaborate on the project.

## HTML Template (home.html)

The HTML template serves as a straightforward form for entering a website URL to initiate the scraping process. It also features a checkbox that provides control over whether to scrape text or not. While minimal, it fulfills its functional purpose effectively.

The core structure is defined in the `templates/home.html` file, which contains an HTML form. This form enables users to input a website URL and make a choice regarding text scraping. Additionally, the `src/main.py` file plays a pivotal role in the integration by importing the `app` object from the `web_ui` module. It also registers the `home_bp` blueprint and applies `nest_asyncio` to enable asynchronous functionality with Flask. In addition, the Flask app is run in debug mode to facilitate development and testing.
## Main Script (main.py)

The `main.py` script plays a pivotal role in the project by setting up the Flask app and registering blueprints to handle web routes. It effectively integrates asynchronous functionality with Flask using `nest_asyncio`, enhancing the application's responsiveness.

The `src` folder serves as the project's codebase, housing various modules such as chatbots, common, routes, and web_scraping. It's in this directory that you'll find the source code for the entire project.

Within the `main.py` file, you'll find the entry point for the Flask app. It registers the `home_bp` blueprint from the `routes.home` module, facilitating the handling of web routes and user interactions.

## Web UI (web_ui.py)

The `web_ui.py` script serves as the initialization point for the Flask app. It is responsible for setting the secret key and defining the `launch_browser_and_scrape` function. This function is designed to launch a browser, navigate to a specified website URL, scrape text from the webpage, and return the text.

## Browser Functionality (browser.py)

The `browser.py` module, located within the `web_scraping` folder, also provides a function called `launch_browser_and_scrape`. This function, like the one in `web_ui.py`, is responsible for launching a browser, navigating to a specified website URL, scraping text from the webpage, and returning the text.

Having two separate implementations of the same function in different locations could lead to confusion and duplication. It's recommended to ensure a clear separation of concerns and avoid duplicate function definitions for better code organization and maintenance. A potential improvement could be to consolidate the functionality into a single location to maintain consistency.

## File Handling (file_handling.py)

The `file_handling.py` script is a valuable asset for the project, providing essential functions for efficient file and directory management. It includes the following key functions:

- **create_directory:** This function creates a directory if it doesn't already exist, ensuring the project's data is organized systematically.

- **find_unique_file_name:** The `find_unique_file_name` function is responsible for locating a unique and available file name within a specified directory, preventing naming conflicts.

- **save_text_to_file:** This function allows for the seamless saving of text to a file, enabling the storage of scraped data efficiently.

These functions, residing in the `file_handling.py` module within the `common` folder, are crucial for maintaining the project's data and ensuring smooth data handling operations.

## Route Handling (home.py)

The `home.py` script is responsible for defining the route handling logic for the home page. It manages the form submission, performs web scraping, preprocesses text if requested, and saves the data. However, there are some key points to consider for improvement:

- **Scraper Class Usage:** The code utilizes the `Scraper` class for web scraping, but the class's methods are not explicitly defined within the provided code. It's crucial to ensure that the `Scraper` class is appropriately defined, and its methods are called as intended.

- **Exception Handling:** While the code includes error handling, there's room for improvement in how exceptions are managed. A best practice is to handle exceptions more gracefully. Consider logging errors for debugging purposes or providing more detailed error messages to assist users.

The `home.py` module, located in the `routes` folder, defines the route handling for the home page. It processes form submissions, retrieves the website URL, and checkbox values. The script creates an instance of the `Scraper` class, extracts the website name from the URL, defines the directory structure, and manages the scraping and saving logic based on the checkbox's value. Additionally, it handles the rendering of the `home.html` template for the initial page load.

This script is a central part of the project, facilitating user interactions and data management for web scraping.


## Text Preprocessing (data_cleaning.py)

The `data_cleaning.py` script is an integral part of the project, providing essential text preprocessing functions that play a pivotal role in the natural language processing (NLP) pipeline. These functions ensure that the scraped text is properly prepared for further analysis. The key preprocessing steps include:

- **Lowercasing:** The text is converted to lowercase, ensuring uniformity in text analysis.

- **Punctuation Removal:** Punctuation marks are removed from the text, enhancing text clarity and analysis.

- **Tokenization:** The text is tokenized, splitting it into individual words or tokens.

- **Stopword Removal:** Common stopwords are eliminated from the tokens, reducing noise in the text data.

- **Stemming:** Tokens are subjected to stemming, which involves reducing words to their root forms, aiding in text analysis.

The `data_cleaning.py` module within the `web_scraping` folder offers a function called `preprocess_text`. This function seamlessly performs the entire preprocessing pipeline, encompassing lowercasing, punctuation removal, tokenization, stopwords removal, stemming, and the rejoining of processed tokens into a single string.

These text preprocessing functions are crucial for ensuring that the scraped data is appropriately formatted for further analysis in the NLP pipeline.

## Scraping (Scraper.py)

The `Scraper.py` script houses the `Scraper` class, which serves as the primary component for web scraping in the project. However, it's important to ensure that the class and its methods are well-defined and utilized consistently throughout the application. The Scraper class provides an array of essential methods for various scraping tasks, including:

- **Sending GET Requests:** The `send_get_request` method is used to send GET requests to a specified URL via a session object, allowing the retrieval of web content.

- **HTML Parsing:** The class provides a method to parse HTML responses using the lxml parser, making it easier to navigate and extract information from web pages.

- **Text Extraction:** The `extract_text` method is responsible for extracting all text content from a given website, making it accessible for further processing.

- **Website Name Retrieval:** This class feature allows you to extract the website name from a URL using the `urlsplit` library, aiding in data organization.

- **Browser Launch and Scraping:** The Scraper class supports launching a browser, scraping data from web pages, and saving the data for future use.

- **Data Scraping and Saving:** The class is equipped to handle the complete data scraping and saving process, ensuring that valuable information is captured and stored.

- **Exception Handling:** The Scraper class includes mechanisms to handle exceptions gracefully, enhancing the reliability and robustness of the web scraping operations.

The `Scraper.py` module, residing in the `web_scraping` folder, encapsulates these functionalities within the `Scraper` class. It serves as a critical component for gathering and managing web data for your project.

