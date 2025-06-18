from linguistix.analysis.tokenization import tokenize
from linguistix.analysis.frequency import word_frequencies


def test_word_frequencies():
    text = "Hello world hello"
    tokens = tokenize(text)
    freq = word_frequencies(tokens)
    assert freq["hello"] == 2
    assert freq["world"] == 1
