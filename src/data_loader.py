"""
Utilities to load and cache the IMDB dataset.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def get_data_dir() -> Path:
    """Return the path to the data directory, creating it if needed."""
    DATA_DIR.mkdir(exist_ok=True)
    return DATA_DIR
