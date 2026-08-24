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

    if not "profiles.json" in get_profile_files():
        profiles_file.touch()
        profiles_file.write_text("{}", encoding="utf-8")




def get_profile_files() -> list:
    """Returns the whole list of file names contained inside the player_profiles directory."""

    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)

    return [file.name for file in profiles_folder.iterdir()]


def save_profile(player, profiles:dict) -> None:
    """Saves the informations of the given Player object under profiles.json
    - player: an instance of the Player object
    - profiles: a dictionnary containing all player profiles."""

    player_id = str(player.id) # Get and convert the player's ID


    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)
            
           
        
    # Locate and open the "profiles.json" file
    profiles_file_path = profiles_folder / "profiles.json"
    profiles_file = Path(profiles_file_path)

    with profiles_file.open("w", encoding="utf-8") as f:
        profiles[player_id] = {
            "score": player.score,
            "xp": player.xp
        }

        json.dump(profiles, f, indent=4)






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
