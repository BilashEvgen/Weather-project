import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core

class DiagrammTempLable(widgets.QLabel):
    def __init__(self, parent, temp):
        super().__init__(parent)

        self.setStyleSheet(f"border-radius: 0px; background-color: transparent; font-family: 'Roboto'; font-weight: 400; color: #FFFFFF;")
        self.setFixedSize(27, 14)
        self.setText(temp)