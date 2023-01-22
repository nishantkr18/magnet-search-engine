# a basic streamlit application.   

import streamlit as st

from driver_engine import Engine


def show_results(results):
    st.markdown(results.to_html(render_links=True, escape=False),unsafe_allow_html=True)

    # for x, email in enumerate(results['name']):
    #     col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
    #     col1.write(x)  # index
    #     col2.write(results['name'][x])  # email
    #     col3.write(results['size'][x])  # unique ID
    #     col4.write(results['seeds'][x])   # email status
    #     # disable_status = results['disabled'][x]  # flexible type of button
    #     # button_type = "Unblock" if disable_status else "Block"
    #     button_phold = col5.empty()  # create a placeholder
    #     do_action = button_phold.button(button_type, key=x)
    #     if do_action:
    #          pass # do some action with row's data
    #          button_phold.empty()  #  remove button


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