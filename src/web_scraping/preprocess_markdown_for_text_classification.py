# \src\web_scraping\preprocess_markdown_for_text_classification.py

import markdown
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the Markdown text from a file
with open('data.md', 'r') as f:
    text = f.read()

# Parse the Markdown text into plain text
md = markdown.Markdown(text)
plain_text = md.safe_get_body()

# Tokenize the plain text into words
tokens = word_tokenize(plain_text)

# Remove stop words and punctuation
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token.lower() not in stop_words]

# Convert tokens to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tokens)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing data
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))