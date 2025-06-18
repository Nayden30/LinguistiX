from pathlib import Path
from typing import Iterable, List


def read_corpus(paths: Iterable[str]) -> str:
    """Read and concatenate text from multiple files."""
    texts: List[str] = []
    for p in paths:
        path = Path(p)
        text = path.read_text(encoding="utf-8")
        texts.append(text)
    return "\n".join(texts)
