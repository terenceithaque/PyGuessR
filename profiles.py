"""profiles.py provides various functions to manage player profiles."""
import json
from pathlib import Path


def create_profiles_folder() -> None:
    """Creates the player_profiles directory within the location of the player.py script"""

    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)
    
    profiles_folder.mkdir(exist_ok=True)


    # Locate and create the "profiles.json" file if it does not exist
    profiles_file_path = profiles_folder / "profiles.json"
    profiles_file = Path(profiles_file_path)

    if not "profiles.json" in get_profiles():
        profiles_file.touch()
        profiles_file.write_text("{}", encoding="utf-8")




def get_profiles() -> list:
    """Returns the whole list of file names contained inside the player_profiles directory."""

    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)

    return [file.name for file in profiles_folder.iterdir()]


def load_profiles_file() -> dict:
    """Loads the profiles.json file located in the player_profiles folder and returns its content as a dictionnary."""

    profiles_content = {}

    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)
        
       
    
    # Locate and open the "profiles.json" file
    profiles_file_path = profiles_folder / "profiles.json"
    profiles_file = Path(profiles_file_path)

    with profiles_file.open("r", encoding="utf-8") as f:
        profiles_content = json.load(f)

    return profiles_content    
