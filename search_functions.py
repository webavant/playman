from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog, message_dialog
import json, xmltodict, pafy
from theme import theme
from cache_request import *
from youtube_search import YoutubeSearch

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
    if not len(selections): return
    choice = radiolist_dialog(title="Playman", text="Choose one:", values=selections, style=theme).run()

    return pafy.new(choice).getbestaudio().url

def search_radio():
    search_term = input_dialog(title='Playman',text='search radio', style=theme).run()

    filename = f'search_radio_{search_term}.json'
    url = 'http://de1.api.radio-browser.info/json/stations/search'
    params = {'name': search_term}
    results = json.loads(get_request(filename, url, params))

    selections = [ ( l.get('url'), l.get('name') ) for l in results ]
    if not len(selections): return
    return radiolist_dialog(title="Playman", text="Choose one:", values=selections, style=theme).run()
