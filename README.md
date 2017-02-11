# python-emojipedia
[![Build Status](https://travis-ci.org/bcongdon/python-emojipedia.svg?branch=master)](https://travis-ci.org/bcongdon/python-emojipedia)
[![Code Climate](https://codeclimate.com/github/bcongdon/python-emojipedia/badges/gpa.svg)](https://codeclimate.com/github/bcongdon/python-emojipedia)
[![PyPI version](https://badge.fury.io/py/Emojipedia.svg)](https://badge.fury.io/py/Emojipedia)
[![Test Coverage](https://codeclimate.com/github/bcongdon/python-emojipedia/badges/coverage.svg)](https://codeclimate.com/github/bcongdon/python-emojipedia/coverage)
>Emoji data from Emojipedia :sunglasses:

## Installation:
To install, simply run `pip install emojipedia`.

To install from source, run the following from within the main project directory:

```
python setup.py build
python setup.py install
```

## Example:
```
from emojipedia import Emojipedia

# Search for emoji by title
taco = Emojipedia.search('taco')

# Emojipedia description
print(taco.description)  # "A taco; a Mexican food item displayed with a variety of fillings. ..."

# Emojipedia codepoints
print(taco.codepoints)  # "U+1F32E"

# Emojipedia listed platforms 
# Contains title, Emojipedia platform url, and platform specific emoji img url
platforms = taco.platforms 
print(platforms[0])  # {'title': 'Apple', 'platform_url': '...', 'platform_img': '...'}

joy = Emojipedia.search('face-with-tears-of-joy')
# Emoji shortcodes
joy.shortcodes  # ":joy:"

# Search for emoji by emoji
smirk = Emojipedia.search('😏')
# Custom Emoji string preview
print(str(smirk))  # <Emoji - 'Smirking Face' - character: 😏, description: A sly smile, often u...>

# Get a category of emoji
people = Emojipedia.category('people')
people[0].title  # <Emoji - 'Grinning Face' - character: 😀, description: A face with a big op...>
print(len(people))  # 306

# Get all the emoji
emojis = Emojipedia.all()
print(len(emojis))  # 2621
for emoji in emojis:
    print(emoji.title)
```

## Contributing

Contributions to `python-emojipedia` are welcomed! 😁

1. Fork the repo.
2. Create a new feature branch.
3. Add your feature / make your changes.
4. Install [pep8](https://pypi.python.org/pypi/pep8) and run `pep8 *.py` in the root project directory to lint your changes. Fix any linting errors.
5. Create a PR.
6. ???
7. 🎉 Profit. 🎉
