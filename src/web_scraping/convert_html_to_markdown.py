# \src\web_scraping\convert_html_to_markdown.py

import logging
import os
from common.file_handling import save_text_to_file
from langchain.document_loaders import AsyncHtmlLoader
from langchain.document_transformers import Html2TextTransformer
from user_interface.ui_functions import unique_filename
from web_scraping.text_classification import TextClassifier

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_to_markdown(html_content, labels, unique_filename):
    # Log the start of the function
    logging.info("Starting convert_to_markdown")

    # Save the HTML content to a file
    html_file_directory = os.path.join('data', 'raw_data', 'html_data')
    html_file_name = unique_filename('dummy_url')  # Replace 'dummy_url' with actual URL
    html_file_path = os.path.join(html_file_directory, html_file_name + '.html')

    try:
        save_text_to_file(html_file_path, html_content)

        # Load the html content
        with open(html_file_path, 'r') as file:
            html_content = file.read()

        # Convert HTML to Markdown using html2text
        loader = AsyncHtmlLoader([''])
        docs = loader.load(html_content)
        html2text_transformer = Html2TextTransformer()
        docs_transformed = html2text_transformer.transform_documents(docs)

        # Assign the transformed text to the 'transformed_text' variable
        transformed_text = "\n".join(doc.page_content for doc in docs_transformed)

        # Use the TextClassifier to classify the transformed text
        classifier = TextClassifier(labels, html_file_name)

        # Train the classifier with the extracted labels
        classifier.train(transformed_text, labels)

        # Predict the class
        predicted_class = classifier.predict(transformed_text)

        if predicted_class is not None:
            # Save the markdown content to a file with .md extension
            save_text_to_file(os.path.join('data', 'raw_data', html_file_name + ".md"), transformed_text + "\n\n" + str(predicted_class))
            return html_file_name
        else:
            print("Failed to predict class.")
            logging.error("Failed to predict class.")
            return None

    except Exception as e:
        logging.error(f"Error in convert_to_markdown: {e}")
        return None
