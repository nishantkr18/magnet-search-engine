import libtorrent as lt
import time
import sys
import streamlit as st


def download_torrent(magnet_link, save_path='./downloads/'):
    ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

    h = lt.add_magnet_uri(ses, magnet_link, {'save_path': save_path})
    s = h.status()
    print('starting', s.name)

    placeholder = st.empty()
    h.set_sequential_download(True)

    while (not s.is_seeding):
        s = h.status()

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
            s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
            s.num_peers, s.state), end=' ')
        placeholder.write('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
            s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
            s.num_peers, s.state))

        # alerts = ses.pop_alerts()
        # for a in alerts:
        #     if a.category() & lt.alert.category_t.error_notification:
        #         print(a)

        sys.stdout.flush()

        time.sleep(1)

    print(h.status().name, 'complete')


if __name__ == '__main__':

    magnet_link = 'magnet:?xt=urn:btih:A437EB6825720E780C4C33063476499EC6B57276&dn=Horrible+Bosses+%282011%29+1080p+BrRip+x264+-+YIFY&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fwww.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fretracker.lanta-net.ru%3A2710%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce'
    download_torrent(magnet_link=magnet_link)