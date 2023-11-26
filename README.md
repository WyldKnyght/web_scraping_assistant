# Web Scraping Assistant

# Project README

## Overview
This project comprises a Streamlit web application designed for efficient web scraping, markdown conversion, and dataset creation. Users can input a web URL, triggering a process that adeptly scrapes HTML content, converts it to Markdown, and further transforms it into a CSV dataset. The main functionalities are encapsulated in the following modules:

### 1. `src/app/main.py`
- Initiates the Streamlit web app.
- Manages the execution of the web app process.

### 2. `src/user_interface/web_ui.py`
- Streamlit interface for user interaction.
- Prompts users for a web URL and topic.
- Performs web scraping and conversion functions.
- Displays results using Streamlit elements.

### 3. `src/user_interface/ui_functions.py`
- Contains UI functions for user input and interaction.
- Validates URLs, checks robots.txt, and triggers scraping.
- Supports user prompts for website URL, main topic, and scraping preferences.

### 4. `src/web_scraping/convert_markdown_to_dataset.py`
- Converts Markdown content into a dataset.
- Saves the dataset to a CSV file.

### 5. `src/web_scraping/scrape_and_convert_to_markdown.py`
- Fetches HTML content from a given URL.
- Parses HTML using BeautifulSoup.
- Converts HTML to Markdown using html2text.
- Saves the Markdown content to a file.

## Instructions for Launching the App
1. Navigate to `/src/app/` and run `main.py` to start the Streamlit web app.
2. Access the app via the provided URL.

**Note:** Ensure dependencies are installed (`pip install -r requirements.txt`).

This project is my submission for [Backdrop Build v2](https://backdropbuild.com/v2)

## Getting Started

To get started with the Web Scraping Assistant, follow these steps:

1. Clone the repository: `git clone https://github.com/WyldKnyght/web_scraping_assistant.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the application: `python src/main.py`

## Roadmap

<img src="\docs\Roadmap.png">


## Contributing

Contributions to the Web Scraping Assistant are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

This project is developed in collaboration with ChatGPT (GPT-3.5) and Phind. 

Llama Generative Agent created by Uranus Seven [UranusSeven\llama_generative_agent](https://github.com/UranusSeven/llama_generative_agent)

AI-Chatbot using Streamlit + Langchain + LLama.cpp created by Karim Lalani[karimlalani/ai-chatbot](https://github.com/karimlalani/ai-chatbot)

