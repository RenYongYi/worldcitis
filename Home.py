import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

st.title("Welcome to World Cities")

st.write("""
This is the home page of the World Cities application.
Navigate to the pages section to explore more features.
""")

if st.button("Go to App →", key="go_to_app"):
    st.switch_page("pages/app.py")
