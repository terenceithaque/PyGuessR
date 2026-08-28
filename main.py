# Main application script
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QGridLayout, QLabel, QPushButton, QDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from list_themes import *
from player import *
from quizz_window import *


class SelectPage(QWidget):
    def __init__(self, select_mode:str="theme") -> None:
        """A page integrated to a QStackedWidget allowing the player to choose either a theme or difficulty level based on the selection mode.
        - select_mode: the selection mode that determines which kind of buttons will be presented to the player. The default selection mode is 'theme'.\n
        For example, to allow the player to choose a quizz theme, set the selection mode as 'theme'. If you want to display a difficulty level selection,
        set the selection mode as 'difficulty'."""

        # Initialize the QWidget
        super().__init__()

        self.select_mode = select_mode


class MainAppWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        # Initialize the QMainWindow object
        super().__init__()


        # Set window title
        self.setWindowTitle("PyGuessR")


        # Current quizz window
        self.quizz_window = None


        # Ask for the player's name
        player_name_dialog = NameInput(self)
        if player_name_dialog.exec() == QDialog.DialogCode.Accepted:
            print("Entered player name :", player_name_dialog.name_input.text())

        # Create a Player object with the given player name
        self.player = Player(player_name_dialog.name_input.text())    

        

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

        self.quizz_window = QuizzWindow(self, quizz_path, self.player)
        #self.quizz_window.setParent(self)
        self.quizz_window.show()



application = QApplication([])
window = MainAppWindow()
window.show()
application.exec()


        