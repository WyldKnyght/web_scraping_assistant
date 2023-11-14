# \src\web_scraping\data_preprocessing.py

import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from common.file_handling import create_directory, save_text_to_file
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from gensim.models import LdaModel
from gensim.corpora import Dictionary

# Instantiate the lemmatizer
lemmatizer = WordNetLemmatizer()

class Preprocessor:
    def preprocess_and_save_data(self, text, filename):
        if not text:
            raise ValueError("Text is empty")
       
        # Tokenize the text
        tokens = word_tokenize(text)
        
        # Lemmatize the tokens
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        # Remove domain-specific stopwords
        domain_stopwords = ["some", "domain", "specific", "stopwords"]  # replace with your domain-specific stopwords
        processed_tokens = [token for token in lemmatized_tokens if token not in domain_stopwords]
        
        # Remove rare words
        word_counts = Counter(processed_tokens)
        rare_words = [word for word, count in word_counts.items() if count <= 2]
        processed_tokens = [token for token in processed_tokens if token not in rare_words]
        
        # Perform POS tagging
        pos_tags = pos_tag(processed_tokens)
        
        # Perform NER
        ner_tags = ne_chunk(pos_tags)
        
        # Convert the list of tokens and NER tags back to a single string
        processed_text = ' '.join([f"{token}_{tag}" for token, tag in ner_tags])
        
        # Perform TF-IDF vectorization
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([processed_text])
        
        # Perform Word Embedding
        word2vec_model = Word2Vec([processed_tokens], min_count=1)
        
        # Perform Topic Modeling using LDA
        dictionary = Dictionary([processed_tokens])
        corpus = [dictionary.doc2bow(processed_tokens)]
        lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary)
        
        directory = "data/preprocessed_data"
        create_directory(directory)
        file_path = os.path.join(directory, filename)
        save_text_to_file(file_path, processed_text)
        
        return file_path, tfidf_matrix, word2vec_model, lda_model
