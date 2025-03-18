from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtGui import QFont
from config.config import Config
from datetime import datetime

class SettingsSection(QGroupBox):
    """
    Widget for displaying settings
    This section contains several cards, each with a label and a combobox for selecting settings.
    """

    def __init__(self):
        """
        Initializes the settings section widget.
        """
        super().__init__()
        self.setTitle("")
        self.init_ui()

    def init_ui(self):
        """
        Sets up the user interface for the settings.
        """
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Create filter cards (each contains a label and a combobox)
        labels = ["Fachrichtung", "Prüfteil", "Dateityp", "Jahr", "Abschlusszeitraum"]
        current_year = datetime.now().year
        years = [str(year) for year in range(current_year - 5, current_year + 6)]

        combos = [
            self.create_combobox(Config.get_specializations(), "Fachrichtung wählen", "specialization_combo"),
            self.create_combobox(Config.get_exam_parts(), "Prüfungsteil wählen", "exam_part_combo"),
            self.create_combobox(Config.get_file_types(), "Dateityp wählen", "file_type_combo"),
            self.create_combobox(years, "Jahr wählen", "year_combo", current_year),
            self.create_combobox(Config.get_periods(), "Abschlusszeitraum wählen", "period_combo")
        ]

        # For each setting card, create a vertical layout
        for label_text, combo in zip(labels, combos):
            card_layout = QVBoxLayout()
            lbl = QLabel(label_text)
            lbl.setFont(QFont("Segoe UI", 11))
            card_layout.addWidget(lbl)
            card_layout.addWidget(combo)
            layout.addLayout(card_layout)

        layout.addStretch()
        self.setLayout(layout)
        self.setStyleSheet("""
            QGroupBox {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
                border-radius: 15px;
            }
        """)

    def create_combobox(self, items, tooltip, object_name, default=None):
        """
        Creates a combobox with the given items, tooltip, and object name.

        :param items: List of items to be added to the combobox.
        :param tooltip: Tooltip text to display.
        :param object_name: Object name for the combobox (used for styling and retrieval).
        :return: Configured QComboBox widget.
        """
        combo = QComboBox()
        combo.addItems(items)
        combo.setToolTip(tooltip)
        combo.setObjectName(object_name)
        if default:
            combo.setCurrentText(str(default))
        combo.setFont(QFont("Segoe UI", 12))
        combo.setStyleSheet("""
            QComboBox {
                padding: 5px 10px;
                border: 1px solid #dcdcdc;
                border-radius: 8px;
                background-color: white;
                color: black;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: none;
                background-color: white;
            }

            /* The pop-up list (QAbstractItemView) */
            QComboBox QAbstractItemView {
                background-color: white;               /* list background */
                selection-background-color: #333333;     /* highlight color */
                selection-color: #333333;                /* highlight text color */
                border-radius: 15px;
            }
        """)
        return combo

    def get_setting(self, setting):
        """
        Retrieves the selected value from the combobox corresponding to the provided setting name.

        :param setting: The name of the setting to retrieve ('specialization', 'exam_part', 'file_type', 'year', or 'period').
        :return: The currently selected text from the corresponding combobox, or None if not found.
        """
        if setting == "specialization":
            return self.findChild(QComboBox, "specialization_combo").currentText()
        elif setting == "exam_part":
            return self.findChild(QComboBox, "exam_part_combo").currentText()
        elif setting == "file_type":
            return self.findChild(QComboBox, "file_type_combo").currentText()
        elif setting == "year":
            return self.findChild(QComboBox, "year_combo").currentText()
        elif setting == "period":
            return self.findChild(QComboBox, "period_combo").currentText()
        else:
            return None