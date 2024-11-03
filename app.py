import streamlit as st
import requests

uploaded_file = st.file_uploader(label="Choose a PDF file", type="pdf")
