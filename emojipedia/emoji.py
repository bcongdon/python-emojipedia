class Emoji:
    def __init__(self, content):
        self.soup = content

        self._aliases = None
        self._character = None
        self._codepoints = None
        self._description = None
        self._platforms = None
        self._shortcodes = None
        self._title = None

    @property
    def description(self):
        if not self._description:
            text = self.soup.find('section', {'class': 'description'}).text
            if text:
                self._description = text.strip()
        return self._description

    @property
    def codepoints(self):
        if not self._codepoints:
            code_list = self.soup.find(text='Codepoints').findNext('ul')
            if code_list:
                nonunique = [child.text.split()[1]
                             for child in code_list.findChildren()]
                self._codepoints = list(set(nonunique))
        print self._codepoints
        return self._codepoints

    @property
    def platforms(self):
        if not self._platforms:
            self._platforms = list()
            platform_section = self.soup.find('section',
                                              {'class': 'vendor-list'})
            for vendor in platform_section.findAll('li'):
                vendor_title = vendor.findNext('h2')
                vendor_img = vendor.find('div', {'class': 'vendor-image'})

                platform = {
                    'title': vendor_title.text,
                    'platform_url': vendor_img.find('a')['href'],
                    'platform_image': vendor_img.find('img')['src'],
                }
                self._platforms.append(platform)
        return self._platforms

    @property
    def shortcodes(self):
        if not self._shortcodes:
            codelist = self.soup.find(text='Shortcodes')
            if codelist:
                self._shortcodes = codelist.findNext('ul').text.strip()
        return self._shortcodes

    @property
    def aliases(self):
        if not self._aliases:
            alias_section = self.soup.find('section', {'class': 'aliases'})
            if alias_section:
                self._aliases = list()
                for alias in alias_section.findAll('li'):
                    # Remove initial emoji + whitespace
                    self._aliases.append(" ".join(alias.text.split()[1:]))
        return self._aliases

    @property
    def title(self):
        if not self._title:
            # Remove initial emoji + whitespace
            self._title = " ".join(self.soup.find('h1').text.split()[1:])
        return self._title

    @property
    def character(self):
        if not self._character:
            self._character = self.soup.find('h1').text.split()[0]
        return self._character

    def __str__(self):
        string = u"<Emoji - '{0}' - character: {2}, description: {1}>"
        string = string.format(self.title,
                               self.description[:20] + "...",
                               self.character)
        return string.encode('utf-8')

    def __repr__(self):
        return self.__str__()
