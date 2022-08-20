import sys
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QDialog ,QVBoxLayout)

class Form(QDialog):
    def __init__(self, parent = None):
        # super() allows us to access methods of the base class.
        super().__init__()
        # super(Form, self).__init__(parent)
        self.setWindowTitle("Dialog Application!")
        self.initUI()

    def initUI(self):
        self.edit = QLineEdit("What is your name ?")
        self.btn1 = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.btn1)
        self.setLayout(layout)

        self.btn1.clicked.connect(self.greeting) # Not self.greeting()
        
    def greeting(self):
        print(f"Hello {self.edit.text()}!")
        pass
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
    pass