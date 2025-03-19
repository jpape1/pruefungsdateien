from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtGui import QFont
from config.config import Config
from datetime import datetime

class SettingsSection(QGroupBox):
    """
    Widget for displaying settings
    This section contains several cards, each with a label and a combobox for selecting settings
    """

    def __init__(self) -> None:
        """
        Initializes the settings section widget
        """
        super().__init__()
        self.setTitle("")
        self.init_ui()

    def init_ui(self) -> None:
        """
        Sets up the user interface for the settings
        """
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        labels = ["Fachrichtung", "Prüfteil", "Dateityp", "Jahr", "Abschlusszeitraum"]
        current_year = datetime.now().year
        years = [str(year) for year in range(current_year - 5, current_year + 1)]

        combos = [
            self.create_combobox(Config.get_specializations(), "Fachrichtung wählen", "specialization_combo"),
            self.create_combobox(Config.get_exam_parts(), "Prüfungsteil wählen", "exam_part_combo"),
            self.create_combobox(Config.get_file_types(), "Dateityp wählen", "file_type_combo"),
            self.create_combobox(years, "Jahr wählen", "year_combo", current_year),
            self.create_combobox(Config.get_periods(), "Abschlusszeitraum wählen", "period_combo")
        ]

        for label_text, combo in zip(labels, combos):
            card_layout = QVBoxLayout()
            lbl = QLabel(label_text)
            lbl.setFont(QFont("Segoe UI", 11))
            card_layout.addWidget(lbl)
            card_layout.addWidget(combo)
            layout.addLayout(card_layout)

        layout.addStretch()
        self.setLayout(layout)

    def create_combobox(self, items, tooltip, object_name, default=None) -> QComboBox:
        """
        Creates a combobox with the given items, tooltip, and object name

        :param items: List of items to be added to the combobox
        :param tooltip: Tooltip text to display
        :param object_name: Object name for the combobox
        :return: Configured QComboBox widget
        """
        combo = QComboBox()
        combo.addItems(items)
        combo.setToolTip(tooltip)
        combo.setObjectName(object_name)
        if default:
            combo.setCurrentText(str(default))

        combo.setFont(QFont("Segoe UI", 12))
        return combo

    def get_setting(self, setting) -> str:
        """
        Retrieves the selected value from the combobox corresponding to the provided setting name

        :param setting: The name of the setting to retrieve
        :return: The currently selected text from the corresponding combobox, or None if not found
        """
        widget = self.findChild(QComboBox, f"{setting}_combo")
        return widget.currentText() if widget else None