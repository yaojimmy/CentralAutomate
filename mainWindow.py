from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import storedFunctions

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Central Commands")

        vLay = QVBoxLayout()

        funcLabel = QLabel("Functions")
        funcLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vLay.addWidget(funcLabel)

        for name, val in storedFunctions.__dict__.items():
            if callable(val):
                name = name.split("_")
                name = [x.capitalize() for x in name]
                name = ' '.join(name)
                button = QPushButton(name)
                vLay.addWidget(button)
                button.clicked.connect(val)
        
        vLay.addStretch()

        self.setLayout(vLay)
        self.setFixedSize(QSize(400, 300))

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
