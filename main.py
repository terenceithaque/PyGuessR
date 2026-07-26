# Main application script
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from list_themes import *


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



application = QApplication([])
window = MainAppWindow()
window.show()
application.exec()


        