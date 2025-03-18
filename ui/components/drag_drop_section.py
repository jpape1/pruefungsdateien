from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QProgressBar, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class DragDropSection(QWidget):
    def __init__(self, upload_callback):
        """
        Initializes the drag and drop section widget.
        :param upload_callback: Callback function to trigger file upload.
        """
        super().__init__()
        self.upload_callback = upload_callback
        self.init_ui()
        self.setAcceptDrops(True)

    def init_ui(self):
        """
        Sets up the user interface components.
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        # Create the drop area styled as a card
        self.drop_frame = QFrame()
        self.drop_frame.setObjectName("DropFrame")
        self.drop_frame.setFixedHeight(250)
        drop_layout = QVBoxLayout()
        self.drop_label = QLabel("Datei ablegen oder unten klicken")
        self.drop_label.setFont(QFont("Segoe UI", 16))
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        drop_layout.addStretch()
        drop_layout.addWidget(self.drop_label)
        drop_layout.addStretch()
        self.drop_frame.setLayout(drop_layout)

        # Create the upload button
        self.upload_button = QPushButton("Datei wählen")
        self.upload_button.setFixedSize(220, 50)
        self.upload_button.setFont(QFont("Segoe UI", 14))
        self.upload_button.clicked.connect(self.upload_callback)

        # Create the progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(25)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)

        layout.addWidget(self.drop_frame)
        layout.addWidget(self.upload_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)

        self.setStyleSheet("""
            #DropFrame {
                border: 2px dashed #16a085;
                border-radius: 15px;
                background-color: #ffffff;
                color: #333333;
            }
            QPushButton {
                background-color: #16a085;
                color: #ffffff;
                border: none;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #1abc9c;
            }
            QLabel {
                color: #333333;
            }
            QProgressBar {
                border: 1px solid #16a085;
                border-radius: 12px;
                text-align: center;
                background-color: #e0e0e0;
            }
            QProgressBar::chunk {
                background-color: #1abc9c;
                border-radius: 12px;
            }
        """)

    def update_progress(self, value):
        """
        Updates the progress bar with the given value.
        :param value: Integer progress percentage.
        """
        self.progress_bar.setValue(value)
        if value >= 100:
            self.progress_bar.setVisible(False)

    def show_progress(self):
        """
        Displays the progress bar and resets its value.
        """
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

    # Drag & Drop Event Handlers
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() and len(event.mimeData().urls()) == 1:
            event.acceptProposedAction()
            self.drop_frame.setStyleSheet("""
                #DropFrame {
                    border: 2px dashed #1abc9c;
                    background-color: #f7f7f7;
                    color: #333333;
                }
            """)
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.drop_frame.setStyleSheet("""
            #DropFrame {
                border: 2px dashed #16a085;
                background-color: #ffffff;
                color: #333333;
            }
        """)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) != 1:
                QMessageBox.warning(self, "Warnung", "Bitte legen Sie maximal eine Datei gleichzeitig ab", QMessageBox.StandardButton.Ok)
                event.ignore()
                return
            file_path = urls[0].toLocalFile()
            if file_path:
                self.show_progress()
                self.upload_callback(file_path)
            self.drop_frame.setStyleSheet("""
                #DropFrame {
                    border: 2px dashed #16a085;
                    background-color: #ffffff;
                    color: #333333;
                }
            """)
