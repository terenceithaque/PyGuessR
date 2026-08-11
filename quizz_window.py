"""quizz_window.py offers a QuizzWindow class which represents a full quizz window"""
from PyQt6.QtWidgets import QMainWindow, QLabel, QStackedWidget, QGridLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from json_quizz import *
import random


class QuestionPage(QWidget):
    def __init__(self, question_number:str, json_content:dict) -> None:
        """A page containing a question in the quizz referenced by a question number (string) with its content and widgets.
        - question_number: a string containing the number referencing the question.
        - json_content: the JSON content of the quizz file."""
        super().__init__()


        parent_layout = QGridLayout()
        self.setLayout(parent_layout)

        self.question_number = question_number
        self.json_content = json_content

        print(json_content)
        print(f"Key '{question_number}' in json_content :", question_number in json_content.keys())
        self.question = json_content[question_number] # Get the question referenced by the number

        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(16)

        self.question_title = QLabel(self.question["content"])
        self.question_title.setFont(title_font)
        self.question_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        parent_layout.addWidget(self.question_title)
        



class QuizzWindow(QMainWindow):
    def __init__(self, quizz_file:str) -> None:
        """A QuizzWindow object represents a game window inside of which random questions from the given JSON quizz file appear.
        - quizz_file: the path to JSON file containing the quizz questions."""
        super().__init__()

        self.setWindowTitle(f"{quizz_file} - PyGuessR")

        # The QStackedWidget allows to handle several quizz pages all by displaying only one at a time
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Set the grid layout
        parent_layout = QGridLayout()
        self.setLayout(parent_layout)

        # Load the quizz from the file
        self.quizz = JSONQuizzFormat(quizz_file)

        # Choose the questions that will be presented to the player
        self.quizz_questions = self.quizz.question_serie(random.randint(1, len(self.quizz.quizz_content)))

        self.current_question_index = 0 # Current question index in the serie
        self.current_question_number = str(self.quizz_questions[0])
        self.current_question = QuestionPage(self.current_question_number, self.quizz.quizz_content["questions"])
        self.central_widget.addWidget(self.current_question)
        self.central_widget.setCurrentIndex(0)