from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog, message_dialog
import re, json, xmltodict
from yt_dlp import YoutubeDL
from theme import theme
from cache_request import *
from youtube_search import YoutubeSearch
from pprint import pprint

def search_podcasts():
    search_term = input_dialog(title='Playman',text='search podcasts', style=theme).run()

    filename = f'search_podcast_{search_term}.json'
    url = 'https://itunes.apple.com/search'
    params = {'term': search_term, 'entity': 'podcast'}
    results = json.loads(get_request(filename, url, params)).get('results')

    selections = [ (
        { 'id': l.get('collectionId'), 'url': l.get('feedUrl') },
        l.get('collectionName')
    ) for l in results ]
    
    if not len(selections): return
    choice = radiolist_dialog(title="Playman", text="Choose one:", values=selections, style=theme).run()
    x = xmltodict.parse(get_request(f'rss_{choice.get("id")}.xml', choice.get('url')))

    selections = [(l.get('enclosure').get('@url'), f'{l.get("pubDate")} – {l.get("title")}') for l in x.get('rss').get('channel').get('item')]
    return radiolist_dialog(title="Playman", text="Choose one:", values=selections, style=theme).run()

def  search_youtube():
    search_term = input_dialog(title='Playman',text='search youtube', style=theme).run()

    selections = [(f'https://www.youtube.com/{l.get("url_suffix")}', l.get("title")) for l in YoutubeSearch(search_term).to_dict()]

    for i in range(len(selections)):
        selections[i] = (re.sub(r'.*v=([^&]+).*', r'\1', selections[i][0]), selections[i][1])

    if not len(selections): return
    choice = radiolist_dialog(title="Playman", text="Choose one:", values=selections, style=theme).run()

    yt_dl_opts = {'cookiefile': 'cookie.txt', 'quiet': True, 'force_generic_extractor': True, 'noplaylist': True, 'simulate': True, 'format': 'bestaudio/best', 'skip_download': True}
    info = YoutubeDL(yt_dl_opts).extract_info(choice, download=False)
    for f in info['formats']:
        if f.get('acodec') != 'none' and f.get('url'):
            url = f.get('url')
            break

    if not url: return
    return url

def search_radio():
    search_term = input_dialog(title='Playman',text='search radio', style=theme).run()

    filename = f'search_radio_{search_term}.json'
    url = 'http://de1.api.radio-browser.info/json/stations/search'
    params = {'name': search_term}
    results = json.loads(get_request(filename, url, params))

    selections = [ ( l.get('url'), l.get('name') ) for l in results ]
    if not len(selections): return
    return radiolist_dialog(title="Playman", text="Choose one:", values=selections, style=theme).run()
