"""quizz_window.py offers a QuizzWindow class which represents a full quizz window"""
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QGridLayout
from json_quizz import *
import random


class QuizzWindow(QMainWindow):
    def __init__(self, quizz_file:str) -> None:
        """A QuizzWindow object represents a game window inside of which random questions from the given JSON quizz file appear.
        - quizz_file: the path to JSON file containing the quizz questions."""
        super().__init__()

        # The QStackedWidget allows to handle several quizz pages all by displaying only one at a time
        central_widget = QStackedWidget()
        self.setCentralWidget(central_widget)

        # Set the grid layout
        parent_layout = QGridLayout()
        self.setLayout(parent_layout)

        # Load the quizz from the file
        self.quizz = JSONQuizzFormat(quizz_file)

        # Choose the questions that will be presented to the player
        self.quizz_questions = self.quizz.question_serie(random.randint(1, len(self.quizz.quizz_content)))