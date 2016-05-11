from emojipedia import Emojipedia
import nose.tools


@nose.tools.raises(UserWarning)
def test_invalid_url():
    Emojipedia.search('not a valid url')


@nose.tools.raises(UserWarning)
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
    wink = Emojipedia.search('winking-face')
    correct = ['Apple', 'Google', 'Microsoft', 'Samsung',
               'LG', 'HTC', 'Twitter', 'Facebook', 'Mozilla', 'Emoji One']

    # Order not important
    assert set([x['title'] for x in wink.platforms]) == set(correct)
    for platform in wink.platforms:
        assert 'title' in platform
        assert ('platform_url' in platform and
                platform['platform_url'].startswith('/'))
        assert ('platform_image' in platform and
                platform['platform_image'].startswith('http'))


def test_emoji_shortcodes():
    joy_tears = Emojipedia.search('face-with-tears-of-joy')
    correct = ':joy:'
    assert joy_tears.shortcodes == correct


def test_emoji_without_shortcode():
    wind_blow = Emojipedia.search('wind-blowing-face')
    assert wind_blow.shortcodes is None


def test_emoji_aliases():
    hands = Emojipedia.search('person-with-folded-hands')
    correct = ['High Five Emoji',
               'Please Emoji',
               'Praying Hands Emoji',
               'Thank You Emoji']
    assert set(hands.aliases) == set(correct)


def test_emoji_no_aliases():
    heavy_plus = Emojipedia.search('heavy-plus-sign')
    assert heavy_plus.aliases is None


def test_emoji_title():
    taco = Emojipedia.search('taco')
    assert taco.title == "Taco"


def test_emoji_character():
    taco = Emojipedia.search('taco')
    # Python Unicode silliness
    assert taco.character.encode('unicode_escape') == '\\U0001f32e'
