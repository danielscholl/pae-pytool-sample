"""Core text-statistics functions."""

from __future__ import annotations


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def char_count(text: str, *, include_spaces: bool = True) -> int:
    """Return the number of characters in *text*.

    When *include_spaces* is False, all whitespace is ignored.
    """
    if include_spaces:
        return len(text)
    return len("".join(text.split()))


def reverse_words(text: str) -> str:
    """Return *text* with whitespace-separated words in reverse order."""
    return " ".join(reversed(text.split()))
