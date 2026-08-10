"""quizz_window.py offers a QuizzWindow class which represents a full quizz window"""
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QGridLayout
from json_quizz import *
import random


class QuestionPage:
    def __init__(self, question_number:str, json_content:dict) -> None:
        """A page containing a question in the quizz referenced by a question number (string) with its content and widgets.
        - question_number: a string containing the number referencing the question.
        - json_content: the JSON content of the quizz file."""

        self.question_number = question_number
        self.json_content = json_content



class QuizzWindow(QMainWindow):
    def __init__(self, quizz_file:str) -> None:
        """A QuizzWindow object represents a game window inside of which random questions from the given JSON quizz file appear.
        - quizz_file: the path to JSON file containing the quizz questions."""
        super().__init__()

        self.setWindowTitle(f"{quizz_file} - PyGuessR")

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