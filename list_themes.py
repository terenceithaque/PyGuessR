# Script that allows listing themes
from pathlib import Path
import json

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



def get_difficulty_levels(theme:str) -> list:
    """Returns the full list of diffculty levels (int) available for the given theme.
    - theme: the quizz theme for which the available difficulty levels are returned."""


    levels = []

    theme_folder = get_theme_abspath(theme)


    # Open all the JSON files and inspect the indicated difficulty level for each
    for json_file in theme_folder.iterdir():
        with json_file.open("r", encoding="utf-8") as f:
            file_content = json.load(f)
            levels.append(file_content["level"])


    return levels        

def get_quizz_abspath(theme:str, level:int=1) -> Path:
    """Returns the absolute file path to the quizz file for a theme and difficulty level."""

    return get_theme_abspath(theme) / f"level_{level}.json"