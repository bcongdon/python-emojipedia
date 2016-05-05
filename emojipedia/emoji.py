class Emoji:
    def __init__(self, content):
        self.soup = content
        self._description = None
        self._codepoints = None

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
                self._codepoints = list(set([child.text[3:] for child in code_list.findChildren()]))
        print self._codepoints
        return self._codepoints
