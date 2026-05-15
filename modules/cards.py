import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import request
from datetime import datetime, timezone, timedelta

class Cards(widgets.QFrame):
    CARDS_SELECTED_COUNTER = 0
    CARDS_LIST = []
    def __init__(self, parent, city_name):
        super().__init__(parent)
        
        request_data = request(city_name)
        
        city_timezone = request_data["timezone"]
        tz = timezone(timedelta(seconds=city_timezone))
        
        current_time = datetime.now(tz)
        time_str = current_time.strftime("%H:%M")
        
        self.SELECTED = False
        
        self.setStyleSheet("border-bottom: 1px solid #859892;")
        self.setFixedSize(330, 82)
        
        card_layout = widgets.QHBoxLayout()
        card_layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(card_layout)

        frame1 = widgets.QFrame(parent = self)
        frame1.setFixedSize(105, 82)
        frame1.setStyleSheet("border: none; background-color: transparent;")
        frame1_layout = widgets.QVBoxLayout()
        frame1.setLayout(frame1_layout)
        
        frame1_label1 = widgets.QLabel(text = request_data["name"], parent = frame1)
        frame1_label2 = widgets.QLabel(text = time_str, parent = frame1)
        frame1_label3 = widgets.QLabel(text = request_data["weather"][0]["main"], parent = frame1)

        frame1_layout.addWidget(frame1_label1)
        frame1_layout.addWidget(frame1_label2)
        frame1_layout.addWidget(frame1_label3)

        frame2 = widgets.QFrame(parent = self)
        frame2.setFixedSize(105, 82)
        frame2.setStyleSheet("border: none; background-color: transparent;")
        
        frame2_layout = widgets.QVBoxLayout()
        frame2_layout.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        frame2_layout.setContentsMargins(0,0,0,0)
        frame2.setLayout(frame2_layout)
        
        frame2_label1 = widgets.QLabel(text = f"{int(request_data['main']['temp']-273)}°", parent = frame2)
        frame2_label2 = widgets.QLabel(text = f"Макс.:{int(request_data['main']['temp_max']-273)}°, Мін.:{int(request_data['main']['temp_min']-273)}°", parent = frame2)
        
        frame2_layout.addWidget(frame2_label1, alignment = core.Qt.AlignmentFlag.AlignRight)
        frame2_layout.addWidget(frame2_label2)
        
        card_layout.addWidget(frame1)
        card_layout.addStretch(1)
        card_layout.addWidget(frame2)
        
        Cards.CARDS_LIST.append(self)
        
    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton and self.SELECTED == False:
            if Cards.CARDS_SELECTED_COUNTER < 1:
                
                self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 17px;")
                self.SELECTED = True
                
                Cards.CARDS_SELECTED_COUNTER += 1
                
            elif Cards.CARDS_SELECTED_COUNTER >= 1:
                
                for card in Cards.CARDS_LIST:
                    
                    if card.SELECTED:
                        card.setStyleSheet("background-color: transparent; border-radius: 17px;")
                        card.SELECTED = False

                Cards.CARDS_SELECTED_COUNTER = 1
                
                self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 17px;")
                self.SELECTED = True