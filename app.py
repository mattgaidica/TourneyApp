import streamlit as st

# Set page config
st.set_page_config(
    page_title="Tournament App",
    page_icon="🏆",
    layout="wide"
)

# Main title
st.title("Tournament Management App")

# Add a description
st.markdown("""
Welcome to the Tournament Management App! This application helps you manage and track tournaments efficiently.
""")

# Add a sidebar
with st.sidebar:
    st.header("Navigation")
    st.write("Use this sidebar to navigate through different sections of the app.") 