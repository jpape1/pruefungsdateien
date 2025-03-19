# config/config.py

class Config:
    @staticmethod
    def get_specializations() -> list[str]:
        return ["Anwendungsentwicklung", "Systemintegration", "Digitale Vernetzung", "Daten- und Prozessanalyse", "WISO"]

    @staticmethod
    def get_exam_parts() -> list[str]:
        return ["AP1", "AP2"]

    @staticmethod
    def get_periods() -> list[str]:
        return ["Sommer", "Winter"]

    @staticmethod
    def get_file_types() -> list[str]:
        return ["Löser", "Aufgabenblatt", "Belegsatz"]
    
    @staticmethod
    def get_version() -> str:
        return "2.1"
