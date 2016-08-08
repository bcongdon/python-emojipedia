# python-emojipedia
[![Build Status](https://travis-ci.org/bcongdon/python-emojipedia.svg?branch=master)](https://travis-ci.org/benjamincongdon/python-emojipedia)
[![Code Climate](https://codeclimate.com/github/benjamincongdon/python-emojipedia/badges/gpa.svg)](https://codeclimate.com/github/benjamincongdon/python-emojipedia)
[![PyPI version](https://badge.fury.io/py/emojipedia.svg)](https://badge.fury.io/py/emojipedia)
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
print taco.description # "A taco; a Mexican food item displayed with a variety of fillings. ..."

# Emojipedia codepoints
print taco.codepoints # "U+1F32E"

# Emojipedia listed platforms 
# Contains title, Emojipedia platform url, and platform specific emoji img url
platforms = taco.platforms 
print platforms[0] # {'title': 'Apple', 'platform_url': '...', 'platform_img': '...'}

joy = Emojipedia.search('face-with-tears-of-joy')
# Emoji shortcodes
joy.shortcodes # ":joy:"

# Search for emoji by emoji
smirk = Emojipedia.search('😏')
# Custom Emoji string preview
print str(smirk) # <Emoji - 'Smirking Face' - character: 😏, description: A sly smile, often u...>
```
