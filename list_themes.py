# Script that allows listing themes
import os

def get_themes() -> list:
    """Returns the list of quizz themes available in the quizz folder."""

    # Get the directory in which the script is located
    script_dir = os.path.abspath(os.path.dirname(__file__))

    return os.listdir(f"{script_dir}/quizz")