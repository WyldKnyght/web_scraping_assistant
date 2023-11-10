#\src\web_scraping\data_cleaning.py

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

# Create global variables for stopwords and stemmer to avoid reinitializing them for every text
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords and stem the tokens
    processed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    
    # Join the processed tokens back into a single string
    processed_text = ' '.join(processed_tokens)
    
    return processed_text
