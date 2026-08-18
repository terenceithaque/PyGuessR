"""quizz_window.py offers a QuizzWindow class which represents a full quizz window"""
from PyQt6.QtWidgets import QMainWindow, QLabel, QStackedWidget, QGridLayout, QWidget, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from json_quizz import *
from player import *
import random


class QuestionPage(QWidget):
    def __init__(self, question_number:str, json_content:dict, player:Player) -> None:
        """A page containing a question in the quizz referenced by a question number (string) with its content and widgets.
        - question_number: a string containing the number referencing the question.
        - json_content: the JSON content of the quizz file
        - player: an instance of the Player object."""

        super().__init__()

        self.player = player

        self.parent_layout = QGridLayout()
        self.setLayout(self.parent_layout)

        self.question_number = question_number
        print("Question number :", self.question_number)
        self.json_content = json_content


        self.question_data= json_content[question_number] # Get the question referenced by the number
        self.question = JSONQuestion(
            self.question_data["content"], 
            self.question_data["answer"], 
            self.question_data["reward"],
            self.question_data["widgets"]

        )

        self.answered = False

        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(16)

        self.question_title = QLabel(self.question_data["content"])
        self.question_title.setFont(title_font)
        self.question_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parent_layout.addWidget(self.question_title)

        self.widgets = self.widgets_list()

        self.build_widgets()


    def build_widgets(self) -> None:
        """Builds the widgets tied to the question within the page based on JSON description."""

        x = 0 # x position of widget
        y = 1 # y position of widget

        for widget in self.widgets:
            widget_type = widget[0]
            widget_attribute = widget[1]

            # Build buttons
            if widget_type == "button":

                button_text = widget_attribute[5:] # The text of the button is specified after index 5
                button = QPushButton()
                button.setText(button_text)
                button.clicked.connect(lambda checked=False, text=button_text: self.check_answer(text))
                self.parent_layout.addWidget(button, x, y)
                y += 1
                if y == 6:
                    x += 1
                    y = 0

            # Build inputs
            elif widget_type == "input":

                input_length = int(widget_attribute[7:]) # The maximum input length is specified after index 7
                user_input = QLineEdit()
                user_input.setMaxLength(input_length)
                self.parent_layout.addWidget(user_input, x, y)
                y += 1
                if y == 6:
                    x += 1
                    y = 0


    def widgets_list(self) -> list:
        """Returns a (type, widgets) list of tuples containing all widgets as described in JSON."""

        widgets = [] # List containing widgets

        for widget_desc in self.question_data["widgets"]:

            # Widget type and attribute are separated by a space
            widget_type, attribute = widget_desc.split(" ")
            widgets.append((widget_type, attribute))

        return widgets

    def check_answer(self, answer:str) -> bool:
        """Checks if the player's answer is correct and make him gain or loose points based on the answer's correctness.
        Returns True if the question was answered correctly, False if not."""


        answer = answer.strip("'")
        

        if self.question.is_answer_correct(answer):
            self.player.score += self.question.reward
            self.answered = True
            return True

        else:
            if self.player.score >= self.question.reward:
                self.player.score -= self.question.reward
                self.answered = True
                return False

            
        



class QuizzWindow(QMainWindow):
    def __init__(self, quizz_file:str, player:Player) -> None:
        """A QuizzWindow object represents a game window inside of which random questions from the given JSON quizz file appear.
        - quizz_file: the path to JSON file containing the quizz questions
        - player: an instance of the Player object playing the quizz."""

        super().__init__()

        self.setWindowTitle(f"{quizz_file} - PyGuessR")

        # The QStackedWidget allows to handle several quizz pages all by displaying only one at a time
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.player = player

        # Set the grid layout
        parent_layout = QGridLayout()
        self.setLayout(parent_layout)

        # Load the quizz from the file
        self.quizz = JSONQuizzFormat(quizz_file)

        # Choose the questions that will be presented to the player
        self.quizz_questions = self.quizz.question_serie(random.randint(1, len(self.quizz.quizz_content)))

        self.current_question_index = 0 # Current question index in the serie
        self.current_question_number = str(self.quizz_questions[0])
        self.current_question = QuestionPage(self.current_question_number, self.quizz.quizz_content["questions"], self.player)
        self.central_widget.addWidget(self.current_question)
        self.central_widget.setCurrentIndex(0)