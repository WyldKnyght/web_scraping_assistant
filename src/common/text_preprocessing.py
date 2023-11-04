#/src/common/text_preprocessing.py

import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Create global variables for stopwords and stemmer to avoid reinitializing them for every text
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Remove whitespaces
    text = " ".join(text.split())

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and stem the tokens in one loop
    tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]

    # Join the tokens back into a string
    return ' '.join(tokens)