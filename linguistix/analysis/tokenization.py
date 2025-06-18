import re
from typing import List

_TOKEN_RE = re.compile(r"\b\w+\b", re.UNICODE)


def tokenize(text: str) -> List[str]:
    """Simple regex-based tokenizer returning lowercase tokens."""
    return _TOKEN_RE.findall(text.lower())
