# config/config.py

class Config:
    @staticmethod
    def get_specializations():
        return ["Anwendungsentwicklung", "Systemintegration", "Digitale Vernetzung", "Daten- und Prozessanalyse", "WISO"]

    @staticmethod
    def get_exam_parts():
        return ["AP1", "AP2"]

    @staticmethod
    def get_periods():
        return ["Sommer", "Winter"]

    @staticmethod
    def get_file_types():
        return ["Löser", "Aufgabenblatt", "Belegsatz"]
