# Web Scraping Assistant

The Web Scraping Assistant is a comprehensive project designed to streamline web data extraction and preprocessing for training Language Model Models (LLMs). This project offers a well-organized directory structure, clear separation of responsibilities, and a user-friendly web interface for effortless data acquisition. The system is equipped with essential components, including HTML templates, route handling, text preprocessing, and efficient data management. This document delves into the details of each component, providing an in-depth understanding of the project's architecture and functionality.

## Project Directory Structure

This project follows a well-organized directory structure to enhance maintainability and collaboration. The directories are structured as follows:

- **data:** This directory is dedicated to storing extracted data.
- **src:** The project's source code is located in this directory.

This organization ensures a clear separation of data, source code, and other project-related files, making it easier to manage and collaborate on the project.

## Main Script

The `main.py` responsible for setting up the environment and starting the application.

The `src` folder serves as the project's codebase, housing various modules such as chatbots, common, routes, and web_scraping. It's in this directory that you'll find the source code for the entire project.

## User Interface

The `web_ui.py` script serves as the main interface using Streamlit.

The 'ui_functions.py' script provides a set of functions for interacting with the user interface.

## Web Scraping

The `scrape_and_convert_to_markdown.py` script is responsible for scraping the website and converting the HTML content to markdown using BeautifulSoup and html2text

The 'convert_markdown_to_dataset.py' script is responsible for converting the scraped markdown content into a dataset using pandas to create the dataset

## Model Handling

The 'model_handler.py' script is responsible for handling the language model using the LlamaCpp model

## Chatbot

The 'chatbot.py' script is responsible for handling the chatbot functionality.

The 'message_handling.py' script is responsible for handling the chatbot messages using Streamlit

## File Handling

The `file_handling.py` script is responsible for handling file operations.is responsible for handling file operations.