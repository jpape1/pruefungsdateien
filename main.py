# main.py

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main() -> int:
    """
    Initialize and run the main application.

    This function creates the QApplication instance, sets the application style,
    instantiates the main window, and starts the event loop.

    Returns:
        int: The exit status of the application
    """
    # Create the QApplication instance with command line arguments
    app = QApplication(sys.argv)
    # Set the application style to "Fusion"
    app.setStyle("Fusion")
    # Instantiate the main window from the app module
    window = MainWindow()
    # Show the main window
    window.show()
    # Execute the application's main loop and return its exit status
    return app.exec()

if __name__ == "__main__":
    # Run the main function and exit with its return code
    sys.exit(main())