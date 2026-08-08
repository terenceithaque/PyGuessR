# Script that allows listing themes
from pathlib import Path

# Get the path to the 'quizz' folder
QUIZZ_DIR = Path(__file__).resolve().parent / "quizz"


def get_themes() -> list[str]:
    """Returns the list of quizz themes available in the quizz folder"""
    return [theme.name for theme in QUIZZ_DIR.iterdir() if theme.is_dir()]


def get_theme_abspath(theme:str) -> Path:
    """Returns the absolute file path of a theme folder."""

    theme_path = QUIZZ_DIR / theme

    if not theme_path.is_dir():
        raise FileNotFoundError(
            f"The requested theme ({theme}) does not exist."
        )

    return theme_path


def get_quizz_abspath(theme:str, level:int=1) -> Path:
    """Returns the absolute file path to the quizz file for a theme and difficulty level."""

    return get_theme_abspath(theme) / f"level_{level}.json"