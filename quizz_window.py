"""quizz_window.py offers a QuizzWindow class which represents a full quizz window"""
from PyQt6.QtWidgets import QMainWindow, QLabel, QStackedWidget, QGridLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from json_quizz import *
from player import *
from profiles import *
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

        # Question cenetered
        self.question_title = QLabel(self.question_data["content"])
        self.question_title.setFont(title_font)
        self.question_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parent_layout.addWidget(self.question_title,
                                     1, 0, 1, 2)

        self.widgets = self.widgets_list()

        self.build_widgets()


    def build_widgets(self) -> None:
        """Builds the widgets tied to the question within the page based on JSON description."""

        y = 0 # x position of widget

        for widget in self.widgets:
            widget_type = widget[0]
            widget_attribute = widget[1]

            # Build buttons
            if widget_type == "button":

                button_text = widget_attribute[5:] # The text of the button is specified after index 5
                button = QPushButton()
                button.setText(button_text)
                button.clicked.connect(lambda checked=False, text=button_text: self.check_answer(text))
                self.parent_layout.addWidget(button, 2, y)
                y += 1

            # Build inputs
            elif widget_type == "input":

                input_length = int(widget_attribute[7:]) # The maximum input length is specified after index 7
                user_input = QLineEdit()
                user_input.setMaxLength(input_length)
                self.parent_layout.addWidget(user_input, 2, y)
                y += 1
                


    def widgets_list(self) -> list:
        """Returns a (type, widgets) list of tuples containing all widgets as described in JSON."""

        widgets = [] # List containing widgets

        for widget_desc in self.question_data["widgets"]:

            # Widget type and attribute are separated by a space
            widget_type, attribute = widget_desc.split(" ", 1)
            widgets.append((widget_type, attribute))

        return widgets

    def check_answer(self, answer:str) -> bool:
        """Checks if the player's answer is correct and make him gain or loose points based on the answer's correctness.
        Returns True if the question was answered correctly, False if not."""


        answer = answer.strip("'")

        correct = self.question.is_answer_correct(answer)
        

        if correct:
            self.player.update_score(self.question.reward)
            self.answered = True
            

        else:
            self.player.update_score(-self.question.reward)
            self.answered = True
                

        # Change the main window's background
        window = self.window()

        window.update_score_label()

        if correct:
            window.setStyleSheet("background-color: green;")

        else:
            window.setStyleSheet("background-color: red;")



        # Restore the window's default background color after 3 seconds
        QTimer.singleShot(3000, window.restore_background)

        print(f"Quizz completed : {window.quizz_ended()}")
        window.next_question()

        return correct
        



class QuizzWindow(QMainWindow):
    def __init__(self, quizz_file:str, player:Player) -> None:
        """A QuizzWindow object represents a game window inside of which random questions from the given JSON quizz file appear.
        - quizz_file: the path to JSON file containing the quizz questions
        - player: an instance of the Player object playing the quizz."""

        super().__init__()


        # Set the grid layout
        parent_layout = QGridLayout()

        # Central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(parent_layout)
        self.setCentralWidget(self.central_widget)

        # The QStackedWidget allows to handle several quizz pages all by displaying only one at a time
        self.question_stack = QStackedWidget()
        

        self.player = player

        
        

        

        # Load the quizz from the file
        self.quizz = JSONQuizzFormat(quizz_file)

        self.setWindowTitle(f"{self.quizz.theme} level {self.quizz.level} - PyGuessR")
        

        # Choose the questions that will be presented to the player
        self.quizz_questions = self.quizz.question_serie(random.randint(2, len(self.quizz.quizz_content["questions"])))
        print("Questions :", self.quizz_questions)

        # Completed questions
        self.completed_questions = []

        self.points_sum = self.quizz.get_points_sum(self.quizz_questions)

        # Score label in the top-right corner        
        self.score_label = QLabel(f"{self.player.score} / {self.points_sum}")
        parent_layout.addWidget(
            self.score_label,
            0, 1,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight
        )

        

        self.current_question_index = 0 # Current question index in the serie
        self.current_question_number = str(self.quizz_questions[0])
        self.current_question = QuestionPage(self.current_question_number, self.quizz.quizz_content["questions"], self.player)
        self.question_stack.addWidget(self.current_question)
        self.question_stack.setCurrentIndex(0)
        parent_layout.addWidget(
            self.question_stack,
            1, 0, 1, 2
        )


    def restore_background(self) -> None:
        """Restores the default background color of the window."""
        self.setStyleSheet("")


    def update_score_label(self) -> None:
        """Updates the score label to display the player's current score."""
        self.score_label.setText(f"{self.player.score} / {self.points_sum}")    


    def next_question(self) -> None:
        """Sets the window's QStackedWidget to the next question.
        If the quizz is completed, ends the game."""


        self.completed_questions.append(int(self.current_question_number))


        if self.quizz_ended():

            self.player.update_xp()
            self.player.update_themes(self.quizz.theme, self.quizz.level)
            save_profile(self.player, self.player.player_profiles)

            QMessageBox.information(self, 
                                    "Quizz completed", 
                                    f"""Congratulations {self.player.pseudo} ! You have successfully completed the {self.quizz.theme} level {self.quizz.level} test with a total point number of  {self.player.score}.""")

            self.hide()

        else:    
            print(f"Completed questions : {len(self.completed_questions)} / {len(self.quizz_questions)}")
            self.current_question_index += 1
            print("Current question index :", self.current_question_index)
            self.current_question_number = str(self.quizz_questions[self.current_question_index])
            self.current_question = QuestionPage(self.current_question_number, self.quizz.quizz_content["questions"], self.player)
            self.question_stack.addWidget(self.current_question)
            self.question_stack.setCurrentIndex(self.current_question_index)


    def quizz_ended(self) -> bool:
        """Returns True if all the questions of the quizz where answered, False if not."""

        return self.completed_questions == self.quizz_questions       