import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import DriverScrubWindow
from gui.dark_theme import DARK_STYLE

def run_app():
    app = QApplication(sys.argv)

    # Apply custom dark theme
    app.setStyleSheet(DARK_STYLE)

    window = DriverScrubWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()
