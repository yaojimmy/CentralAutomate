from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class ParamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.paramLabel = QLabel("Parameters")
        self.layout.addWidget(self.paramLabel)
        self.setLayout(self.layout)
    
    def addParam(self, paramName, choices):
        label = QLabel(paramName + ": ")
        combo = QComboBox()
        for choice in choices:
            combo.addItem(choice)

        thisLayout = QHBoxLayout()
        thisLayout.addWidget(label)
        thisLayout.addWidget(combo)

        self.layout.addLayout(thisLayout)