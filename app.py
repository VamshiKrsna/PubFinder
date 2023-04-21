import streamlit as st
from home import *
from pubs import *
from findpubs import *

PAGES = {
    "Home": home,
    "Pubs": pubs,
    "Find Pubs": findpubs
}

def run_app():
    st.sidebar.title("Choose Page : ")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.run()

if __name__ == "__main__":
    run_app()
