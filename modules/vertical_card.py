import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core

class Vertical_Card(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: transparent;")
        self.setObjectName("Vertical_card")
        self.setFixedSize(45,82)
        self.VCARD_LAYOUT = widgets.QVBoxLayout()
        self.setLayout(self.VCARD_LAYOUT)
        self.VCARD_LAYOUT.setSpacing(10)
        self.VCARD_LAYOUT.setContentsMargins(0,0,0,0)
        self.VCARD_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.TIME_LABEL = widgets.QLabel()
        self.TIME_LABEL.setFixedSize(45,19)
        self.TIME_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TIME_LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px;background-color: transparent; font-family: 'Roboto'; font-weight: 500;")
        
        self.WEATHER_LABEL = widgets.QLabel()
        self.WEATHER_LABEL.setFixedSize(24,24)
        self.WEATHER_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.TEMPERATURE_LABEL = widgets.QLabel()
        self.TEMPERATURE_LABEL.setFixedSize(25,19)
        self.TEMPERATURE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TEMPERATURE_LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px;background-color: transparent; font-family: 'Roboto'; font-weight: 500;")
        
        self.VCARD_LAYOUT.addWidget(self.TIME_LABEL,alignment= core.Qt.AlignmentFlag.AlignCenter )
        self.VCARD_LAYOUT.addWidget(self.WEATHER_LABEL,alignment= core.Qt.AlignmentFlag.AlignCenter)
        self.VCARD_LAYOUT.addWidget(self.TEMPERATURE_LABEL,alignment= core.Qt.AlignmentFlag.AlignCenter)
    
    
    
    
    
    
    
    
    
    
    
    
    # pixmap = gui.QPixmap(f"media/title_bar/weather_icons/{self.REQUEST_DATA['weather'][0]['icon']}.svg")