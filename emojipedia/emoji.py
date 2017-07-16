# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import six

from collections import namedtuple

Platform = namedtuple('Platform', ['image_url', 'name'])


class Emoji:
    def __init__(self, soup=None, url=None):
        self._soup_data = soup
        self._url = url
        if not (soup or url):
            raise ValueError('Emoji needs one of soup or url to be '
                             'initialized.')

        self._aliases = None
        self._character = None
        self._codepoints = None
        self._description = None
        self._platforms = None
        self._shortcodes = None
        self._title = None

    def _get_emoji_article_url(self):
        response = requests.get('http://emojipedia.org' + self._url)
        if response.status_code != 200:
            raise RuntimeError('Could not get emojipedia page for '
                               "'{}'".format(self._url))

        soup = BeautifulSoup(response.text, 'html.parser')
        desc = soup.find('td', text=re.compile('Description'))

        if not desc:
            raise ValueError('Could not parse emoji description')

        article_url = desc.parent.find_next('a')
        if not article_url:
            raise ValueError('Could not find emoji article')

        return article_url['href']

    @property
    def _soup(self):
        if not self._soup_data:
            # Check to see if we've given a general emoji page
            if 'emoji/' in self._url:
                # Resolve to emoji article
                self._url = self._get_emoji_article_url()

            response = requests.get('http://emojipedia.org' + self._url)
            if response.status_code != 200:
                raise RuntimeError('Could not get emojipedia page for \'{0}\''
                                   .format(self._url))
            self._soup_data = BeautifulSoup(response.text, 'html.parser')
        return self._soup_data

    @property
    def title(self):
        '''The title of the emoji

            Example: 'Person Shrugging'
        '''
        if not self._title:
            # Remove initial emoji + whitespace
            self._title = " ".join(self._soup.find('h1').text.split()[1:])
        return self._title

    @property
    def description(self):
        '''The Emojipedia description of the emoji

            Example: ``u'A person shrugging their shoulders to indicate ...'``
        '''
        if not self._description:
            text = self._soup.find('section', {'class': 'description'}).text
            if text:
                self._description = text.strip()
        return self._description

    @property
    def codepoints(self):
        '''A list of unicode codepoints for the emoji

            Example: ``['U+1F937']``
        '''
        if not self._codepoints:
            code_list = self._soup.find(text='Codepoints').findNext('ul')
            if code_list:
                nonunique = [child.text.split()[1]
                             for child in code_list.findChildren()]
                self._codepoints = list(set(nonunique))
        return self._codepoints

    @property
    def platforms(self):
        '''A list of platforms that the emoji is present on

            :rtype: [Platform]
        '''
        if not self._platforms:
            self._platforms = list()
            platform_section = self._soup.find('section',
                                               {'class': 'vendor-list'})
            for vendor in platform_section.findAll(
                    'div', {'class': 'vendor-rollout-target'}):
                vendor_title = vendor.findNext('a')
                vendor_img = vendor.find('div', {'class': 'vendor-image'})

                title = vendor_title.text
                platform_image = None
                if vendor_img and vendor_img.find('img'):
                    platform_image = vendor_img.find('img')['src']

                platform = Platform(name=title, image_url=platform_image)
                self._platforms.append(platform)
        return self._platforms

    @property
    def shortcodes(self):
        '''A list of shortcodes that represent the emoji

            Example: ``[:cop:]``
        '''
        if not self._shortcodes:
            codelist = self._soup.find(text='Shortcodes')
            if codelist:
                self._shortcodes = codelist.findNext('ul').text.strip()
        return self._shortcodes

    @property
    def aliases(self):
        '''A list of aliases associated with the emoji

            Example: ``[u'¯\_(ツ)_/¯', u'shrugging']``
        '''
        if not self._aliases:
            alias_section = self._soup.find('section', {'class': 'aliases'})
            if alias_section:
                self._aliases = list()
                for alias in alias_section.findAll('li'):
                    # Remove initial emoji + whitespace
                    self._aliases.append(" ".join(alias.text.split()[1:]))
        return self._aliases

    @property
    def character(self):
        '''The unicode character of the emoji

            Example: ``u'🤷'``
        '''
        if not self._character:
            self._character = self._soup.find('h1').text.split()[0]
        return self._character

    def __unicode__(self):
        string = u"<Emoji - '{0}' - character: {2}, description: {1}>"
        string = string.format(self.title,
                               self.description[:20] + u"...",
                               self.character)
        return string

    def __str__(self):
        return six.text_type(self.__unicode__()).encode('utf-8')

    def __repr__(self):
        return self.__str__()
