# a basic streamlit application.   

import streamlit as st

from driver_engine import Engine
from download import download_torrent


def show_results(results):
    st.markdown(results.to_html(render_links=True, escape=False),unsafe_allow_html=True)


def main():
    st.title("Movie search engine")
    search_text = st.text_input("Search for a movie:", value='The Matrix')
    button = st.button('Search')

    download_button = st.button('Download')
    if download_button:
        magnet_link = 'magnet:?xt=urn:btih:A437EB6825720E780C4C33063476499EC6B57276&dn=Horrible+Bosses+%282011%29+1080p+BrRip+x264+-+YIFY&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fwww.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fretracker.lanta-net.ru%3A2710%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce'
        download_torrent(magnet_link=magnet_link)
    
    play_button = st.button('Play')
    if play_button:
        video_file = open('downloads\Horrible Bosses (2011) [1080p]\Horrible.Bosses.2011.1080p.BluRay.x264.YIFY.mp4', 'rb')
        video_bytes = video_file.read()
        print("Loaded video")

        st.video(video_bytes)



    if button or search_text:
        with st.spinner('Looking up...'):
            with st.empty():
                for results in Engine().search(what=search_text, cat='movies'):
                    show_results(results) 

if __name__=="__main__":
    main()
print()