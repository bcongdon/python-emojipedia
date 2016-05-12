from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
from emoji import Emoji


class Emojipedia:
    @staticmethod
    def search(query):
        return Emoji(Emojipedia.get_emoji_page(query))

    @staticmethod
    def random():
        return Emoji(Emojipedia.get_emoji_page('random'))

    @staticmethod
    def valid_emoji_page(soup):
        """
        (soup) -> bool
        """
        _type = soup.find('meta', {'property': 'og:type'})
        return (_type and _type['content'] == 'article')

    @staticmethod
    def get_emoji_page(query):
        response = requests.get('http://emojipedia.org/' + query.decode('utf-8', 'backslashreplace'))
        if response.status_code != 200:
            raise UserWarning('Could not get emojipedia page for \'{0}\''
                              .format(query))

        soup = BeautifulSoup(response.text)
        if not Emojipedia.valid_emoji_page(soup):
            raise UserWarning('Query did not yield a emoji entry')
        return soup
