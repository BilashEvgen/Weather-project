import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
import PyQt6.QtWebEngineWidgets as WebEngine
import folium 
import io

from utils import request
from .cards import Cards
from utils import close_drop_menu

class LeftContainer(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.COUNTER = 0
        
        self.setObjectName("Left_container")
        
        self.setFixedSize(370, 800)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        self.leftcontainer_layout = widgets.QVBoxLayout()
        
        self.setLayout(self.leftcontainer_layout)
        self.leftcontainer_layout.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        self.leftcontainer_layout.setContentsMargins(0,0,0,0)
        self.leftcontainer_layout.setSpacing(0)
        
        self.leftcontainer_header = widgets.QFrame(self)
        self.leftcontainer_header.setFixedSize(370, 44)
        self.leftcontainer_layout.addWidget(self.leftcontainer_header)
        
        self.header_layout = widgets.QHBoxLayout()
        self.header_layout.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        self.leftcontainer_header.setLayout(self.header_layout)
        
            
            
        self.CHANGE_THEME_BUTTON = widgets.QPushButton(parent = self.leftcontainer_header)
        
        self.CHANGE_THEME_BUTTON.setFixedSize(54,24)
        self.CHANGE_THEME_BUTTON.setIconSize(self.CHANGE_THEME_BUTTON.size())
        
        self.CHANGE_THEME_BUTTON.setStyleSheet("border : none;background-color: transparent;")
        
        self.change_theme_icon = gui.QIcon("media/title_bar/light_theme.svg")
        self.CHANGE_THEME_BUTTON.setIcon(self.change_theme_icon)
        
        self.CHANGE_THEME_BUTTON.clicked.connect(self.change_button)
        
        self.header_layout.addWidget(self.CHANGE_THEME_BUTTON)
        
        
        self.frame = widgets.QFrame(parent = self)
        self.frame.setFixedSize(370, 756)

        self.leftcontainer_layout.addWidget(self.frame)

        self.scroll_area = widgets.QScrollArea(parent = self.frame)
        self.scroll_area.setFixedSize(370, 730)
        self.scroll_area.setStyleSheet("background-color: transparent;")
        
        
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.scroll_frame = widgets.QFrame(parent = self.scroll_area)
        self.scroll_area.setWidget(self.scroll_frame)
        self.scroll_frame_layout = widgets.QVBoxLayout()
        self.scroll_frame_layout.setAlignment(core.Qt.AlignmentFlag.AlignTop)
        
        self.scroll_frame.setLayout(self.scroll_frame_layout)
        self.leftcontainer_layout.addWidget(self.frame)

    def change_button(self):
        our_content_container = self.window().findChild(widgets.QFrame, "Content_container")
        search_field = self.window().findChild(widgets.QFrame, "SEARCH_FIELD")
        
        if self.COUNTER % 2 == 0:
            icon = gui.QIcon("media/title_bar/dark_theme.svg")
            self.CHANGE_THEME_BUTTON.setIcon(icon)
            our_content_container.setStyleSheet("""
            #Content_container {
                background: qlineargradient(
                    x1:0 y1:1,
                    x2:1 y2:0,
                    stop:0 #5DADE2 stop:1 #808080
                    );
            }
        """)
            if search_field and hasattr(search_field, "DROP_DOWN_FRAME") and search_field.DROP_DOWN_FRAME:
                search_field.DROP_DOWN_FRAME.setStyleSheet("background-color: #6a6a6a")
        else:
            icon = gui.QIcon("media/title_bar/light_theme.svg")
            our_content_container.setStyleSheet("""
            #Content_container {
                background: qlineargradient(
                    x1:0 y1:1,
                    x2:1 y2:0,
                    stop:0 #87CEFA stop:1 #FFDF56
                    );
            }
        """)
            if search_field and hasattr(search_field, "DROP_DOWN_FRAME") and search_field.DROP_DOWN_FRAME:
                search_field.DROP_DOWN_FRAME.setStyleSheet("background-color: #9d8b38")
            self.CHANGE_THEME_BUTTON.setIcon(icon)
        self.COUNTER += 1
        close_drop_menu(self.window())

        
        

