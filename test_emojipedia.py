# -*- coding: utf-8 -*-

from emojipedia import Emojipedia, Emoji
import nose.tools
from nose.tools import timed
from nose import run
from flaky import flaky
import unittest


@nose.tools.raises(RuntimeError)
def test_invalid_url():
    Emojipedia.search('not a valid url')


@nose.tools.raises(ValueError)
def test_non_emoji_entry_query():
    Emojipedia.search('people')


def test_emoji_description():
    shrug = Emojipedia.search('shrug')
    correct = "A person shrugging"
    assert shrug.description.startswith(correct)


def test_emoji_codepoints():
    shrug = Emojipedia.search('shrug')
    correct = 'U+1F937'
    assert shrug.codepoints[0] == correct


def test_platforms():
    wink = Emojipedia.search('bug')
    correct = ['LG', 'Google', 'HTC', 'Apple', 'Samsung', 'Twitter',
               'Mozilla', 'Facebook', 'emojidex', 'Messenger', 'Microsoft']

    # Order not important
    assert set(correct) <= set([x.name for x in wink.platforms])
    for platform in wink.platforms:
        assert platform.name
        assert platform.image_url.startswith('http')


def test_emoji_shortcodes():
    joy_tears = Emojipedia.search('face-with-tears-of-joy')
    correct = ':joy:'
    assert joy_tears.shortcodes == correct


def test_emoji_without_shortcode():
    wind_blow = Emojipedia.search('wind-blowing-face')
    assert wind_blow.shortcodes is None


def test_emoji_aliases():
    hands = Emojipedia.search('person-with-folded-hands')
    correct = ['Please',
               'Prayer',
               'Thank You',
               'Namaste']
    assert set(hands.aliases) == set(correct)


def test_emoji_no_aliases():
    heavy_plus = Emojipedia.search('heavy-plus-sign')
    assert heavy_plus.aliases is None


def test_emoji_title():
    taco = Emojipedia.search('taco')
    assert taco.title == "Taco"


def test_emoji_character():
    taco = Emojipedia.search('taco')
    assert taco.character == u'🌮'


def test_emoji_repr():
    pizza = Emojipedia.search('slice-of-pizza')
    correct = (u"<Emoji - 'Pizza' - character: 🍕, "
               u"description: A slice of pepperoni...>")
    assert pizza.__unicode__() == correct
    assert pizza.__repr__() == pizza.__str__()


def test_emoji_category():
    people = Emojipedia.category('people')
    for e in people:
        assert e.title
        assert e.character


@flaky
@timed(15)
def test_all_emoji():
    all_emoji = Emojipedia.all()
    assert len(all_emoji) >= 2621
    for e in all_emoji:
        # Test private properties so we don't scrape Emojipedia
        # if this fails
        assert e._title
        assert e._character
        assert e._codepoints


def test_lazy_parsing_article():
    article_emoji = Emoji(url='/heavy-plus-sign')
    assert article_emoji.title
    assert article_emoji.character
    assert article_emoji.description
    assert article_emoji.codepoints

    generic_emoji = Emoji(url=u'/emoji/🌮')
    assert generic_emoji.title
    assert generic_emoji.character
    assert generic_emoji.description
    assert generic_emoji.codepoints

if __name__ == '__main__':
    run()
