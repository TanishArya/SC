import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import streamlit as st

# Load the dataset
data = pd.read_csv('spam.csv', encoding='latin1')

# Preprocess the data
X = data['v2']  # Text data
y = data['v1']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Streamlit User Interface
st.title('Spam Filter')

# Text input for user to input text
text_input = st.text_area('Enter email for cheak:', '')

if st.button('Predict'):
    # Preprocess the input text
    input_vec = vectorizer.transform([text_input])

    # Predict the class
    prediction = model.predict(input_vec)

    # Display the prediction
    st.write('Prediction:', prediction[0])
