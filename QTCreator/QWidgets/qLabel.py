import sys
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # label = QLabel("Hello World")
    label = QLabel("<font color=red size=40>Hello World!</font>")
    label.resize(400,400)
    # label.size(400, 400)
    label.show()
    app.exec_()