"""
Tests

Regularly conjugated english verbs.
    "talk", "talks", "talking", and "talked" to all be forms of "talk".
Regularly pluralized english nouns.
    "cat" and "cats" to be forms of "cat".
"""

import pytest

from app.routes import _process_word


def test_converts_to_lowercase():
    assert _process_word('Word') == 'word'


def test_pluralized_nouns():
    assert _process_word('cats') == _process_word('cat')
    assert _process_word('potatoes') == _process_word('potato')
    assert _process_word('scarves') == _process_word('scarf')
    assert _process_word('cherries') == _process_word('cherry')
    assert _process_word('embryos') == _process_word('embryo')

    # fails
    with pytest.raises(AssertionError):
        assert _process_word('cactuses') == _process_word('cactus')


def test_conjugated_verbs():
    assert _process_word('talks') == _process_word('talk')
    assert _process_word('talking') == _process_word('talk')
    assert _process_word('talked') == _process_word('talk')


def test_random_words():
    assert _process_word('is') == 'is'
    assert _process_word('success') == 'success'
