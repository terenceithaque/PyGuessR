# Main application script
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from list_themes import *
from quizz_window import *


class MainAppWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        # Initialize the QMainWindow object
        super().__init__()

        # Set window title
        self.setWindowTitle("PyGuessR")

        

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout for the widgets
        parent_layout = QGridLayout(central_widget)

        available_themes = get_themes()
        print(available_themes)

        # Dictionnary associating themes with their absolute file paths
        theme_paths = {}
        
        for theme in available_themes:
            theme_paths[theme] = get_theme_abspath(theme)
        
        print(theme_paths)
        


        theme_label = QLabel("Which theme do you want to explore today ?")
        theme_label_font = QFont()
        theme_label_font.setBold(True)
        theme_label.setFont(theme_label_font)
        theme_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        parent_layout.addWidget(theme_label, 0, 0)


        # Create buttons to choose a theme

        x = 0 # x is the row of the button
        y = 1 # y is the column

        for theme in theme_paths.keys():
            theme_button = QPushButton(text=theme, parent=central_widget)
            theme_button.clicked.connect(
                lambda checked=False, theme=theme: self.start_quizz(theme)
            )

            theme_button.setFixedWidth(80)
            theme_button.setFixedHeight(30)
            parent_layout.addWidget(theme_button, y, x)
            x += 1
            if x == 3:
                x = 0
                y += 1


    def start_quizz(self, theme:str) -> None:
        """Hides the home window and start """
        quizz_path = get_quizz_abspath(theme, level=1)
        print("Absolute file path to quizz level 1:", quizz_path)

        self.hide() # Hide the home window

        quizz_window = QuizzWindow(quizz_path)
        quizz_window.show()



application = QApplication([])
window = MainAppWindow()
window.show()
application.exec()


        