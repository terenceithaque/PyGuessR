"""player.py offers a Player class handling player-related data and methods."""
from pathlib import Path
import random


def create_profiles_folder() -> None:
    """Creates the player_profiles directory within the location of the player.py script"""

    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)

    profiles_folder.mkdir(exist_ok=True)



def get_profiles() -> list:
    """Returns the whole list of file names contained inside the player_profiles directory."""

    script_dir = Path(__file__).resolve().parent # Get the directory hosting the script
    profiles_folder_path = script_dir / "player_profiles"
    profiles_folder = Path(profiles_folder_path)

    return [file.name for file in profiles_folder.iterdir()]
    

class Player:
    def __init__(self, pseudo:str="New player") -> None:
        """The player class handles various things related to the player (pseudo, id, score, etc).
        - pseudo: the pseudonym attributed to the player, 'New player' by default."""

        self.score = 0
        self.pseudo = pseudo

        self.id = self.generate_id()

        # Create the "player_profiles" folder if it does not exist
        create_profiles_folder()

        print("Player profiles :", get_profiles())

    def generate_id(self, id_length:int=7) -> int:
        """Generates an ID (integer) which is tied to the player.
        - id_length : the length of the generated ID, 7 by default."""

        # Assertions
        assert id_length > 0, f"The length of the ID must be a strictly positive number."

        player_id = "" # Initialize the ID string as empty

        for i in range(id_length):
            player_id += str(random.randint(0, 9))

        return int(player_id)


# Runs only if the script is executed directly
if __name__ == "__main__":
    player = Player()
    print(f"Player ID : {player.id}")        