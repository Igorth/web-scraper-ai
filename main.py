import streamlit as st

st.title("Web Scraper AI")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
