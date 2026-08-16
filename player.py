"""player.py offers a Player class handling player-related data and methods."""
from pathlib import Path
import hashlib
from profiles import *
    

class Player:
    def __init__(self, pseudo:str="New player") -> None:
        """The player class handles various things related to the player (pseudo, id, score, etc).
        - pseudo: the pseudonym attributed to the player, 'New player' by default."""

        self.score = 0
        self.pseudo = pseudo

        self.id = self.generate_id()

        # Create the "player_profiles" folder if it does not exist
        create_profiles_folder()

        print("Player profile files :", get_profile_files())

        self.profile_files = load_profiles_file()
        self.player_profiles = load_profiles_file()
        print("Player profiles :", self.player_profiles)

        save_profile(self, self.player_profiles)

    def generate_id(self) -> str:
        """Returns a hash of the player's pseudo which acts as a unique ID for that player."""

        # Hash the player's pseudo using SHA256
        hashed_pseudo = hashlib.sha256(self.pseudo.encode("utf-8")).hexdigest()

        return hashed_pseudo


# Runs only if the script is executed directly
if __name__ == "__main__":
    player = Player()
    print(f"Player ID : {player.id}")        