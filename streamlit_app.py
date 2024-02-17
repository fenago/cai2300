import streamlit as st
import pickle

# Define a function to load the model and apply the st.cache decorator
@st.cache(allow_output_mutation=True)
def load_model():
    with open('nlp.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load the pickled model using the cached function
model = load_model()

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
