import streamlit as st
import requests

uploaded_file = st.file_uploader(label="Choose a PDF file", type="pdf")

backend_url = st.secrets["BACKEND_URL"]

if uploaded_file is not None and backend_url:
    response = requests.post(backend_url, json={'pdf_url': 'test'})
    
    if response.status_code == 200:
        st.success("PDF uploaded successfully!")
    else:
        st.error("Failed to upload PDF.")