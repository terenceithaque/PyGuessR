"""player.py offers a Player class handling player-related data and methods.\n
It also provides a NameInput class which represents a window inside of which the player can input its pseudo."""
from pathlib import Path
from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
import hashlib
from profiles import *


class NameInput(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Input your player name")
        self.resize(300, 200)


        # Set the layout and widgets
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type pseudo here...")

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.ok_button.setDisabled(True)

        self.name_input.textChanged.connect(self.enable_ok_button)

        layout.addWidget(self.name_input)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)


    def enable_ok_button(self) -> None:
        """Enables the 'OK' if the player filled the name input, and disables it if not."""

        # Disable the button if the name input is empty
        if len(self.name_input.text()) == 0:
            self.ok_button.setDisabled(True)

        else:
            self.ok_button.setEnabled(True)    
    

class Player:
    def __init__(self, pseudo:str="New player") -> None:
        """The player class handles various things related to the player (pseudo, id, score, etc).
        - pseudo: the pseudonym attributed to the player, 'New player' by default."""

        self.score = 0
        self.pseudo = pseudo
        self.__hashed_pseudo = self.generate_id()

        self.id = self.generate_id()

        # Create the "player_profiles" folder if it does not exist
        create_profiles_folder()

        print("Player profile files :", get_profile_files())

        self.player_profiles = load_profiles_file()
        print("Player profiles :", self.player_profiles)
        print(f"{self.__hashed_pseudo} already existing in player profiles:", self.pseudo_exists())

        save_profile(self, self.player_profiles)

    def generate_id(self) -> str:
        """Returns a hash of the player's pseudo which acts as a unique ID for that player."""

        # Hash the player's pseudo using SHA256
        hashed_pseudo = hashlib.sha256(self.pseudo.encode("utf-8")).hexdigest()

        return hashed_pseudo

    def pseudo_exists(self) -> bool:
        """Returns True if the player's hashed pseudo is present within the player profiles or False otherwise."""

        return self.__hashed_pseudo in self.player_profiles.keys()


# Runs only if the script is executed directly
if __name__ == "__main__":
    player = Player()
    print(f"Player ID : {player.id}")        