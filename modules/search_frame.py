import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import json
import os
from .search_field import SearchField
from utils import scale
class SearchFrame(widgets.QFrame):
    DROP_DOWN_MENU = None
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName("SEARCH_FRAME")
        self.setFixedSize(scale.scale_x(261),scale.scale_y(36))
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px;")
        
        self.SEARCH_FRAME_LAYOUT = widgets.QHBoxLayout(self)
        self.setLayout(self.SEARCH_FRAME_LAYOUT)
        self.SEARCH_FRAME_LAYOUT.setContentsMargins(8,7,8,7)
        self.SEARCH_FRAME_LAYOUT.setSpacing(0)
        
        
        
        self.SEARCH_LABEL = widgets.QLabel(self)
        self.SEARCH_LABEL.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.SEARCH_LABEL.setFixedSize(scale.scale_x(25),scale.scale_y(22))
        
        search_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/searcher.png")
        if not search_pixmap.isNull():
            scaled_pixmap = search_pixmap.scaled(scale.scale_x(18),scale.scale_y(19), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            self.SEARCH_LABEL.setPixmap(scaled_pixmap)
            
        self.search_field = SearchField(self)
        
        self.CLEAR_BUTTON_FRAME = widgets.QFrame(parent = self)
        self.CLEAR_BUTTON_FRAME.setFixedSize(scale.scale_x(20),scale.scale_y(20))
        self.CLEAR_BUTTON_FRAME.setStyleSheet("background-color: transparent; border: none;")
        
        self.clear_button = widgets.QPushButton(parent=self.CLEAR_BUTTON_FRAME)
        self.clear_button.hide()
        
    
        self.clear_button.setFixedSize(scale.scale_x(20),scale.scale_y(20))
        self.clear_button.setStyleSheet("background-color: transparent; border: none; color: white;")
        self.clear_button.setIcon(gui.QIcon("media/title_bar/additional_elements/clear_button.png"))
        self.clear_button.clicked.connect(self.hide_clear_button)
        
        
    
        self.SEARCH_FRAME_LAYOUT.addWidget(self.SEARCH_LABEL, alignment = core.Qt.AlignmentFlag.AlignLeft and core.Qt.AlignmentFlag.AlignCenter)
        self.SEARCH_FRAME_LAYOUT.addWidget(self.search_field, alignment = core.Qt.AlignmentFlag.AlignRight)
        self.SEARCH_FRAME_LAYOUT.addWidget(self.CLEAR_BUTTON_FRAME, alignment = core.Qt.AlignmentFlag.AlignRight)
        
    def hide_clear_button(self):
        self.clear_button.hide()
        self.search_field.clear()
        self.search_field.DROP_DOWN_FRAME.hide()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        