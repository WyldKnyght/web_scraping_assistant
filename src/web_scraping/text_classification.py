# \src\web_scraping\text_classification.py

import os
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from common.create_directory import create_directory

# Set up logging
logging.basicConfig(level=logging.INFO)

class TextClassifier:
    def __init__(self, labels, unique_filename):
        self.labels = labels
        self.vectorizer = TfidfVectorizer()
        self.filename = unique_filename

    def predict(self, text):
        try:
            processed_text = self.preprocess(text)

            # Simple rule-based approach for label assignment
            if "keyword1" in processed_text:
                predicted_label = self.labels[0]
            elif "keyword2" in processed_text:
                predicted_label = self.labels[1]
            else:
                predicted_label = "Unknown"

            # Save the predicted label to a file
            self.save_predicted_label(predicted_label)
            return predicted_label
        except Exception as e:
            print(f"Error predicting class: {e}")
            return None

    def preprocess(self, text):
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.lower() not in stop_words]
        processed_text = ' '.join(tokens)
        return processed_text

    def save_predicted_label(self, predicted_label):

        # Define the directory for saving predicted labels
        prediction_directory = os.path.join('data', 'scraped_data', 'predicted_labels')
        create_directory(prediction_directory)

        # Save the predicted label to a file
        predicted_label_file_path = os.path.join(prediction_directory, f"{self.filename}.txt")
        with open(predicted_label_file_path, 'w') as file:
            file.write(predicted_label)

        # Log the end of the function
        logging.info("Finished text classification")

