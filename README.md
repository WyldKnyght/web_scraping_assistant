# Web Scraping Assistant

## Project Description
The goal of this project is to create a Web Scraping Assistant that will extract data from a website and convert it into a dataset that can be used to train LLMs. 
The project is structured in a way that the extracted data is saved in the `data` folder, preprocessed data is saved in the `preprocessed_data` folder, and training data is saved in the `training_data` folder. 
The `src` folder contains the source code for the project.

## Getting Started

To get started with the Web Scraping Assistant, follow these steps:

1. Clone the repository: `git clone https://github.com/WyldKnyght/web_scraping_assistant.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the application: `python src/main.py`

## Usage

1. Open your web browser and navigate to the home page of the Web Scraping Assistant.
2. Enter the URL of the website you want to scrape in the "Website URL" field.
3. Check the "Scrape Text" checkbox if you want to scrape the text from the website.
4. Click the "Scrape" button to start the scraping process.
5. If the "Scrape Text" checkbox is checked, the scraped text will be saved to the `data/preprocessed_data` folder.
6. The file name will be automatically generated based on the website name to ensure uniqueness.


## Roadmap

<img src="\docs\Roadmap.png">


## Contributing

Contributions to the Web Scraping Assistant are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
