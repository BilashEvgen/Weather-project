import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core

class Sun_Move_Card(widgets.QFrame):
    def __init__(self, parent,text):
        super().__init__(parent)
        self.setObjectName("SunMove")

        self.setFixedSize(90, 82)           

        self.SMCARD_LAYOUT = widgets.QVBoxLayout()
        self.SMCARD_LAYOUT.setSpacing(10)
        self.SMCARD_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.SMCARD_LAYOUT)
        
        self.TIME_LABEL = widgets.QLabel()
        self.TIME_LABEL.setFixedSize(41, 19)
        self.TIME_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)

        self.ICON_LABEL = widgets.QLabel()
        self.ICON_LABEL.setFixedSize(24,24)
        self.ICON_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
                    
        self.TEXT_LABEL = widgets.QLabel(text = text)
        self.TEXT_LABEL.setFixedSize(90,19)
        self.TEXT_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
                    
        self.SMCARD_LAYOUT.addWidget(self.TIME_LABEL)
        self.SMCARD_LAYOUT.addWidget(self.ICON_LABEL)   
        self.SMCARD_LAYOUT.addWidget(self.TEXT_LABEL)
                           
        
        