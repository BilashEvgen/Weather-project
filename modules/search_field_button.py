
import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
from utils import scale
class SearchFieldCityButton(widgets.QPushButton):
    def __init__(self, parent, text, width, height) :
        self.TEXT = text
        super().__init__(parent)
        
        self.setText(text)
        self.setStyleSheet("background-color: transparent; border: none; color: white; font-family: 'Roboto'; font-weight: 400; text-align: left;")
        scale.setFontSize(self,17)
        self.setFixedSize(scale.scale_x(width), scale.scale_y(height))   
            
