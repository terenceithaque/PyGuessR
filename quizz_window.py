"""quizz_window.py offers a QuizzWindow class which represents a full quizz window"""
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QGridLayout


class QuizzWindow(QMainWindow):
    def __init__(self):

        # The QStackedWidget allows to handle several quizz pages all by displaying only one at a time
        self.cetral_widget = QStackedWidget()