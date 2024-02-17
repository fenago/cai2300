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

# Setting up the sidebar
st.sidebar.title("Options")
st.sidebar.info("This NLP app uses a pre-trained model to predict sentiment. Enter some text and click 'Predict Sentiment'.")

# Main application
st.title('NLP Sentiment Analysis')

# User input in sidebar
user_input = st.sidebar.text_area("Enter Text for Analysis", "")

# Main area for display output
if st.sidebar.button('Predict Sentiment'):
    prediction = model.predict([user_input])[0]
    if prediction == 1:
        st.success('Positive Sentiment')
    else:
        st.error('Negative Sentiment')
