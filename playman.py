from time import sleep
import vlc
from search_functions import *

while True:
    results = radiolist_dialog(
        title="Playman",
        text="search from:",
        values=[
            ("radio", "radio streams"),
            ("podcast", "podcasts"),
            ("youtube", "youtube"),
        ],
        style=theme).run()

    if not results: break

    if results == 'podcast':
        uri = search_podcasts()
    elif results == 'youtube':
        uri = search_youtube()
    elif results == 'radio':
        uri = search_radio()

    if uri:
        instance = vlc.Instance()
        instance.log_unset()
        player = instance.media_player_new(uri)
        player.play()
        i = 0
        while i < 50 and str(player.get_state()) != 'State.Playing':
            i += 1
            sleep(.1)

        if str(player.get_state()) == 'State.Playing':
            message_dialog(title='Playman', text=str(player.get_state()), ok_text='stop', style=theme).run()
        else:
            message_dialog(title='Playman', text='stream ended', ok_text='ok', style=theme).run()
        player.stop()
