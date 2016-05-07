class Emoji:
    def __init__(self, content):
        self.soup = content

        self._aliases = None
        self._codepoints = None
        self._description = None
        self._platforms = None
        self._shortcodes = None

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
            platform_section = self.soup.find('section', {'class': 'vendor-list'})
            for title in platform_section.findAll('h2'):
                self._platforms.append(title.text)
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
                    self._aliases.append(" ".join(alias.text.split()[1:]))
        return self._aliases
    