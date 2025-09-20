import streamlit as st
import pandas as pd
import numpy as np

with st.sidebar:
    st.header("Thank you for visiting our feedback page!")
    st.write("How can we help you?")

    col1, col2 = st.columns(2)
with col1:
    st.button("Home")
with col2:
    st.button("Contact Us")
# 1. Basic Text Components
st.title("Welcome dear customer!")
st.write("""
## This is our feedback page.
Thank you for chosing our products.
We would love to hear your thoughts and feedback.
""")

st.header("How satisfied are you with our product?")

satisfaction = st.slider("Satisfaction level", 0, 5, 1)

st.header("How do you know about us?")

show_content = st.checkbox("Friends")
show_content = st.checkbox("Family")
show_content = st.checkbox("Social Media")
show_content = st.checkbox("Online Ads")
show_content = st.checkbox("Others")

st.header("Which of our product is your favorite?")

option = st.selectbox(
    "Choose your favorite product",
    ("Classic", "Lite", "Premium", "Ultra")
)
st.write(f"You selected: {option} variant")

st.header("Upload a photo of the product you purchased recently")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")

st.header("Any additional comments?")
comments = st.text_area("Your comments here...", "Type here...")
st.write(f"Thank you for your comments")

import time
if st.button("Submit your Feedback"):
    st.write("Submitting your feedback...")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)
        time.sleep(0.01)
    st.write("Progress complete!")
    st.header("Thank you for your feedback!")


