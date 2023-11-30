# /src/model_handler/text_classification.py

from transformers import pipeline
from transformers import AutoModelForSequenceClassification

class TextClassifier:
    def __init__(self, model_path):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_path,
            local_files_only=True
        )

    def predict(self, text):
        # Use the model to predict the class of the text
        result = self.model(text)
        # Extract the predicted class from the result
        predicted_class = result[0]['label']
        return predicted_class
