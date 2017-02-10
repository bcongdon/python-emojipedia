from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
from .emoji import Emoji


class Emojipedia:
    all_categories = ['people', 'nature', 'food-drink', 'activity',
                      'travel-places', 'objects', 'symbols', 'flags']

    @staticmethod
    def search(query):
        return Emoji(Emojipedia.get_emoji_page(query))

    @staticmethod
    def random():
        return Emoji(Emojipedia.get_emoji_page('random'))

    @staticmethod
    def category(query):
        if query not in Emojipedia.all_categories:
            raise ValueError('{} is not a valid emoji category.'.format(query))
        soup = Emojipedia._get_page(query)
        emoji_list = soup.find('ul', {'class': 'emoji-list'})
        if not emoji_list:
            raise ValueError('Could not extract emoji list')
        emojis = []
        for emoji_entry in emoji_list.find_all('li'):
            url = emoji_entry.find('a')['href']
            emoji_text = emoji_entry.text.split(' ')
            title = ' '.join(emoji_text[1:])
            char = emoji_text[0]
            e = Emoji(url=url)
            e._title = title
            e._character = char
            emojis.append(e)
        return emojis

    @staticmethod
    def all():
        soup = Emojipedia._get_page('emoji')
        emoji_list = soup.find('table', {'class': 'emoji-list'})
        if not emoji_list:
            raise ValueError('Could not extract emoji list')
        emojis = []
        for emoji_entry in emoji_list.find_all('tr'):
            emoji_link = emoji_entry.find('a')
            emoji_text = emoji_link.text.split(' ')
            emoji_row, codepoints = emoji_entry.find_all('td')

            e = Emoji(url=emoji_link['href'])
            e._codepoints = codepoints.text.split(', ')
            e._character, e._title = emoji_text[0], ' '.join(emoji_text[1:])
            emojis.append(e)
        return emojis

    @staticmethod
    def _valid_emoji_page(soup):
        """
        (soup) -> bool
        """
        _type = soup.find('meta', {'property': 'og:type'})
        return (_type and _type['content'] == 'article')

    @staticmethod
    def _get_page(query):
        response = requests.get('http://emojipedia.org/' + query)
        if response.status_code != 200:
            raise RuntimeError('Could not get emojipedia page for \'{0}\''
                               .format(query))
        return BeautifulSoup(response.text, 'html.parser')

    @staticmethod
    def get_emoji_page(query):
        soup = Emojipedia._get_page(query)
        if not Emojipedia._valid_emoji_page(soup):
            raise ValueError('Query did not yield a emoji entry')
        return soup
