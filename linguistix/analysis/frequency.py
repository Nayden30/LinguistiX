from collections import Counter
from typing import Iterable


def word_frequencies(tokens: Iterable[str]) -> Counter:
    """Return a Counter object with word frequencies."""
    return Counter(tokens)
