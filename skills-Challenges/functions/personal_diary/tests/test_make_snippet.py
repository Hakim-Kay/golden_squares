from lib.make_snippet import *


# Test 1:
def test_string_longer_than_five_words():
    assert (
        make_snippet("This is a string longer than five words")
        == "This is a string longer..."
    )


# Test 2:
def test_string_with_exactly_five_words():
    assert make_snippet("This is exactly five words") == "This is exactly five words"


# Test 3:
def test_string_is_less_than_five_words():
    assert make_snippet("Short string") == "Short string"
