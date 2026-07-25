# Main application script
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout


class MainAppWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        # Initialize the QMainWindow object
        super().__init__()

        # Set window title
        self.setWindowTitle("PyGuessR")

        # Layout for the widgets
        display_layout = QGridLayout()



application = QApplication([])
window = MainAppWindow()
window.show()
application.exec()


        