# \src\model_handler\text_classification.py

from model_handler.model_handler import create_model_chain

class TextClassifier:
    def __init__(self, system_prompt):
        self.model = create_model_chain(system_prompt)

    def predict(self, text):
        try:
            # Check if the model is not None before calling it
            if self.model:
                result = self.model(text)
                predicted_class = result[0]['label']
                return predicted_class
            else:
                return None
        except Exception as e:
            # Handle exceptions gracefully
            print(f"Error predicting class: {e}")
            return None
