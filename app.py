# a basic streamlit application.   

import streamlit as st
import pandas as pd

from search_engines import piratebay


def main():
    st.title("Movie search engine")
    search_text = st.text_input("Search for a movie:", value='The Matrix')
    if search_text:
        with st.spinner('Wait for it...'):
            results = piratebay.piratebay().search(search_text, cat='movies')
        if results:
            results = pd.DataFrame.from_dict(results)
            results['size'] = (pd.to_numeric(results['size'].str[:-2])/1024/1024/1024).astype(float).round(2).astype(str) + " GB"
            results['magnet'] = results['link'].apply(lambda x: f'<a target="_blank" href="{x}">Download</a>')
            results = results[['name', 'size', 'seeds', 'leech', 'magnet']]
            st.markdown(results.to_html(render_links=True, escape=False),unsafe_allow_html=True)
            # st.dataframe(results)
            # print(results[['name', 'size', 'seeds', 'leech', 'link']])

        # else:
        #     st.error("No results found")

if __name__=="__main__":
    main()
print()

# import streamlit as st
# import pandas as pd

# data = {'Name':['John', 'Mike', 'Sara'],
#         'Age':[25, 22, 31],
#         'City':['New York', 'Chicago', 'Los Angeles']}
# df = pd.DataFrame(data)

# def show_details(row):
#     # show details logic
#     st.write("You selected:", row)

# def main():
#     st.title("Clickable Dataframe")
#     df.style.set_caption("Click on a row to show details")
#     st.dataframe(df.style.apply(lambda x: ['background: lightblue' if x.name == i else '' for i in range(len(df))], axis=1))
#     row_id = st.empty()
#     if row_id is not None:
#         row_id = int(row_id)
#         show_details(df.loc[row_id])

# if __name__=="__main__":
#     main()