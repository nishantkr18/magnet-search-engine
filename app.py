# a basic streamlit application.   

import streamlit as st

from driver_engine import Engine


def show_results(results):
    st.markdown(results.to_html(render_links=True, escape=False),unsafe_allow_html=True)


def main():
    st.title("Movie search engine")
    search_text = st.text_input("Search for a movie:", value='The Matrix')
    button = st.button('Search')
    if button or search_text:
        with st.spinner('Looking up...'):
            with st.empty():
                for results in Engine().search(what=search_text, cat='movies'):
                    show_results(results) 

if __name__=="__main__":
    main()
print()