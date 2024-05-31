import streamlit as st
from driver_engine import Engine

def main():
    st.title("Movie search engine")
    search_text = st.text_input("Search for a movie:", value='Horrible bosses')
    button = st.button('Search')
    if button or search_text:
        with st.spinner('Looking up...'):
            with st.empty():
                for results in Engine().search(what=search_text, cat='movies'):
                    st.markdown(results.to_html(render_links=True,
                                escape=False), unsafe_allow_html=True)

if __name__=="__main__":
    main()
