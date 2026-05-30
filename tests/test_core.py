from pae_pytool.core import char_count, reverse_words, word_count


def test_word_count_counts_whitespace_separated_words():
    assert word_count("hello world") == 2
    assert word_count("  spaced   out  words ") == 3


def test_word_count_empty_string_is_zero():
    assert word_count("") == 0
    assert word_count("   ") == 0


def test_char_count_includes_spaces_by_default():
    assert char_count("hello world") == 11


def test_char_count_can_exclude_spaces():
    assert char_count("hello world", include_spaces=False) == 10


def test_reverse_words_reverses_sentence_word_order():
    assert reverse_words("hello world foo") == "foo world hello"


def test_reverse_words_empty_string_stays_empty():
    assert reverse_words("") == ""


def test_reverse_words_normalizes_mixed_whitespace():
    assert reverse_words("  hello\tworld   foo  ") == "foo world hello"
