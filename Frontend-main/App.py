import streamlit as st
import base64
import helper
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Custom CSS styles
custom_css = """
<style>
    /* Apply styles to the main container */
    .main-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
        background-color: #f1f8fb; /* Quora light blue color */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Apply styles to the header */
    .header-text {
        font-size: 36px;
        color: #2b6dad; /* Quora dark blue color */
        margin-bottom: 20px;
    }

    /* Apply styles to the text inputs */
    .text-input {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
        border: 1px solid #eeeeee; /* Quora light grey color */
    }

    /* Apply styles to the find button */
    .find-button {
        background-color: #2b6dad; /* Quora dark blue color */
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 18px;
        transition: background-color 0.3s;
    }
    .find-button:hover {
        background-color: #1a4d91; /* Darker shade of Quora dark blue on hover */
    }

    /* Apply styles to the result headers */
    .result-header {
        font-size: 28px;
        color: #2b6dad; /* Quora dark blue color */
        margin-top: 20px;
    }

    /* Apply styles to the Quora logo image */
    .quora-logo {
        margin-bottom: 20px;
    }
</style>
"""

# Inject custom CSS styles
st.markdown(custom_css, unsafe_allow_html=True)

# Load Quora logo image
quora_logo = open("quora_logo.png", "rb").read()
quora_logo_encoded = base64.b64encode(quora_logo).decode()

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Quora logo image with CSS class
st.markdown('<img src="data:image/png;base64,{}" class="quora-logo">'.format(quora_logo_encoded), unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header-text">Check your Question pairs down below !</h1>', unsafe_allow_html=True)

# Input fields
q1 = st.text_input('Enter question 1', value='', max_chars=None, key=None, type='default', help=None, placeholder=None, on_change=None, args=None, kwargs=None)
q2 = st.text_input('Enter question 2', value='', max_chars=None, key=None, type='default', help=None, placeholder=None, on_change=None, args=None, kwargs=None)

# Find button
if st.button('Find', key=None, help=None, on_click=None, args=None, kwargs=None):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    # Display result header
    if result:
        st.markdown('<h2 class="result-header">The question provided conveys a similar meaning. Consider exploring alternative variations of the question to enhance clarity and effectiveness.</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<h2 class="result-header">Not Duplicate</h2>', unsafe_allow_html=True)

# Close main container
st.markdown('</div>', unsafe_allow_html=True)
