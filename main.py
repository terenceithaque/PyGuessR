# Main application script
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout
from list_themes import *


class MainAppWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        # Initialize the QMainWindow object
        super().__init__()

        # Set window title
        self.setWindowTitle("PyGuessR")

        # Layout for the widgets
        display_layout = QGridLayout()

        available_themes = get_themes()
        print(available_themes)



application = QApplication([])
window = MainAppWindow()
window.show()
application.exec()


        