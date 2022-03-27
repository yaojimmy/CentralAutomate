from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
import sys
import storedFunctions

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Central Commands")

        vLay = QVBoxLayout()

        funcLabel = QLabel("Functions")
        vLay.addWidget(funcLabel)

        for name, val in storedFunctions.__dict__.items():
            if callable(val):
                button = QPushButton(name)
                vLay.addWidget(button)
                button.clicked.connect(val)
        
        vLay.addStretch()

        button1 = QPushButton("Make Breakfast")
        button2 = QPushButton("Web Scrape Website")
        button3 = QPushButton("Write Thank You Email")

        button1.clicked.connect(self.breakfast_clicked)

        self.setLayout(vLay)

        self.setFixedSize(QSize(400, 300))

    def breakfast_clicked(self):
        print("Breakfast was made!")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
