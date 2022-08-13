from PyQt5.QtWidgets import QApplication, QPushButton, QTextEdit, QWidget, QVBoxLayout
import os, sys

class qEditTextExample(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("This is my first program - qEditText")
        self.resize(500, 400)

        self.textEdit   = QTextEdit()
        self.btnPress1  = QPushButton("Button 1")
        self.btnPress2  = QPushButton("Button 2")
        self.btnClear1  = QPushButton("Clear")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        layout.addWidget(self.btnClear1)
        self.setLayout(layout)
        
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)
        self.btnClear1.clicked.connect(self.btnClear1_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("You pressed button 1")
    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("You pressed button 2")
    def btnClear1_Clicked(self):
        self.textEdit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = qEditTextExample()
    window.show()
    sys.exit(app.exec_())