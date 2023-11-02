#/src/common/text_preprocessing.py

def lowercase_text(text):
    return text.lower()

import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_whitespaces(text):
    return " ".join(text.split())

from nltk.tokenize import word_tokenize

def tokenize_text(text):
    return word_tokenize(text)

from nltk.corpus import stopwords

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

from nltk.stem import PorterStemmer

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def preprocess_text(text):
    text = lowercase_text(text)
    text = remove_punctuation(text)
    text = remove_whitespaces(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = stem_tokens(tokens)
    return ' '.join(tokens)
