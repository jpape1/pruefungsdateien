from PyQt6.QtWidgets import QStatusBar

class CustomStatusBar(QStatusBar):
    def __init__(self):
        """
        Initializes the custom status bar.
        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Sets up the UI for the status bar.
        """
        self.setStyleSheet("""
            QStatusBar {
                background-color: #ffffff;
                border-top: 1px solid #dcdcdc;
                color: #333333;
                font: 10pt "Segoe UI";
            }
        """)
        self.showMessage("Ready", 5000)

    def update_status(self, message: str, timeout: int = 5000):
        """
        Updates the status bar with a new message.
        :param message: The status message.
        :param timeout: Duration in milliseconds to show the message.
        """
        self.showMessage(message, timeout)
