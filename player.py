"""player.py offers a Player class handling player-related data and methods."""

class Player:
    def __init__(self, pseudo:str="New player") -> None:
        """The player class handles various things related to the player (pseudo, id, score, etc).
        - pseudo: the pseudonym attributed to the player, 'New player' by default."""

        self.score = 0
        self.pseudo = pseudo