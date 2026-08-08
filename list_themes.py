# Script that allows listing themes
import os

def get_themes() -> list:
    """Returns the list of quizz themes available in the quizz folder."""

    # Get the directory in which the script is located
    script_dir = os.path.abspath(os.path.dirname(__file__))

    return os.listdir(f"{script_dir}/quizz")


def get_theme_abspath(theme:str) -> str:
    """Returns the absolute file path of a theme folder."""

    script_dir = os.path.abspath(os.path.dirname(__file__))

    assert theme in os.listdir(f"{script_dir}/quizz"), f"The requested theme ({theme}) does not exist."

    return os.path.abspath(f"{script_dir}/quizz/{theme}")


def get_quizz_abspath(theme:str, level:int=1) -> str:
    """Returns the absolute file path to the quizz file corresponding to the corresponding themes and difficulty levels."""

    theme_path = get_theme_abspath(theme) # Get the absolute file path to the theme's folder
    return os.path.join(theme_path, f"level_{level}.json")