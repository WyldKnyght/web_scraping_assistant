import os 
from common.file_handling import create_directory, save_text_to_file
import nltk
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer

class DataTransformer:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.pca = PCA(n_components=100)

    def text_vectorization(self, text):
        if not text:
            raise ValueError("Text is empty")

        tokens = nltk.word_tokenize(text)
        X = self.vectorizer.fit_transform(tokens)

        return X

    def feature_extraction(self, X):
        X_pca = self.pca.fit_transform(X)

        return X_pca

    def transform_and_save_data(self, X_pca, filename):
        # Save the labeled text to a file
        directory = "data/transformed_data"
        create_directory(directory)
        file_path = os.path.join(directory, filename)
        save_text_to_file(file_path, X_pca)

        return file_path