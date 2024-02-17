import streamlit as st
import pickle

# Load the pickled model
with open('nlp.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('NLP Sentiment Analysis')

# User input
user_input = st.text_area("Enter Text", "")

# Predict and display the result
if st.button('Predict Sentiment'):
    prediction = model.predict([user_input])[0]
    if prediction == 1:
        st.write('Positive Sentiment')
    else:
        st.write('Negative Sentiment')


st.code("for i in range(8): foo()")
