from genericpath import exists
from requests import request

def get_textfile(filepath, textstring=''):
    if exists(filepath):
        with open(filepath, 'r') as f:
            return f.read()
    elif textstring:
        with open(filepath, 'w') as f:
            f.write(textstring)
            return textstring

def get_request(filepath, url, params={}):
    if exists(filepath):
        return get_textfile(filepath)
    else:
        return get_textfile(filepath, request('GET', url, params=params).text)
