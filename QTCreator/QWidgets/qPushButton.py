import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# The @Slot() is a decorator that identifies a function as a slot. 
# It is not important to understand why for now, 
# but use it always to avoid unexpected behavior.
@Slot()
def sayHello():
    print("Hello - You clicked the button.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hello_btn = QPushButton("Hello button")
    hello_btn.clicked.connect(sayHello)
    hello_btn.show()
    app.exec_()