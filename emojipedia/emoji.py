class Emoji:
    def __init__(self, content):
        self.soup = content
        self._description = None

    @property
    def description(self):
        if not self._description:
            text = self.soup.find('section', {'class': 'description'}).text
            self._description = text.strip()
            print text.strip()
        return self._description
