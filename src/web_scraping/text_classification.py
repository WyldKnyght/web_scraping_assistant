# \src\web_scraping\text_classification.py

import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Import the unique_filename variable from web_ui.py
from ..common.file_handling import unique_filename

class TextClassifier:
    def __init__(self, labels, unique_filename):
        self.labels = labels
        self.vectorizer = TfidfVectorizer()
        self.filename = unique_filename  # Assign the filename passed as an argument

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
        prediction_directory = os.path.join('data', 'transformed_data', 'text_classification_predictions')
        
        # Use the passed filename as part of the unique filename
        filename = f"{self.filename}-prediction"

        # Save the predicted label to a file
        file_path = os.path.join(prediction_directory, unique_filename + '.txt')
        with open(file_path, 'w') as file:
            file.write(predicted_label)
