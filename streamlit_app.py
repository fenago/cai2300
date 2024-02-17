import streamlit as st
import pickle

# Load the pickled model
with open('nlp.pkl', 'rb') as file:
    model = pickle.load(file)

# Sidebar for user inputs or information
st.sidebar.title("About")
st.sidebar.info(
    "This is a simple NLP Sentiment Analysis app using a pre-trained model. "
    "Enter text in the input box and click 'Predict Sentiment' to see the sentiment analysis."
)

# Main page layout with tabs
tab1, tab2 = st.tabs(["Sentiment Analysis", "More Information"])

with tab1:
    st.title('NLP Sentiment Analysis')
    st.image('https://www.mdc.edu/kendall/img/campus_building_r.jpg')

    # User input
    user_input = st.text_area("Enter Text", "")

    # Predict and display the result
    if st.button('Predict Sentiment'):
        prediction = model.predict([user_input])[0]
        if prediction == 1:
            st.success('Positive Sentiment')
        else:
            st.error('Negative Sentiment')

with tab2:
    st.title("More Information")
    st.write("Here you can provide more information about the model, the technology, or any other relevant details.")

    # Example: Displaying code
    st.code("for i in range(8): foo()", language='python')

    # You can also add images, videos, graphs, etc.

# Footer
st.markdown("---")
st.footer("NLP Sentiment Analysis App © 2024")
