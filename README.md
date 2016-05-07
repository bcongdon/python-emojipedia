# python-emojipedia
[![Build Status](https://travis-ci.org/benjamincongdon/python-emojipedia.svg?branch=master)](https://travis-ci.org/benjamincongdon/python-emojipedia)
[![Code Climate](https://codeclimate.com/github/benjamincongdon/python-emojipedia/badges/gpa.svg)](https://codeclimate.com/github/benjamincongdon/python-emojipedia)
>Emoji data from Emojipedia :sunglasses:

**Work in progress**

## Example:
```
from emojipedia import Emojipedia

taco = Emojipedia.search('taco')

print taco.description # "A taco; a Mexican food item displayed with a variety of fillings. ..."
print taco.codepoints # "U+1F32E"
print taco.platforms # "['Apple', 'Google', 'Samsung', 'LG', 'Twitter', 'Emoji One', 'Emojipedia']"
```