# utils/status_bar.py

from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtCore import Qt


class CustomStatusBar(QStatusBar):
    def __init__(self):
        """
        Initializes CustomStatusBar widget
        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Sets up user interface components of the status bar
        """
        self.setStyleSheet("""
            QStatusBar {
                background: transparent;
                color: black;
                font: 10pt "Segoe UI";
            }
        """)
        self.showMessage("Bereit", 5000)

    def update_status(self, message: str, timeout: int = 5000):
        """
        Updates status bar with a new message

        Args:
            message (str): The message to display on the status bar
            timeout (int, optional): Duration in milliseconds to display the message. Defaults to 5000
        """
        self.showMessage(message, timeout)

    def clear_status(self):
        """
        Clears the current message from the status bar
        """
        self.clearMessage()
