# main.py

import sys
import os
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def resource_path(relative_path: str) -> str:
    """
    Returns the absolute path to the resource. Works for development
    (running .py files) and for PyInstaller-compiled EXEs.
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main() -> int:
    """
    Initialize and run the main application

    Returns:
        int: The exit status of the application
    """
    app = QApplication(sys.argv)

    style_file = resource_path("resources/styles.qss")
    with open(style_file, "r") as f:
        qss = f.read()
    app.setStyleSheet(qss)

    window = MainWindow()
    window.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())