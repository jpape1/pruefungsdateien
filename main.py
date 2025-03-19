# main.py

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main() -> int:
    """
    Initialize and run the main application

    Returns:
        int: The exit status of the application
    """
    app = QApplication(sys.argv)

    with open("resources/styles.qss", "r") as f:
        qss = f.read()
    app.setStyleSheet(qss)

    window = MainWindow()
    window.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())