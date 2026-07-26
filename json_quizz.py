"""This script handles the JSON format used for the quizz and provides a JSONQuizzFormat class."""
import json


class JSONQuizzFormat:
    """This class acts as an abstraction for the JSON format which is used for the quizz."""

    def __init__(self, json_file:str) -> None:
        """Initializes the quizz in JSON format.
        json_file : the JSON file from which the quizz content (questions, answers, etc.) is parsed by using the json module."""

        self.file = json_file
        