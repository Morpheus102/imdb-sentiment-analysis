"""
Text preprocessing utilities for the IMDB sentiment project.
"""

from typing import Iterable, List
import re

def basic_clean(text: str) -> str:
    """
    Very simple placeholder cleaner.
    Later we'll add:
    - lowercasing
    - removing HTML tags
    - maybe removing extra punctuation, etc.
    """
    return text.strip()


def clean_batch(texts: Iterable[str]) -> List[str]:
    """Apply basic_clean to a sequence of texts."""
    return [basic_clean(t) for t in texts]


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"<br\s*/?>", " ", text)  # remove HTML tags
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)  # remove weird symbols
    text = re.sub(r"\s+", " ", text)  # collapse multiple spaces
    return text.strip()

