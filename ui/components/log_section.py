# ui/components/log_section.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class LogSection(QWidget):
    def __init__(self):
        """
        Initializes LogSection widget
        """
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Sets up user interface components of the log section
        """
        log_layout = QVBoxLayout()
        log_layout.setContentsMargins(0, 0, 0, 0)
        log_layout.setSpacing(5)

        # Log Header
        log_header = QLabel("Log-Ausgabe")
        log_header.setFont(QFont("Segoe UI", 14, QFont.Bold))
        log_header.setStyleSheet("color: #2c3e50;")
        log_header.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Log Text Edit
        self.log_textedit = QPlainTextEdit()
        self.log_textedit.setReadOnly(True)
        self.log_textedit.setPlaceholderText("Logs erscheinen hier...")
        self.log_textedit.setStyleSheet("""
            QPlainTextEdit {
                background-color: #ffffff;
                border: 1px solid #2980b9;
                border-radius: 5px;
                padding: 5px;
                font-family: Consolas, "Courier New", monospace;
                font-size: 12px;
            }
        """)

        log_layout.addWidget(log_header)
        log_layout.addWidget(self.log_textedit)

        self.setLayout(log_layout)
        self.setStyleSheet("""
            LogSection {
                background-color: #f9f9f9;
                border: 1px solid #bdc3c7;
                border-radius: 8px;
            }
        """)

    def append_log(self, message: str):
        """
        Appends a log message to the log text edit

        Args:
            message (str): The message to append
        """
        self.log_textedit.appendPlainText(message)
