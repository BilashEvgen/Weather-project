import PyQt6.QtWidgets as widgets
import PyQt6.QtCore as core

class Sun_Move_Card(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet("background-color: transparent;")
        self.setFixedSize(90, 82)           

        self.SMCARD_LAYOUT = widgets.QVBoxLayout()
        self.SMCARD_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.SMCARD_LAYOUT)
        self.SMCARD_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.SMCARD_LAYOUT.setSpacing(10)
        
        self.TIME_LABEL = widgets.QLabel()
        self.TIME_LABEL.setFixedSize(90, 19)
        self.TIME_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TIME_LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px; font-family: 'Roboto'; font-weight: 500;")

        self.ICON_LABEL = widgets.QLabel()
        self.ICON_LABEL.setFixedSize(90,24)
        self.ICON_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
                    
        self.TEXT_LABEL = widgets.QLabel()
        self.TEXT_LABEL.setFixedSize(90,19)
        self.TEXT_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        self.TEXT_LABEL.setStyleSheet("color: white; font-size: 16px; border-radius: 0px; font-family: 'Roboto'; font-weight: 500;")
                    
        self.SMCARD_LAYOUT.addWidget(self.TIME_LABEL, core.Qt.AlignmentFlag.AlignCenter)
        self.SMCARD_LAYOUT.addWidget(self.ICON_LABEL, core.Qt.AlignmentFlag.AlignCenter)   
        self.SMCARD_LAYOUT.addWidget(self.TEXT_LABEL, core.Qt.AlignmentFlag.AlignCenter)

        
        