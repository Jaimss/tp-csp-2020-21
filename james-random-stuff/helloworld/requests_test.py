import requests
from pprint import pprint


def get_word_json(word):
    r = requests.post(f'{words_api}/{word}')
    return r.json()


words_api = 'https://lingua-robot.p.rapidapi.com/language/v1/entries/en/'
pprint(get_word_json('a'))
