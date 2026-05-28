import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

from utils import json_write, request
from datetime import datetime, timezone, timedelta
from modules import Vertical_Card
from modules import Sun_Move_Card

class Cards(widgets.QFrame):
   
    CARDS_LIST = []
    def __init__(self, parent, city_name):
        self.CITY_NAME = city_name
        super().__init__(parent)
        
        self.REQUEST_DATA = request(self.CITY_NAME, "current")
        
        self.data_time()
        self.SELECTED = False
        
        self.setStyleSheet("border-bottom: 1px solid #859892;")
        self.setFixedSize(330, 98)
        
        self.CARD_LAYOUT = widgets.QHBoxLayout()
        self.CARD_LAYOUT.setContentsMargins(0,0,0,0)
        
        self.setLayout(self.CARD_LAYOUT)

        self.FRAME1 = widgets.QFrame(parent = self)
        self.FRAME1.setFixedSize(200, 82)
        self.FRAME1.setStyleSheet("border: none; background-color: transparent;")
        self.FRAME1_LAYOUT = widgets.QVBoxLayout()
        self.FRAME1.setLayout(self.FRAME1_LAYOUT)
        
        self.FRAME1_LABEL1 = widgets.QLabel(text = self.REQUEST_DATA["name"], parent = self.FRAME1)
        self.FRAME1_LABEL1.setFixedSize(200,28)
        self.FRAME1_LABEL1.setStyleSheet("font-size: 24px; font-family: 'Roboto';font-weight: 500;")
        
        self.FRAME1_LABEL2 = widgets.QLabel(text = self.TIME_STR, parent = self.FRAME1)
        self.FRAME1_LABEL2.setStyleSheet("font-size: 12px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME1_LABEL2.setFixedSize(105,14)
        
        self.FRAME1_LABEL3 = widgets.QLabel(text = self.REQUEST_DATA["weather"][0]["description"].capitalize(), parent = self.FRAME1)
        self.FRAME1_LABEL3.setStyleSheet("font-size: 12px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME1_LABEL3.setFixedSize(105,14)
        
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL1)
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL2)
        self.FRAME1_LAYOUT.addWidget(self.FRAME1_LABEL3)

        self.FRAME2 = widgets.QFrame(parent = self)
        self.FRAME2.setFixedSize(110, 82)
        self.FRAME2.setStyleSheet("border: none; background-color: transparent;")
        
        self.FRAME2_LAYOUT = widgets.QVBoxLayout()
        self.FRAME2_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.FRAME2_LAYOUT.setContentsMargins(0,0,0,0)
        self.FRAME2.setLayout(self.FRAME2_LAYOUT)
        
        self.FRAME2_LABEL1 = widgets.QLabel(text = f"{int(self.REQUEST_DATA['main']['temp']-273)}°", parent = self.FRAME2)
        self.FRAME2_LABEL1.setStyleSheet("font-size: 44px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME2_LABEL1.setFixedSize(67,52 )
        
        
        self.FRAME2_LABEL2 = widgets.QLabel(text = f"Макс.:{int(self.REQUEST_DATA['main']['temp_max']-273)}°, Мін.:{int(self.REQUEST_DATA['main']['temp_min']-273)}°", parent = self.FRAME2)
        self.FRAME2_LABEL2.setStyleSheet("font-size: 12px; font-family: 'Roboto'; font-weight: 500; color: rgba(255, 255, 255, 0.8);")
        self.FRAME2_LABEL2.setFixedSize(110,14)
        self.FRAME2_LABEL2.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.FRAME2_LAYOUT.addWidget(self.FRAME2_LABEL1, alignment = core.Qt.AlignmentFlag.AlignRight)
        self.FRAME2_LAYOUT.addWidget(self.FRAME2_LABEL2)
        
        self.CARD_LAYOUT.addWidget(self.FRAME1)
        self.CARD_LAYOUT.addStretch(1)
        self.CARD_LAYOUT.addWidget(self.FRAME2)
        
        Cards.CARDS_LIST.append(self)

    def data_time(self):
        city_timezone = self.REQUEST_DATA["timezone"]

        tz = timezone(timedelta(seconds=city_timezone))
        
        current_time = datetime.now(tz)
        self.TIME_STR = current_time.strftime("%H:%M")

        self.DAY_STR = current_time.strftime("%A")
        self.DATE = current_time.strftime("%d.%m.%Y")

        sunrise = self.REQUEST_DATA["sys"]["sunrise"]
        self.SUNRISE_TIME = datetime.fromtimestamp(sunrise,timezone.utc).hour
        
        sunset = self.REQUEST_DATA["sys"]["sunset"] 
        self.SUNSET_TIME = datetime.fromtimestamp(sunset,timezone.utc).hour
        

    def mousePressEvent(self, event: gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton and self.SELECTED == False:
            self.REQUEST_DATA = request(self.CITY_NAME, "current")
            self.DAY_REQUEST_DATA = request(self.CITY_NAME, "daily")
            
            
            weather_container = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER")
            real_time = datetime.fromtimestamp(self.DAY_REQUEST_DATA["list"][0]["dt"], timezone.utc).hour + self.DAY_REQUEST_DATA["city"]["timezone"] // 3600
            
            vertical_card = self.window().findChild(widgets.QFrame,"vertical_card")
            
            
            for index in range(len(self.DAY_REQUEST_DATA["list"])):
                hour_data = self.DAY_REQUEST_DATA["list"][index]
                self.HOUR_TIME = datetime.fromtimestamp(hour_data["dt"], timezone.utc).hour + self.DAY_REQUEST_DATA["city"]["timezone"] // 3600
                
                vertical_card = Vertical_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME)
                
                vertical_card.TIME_LABEL.setText(f"{self.HOUR_TIME}")
                
                pixmap = gui.QPixmap(f"media/title_bar/weather_icons/{self.DAY_REQUEST_DATA['weather'][hour_data]['icon']}.png")
                
                if not pixmap.isNull():
                    scaled = pixmap.scaled(vertical_card.WEATHER_LABEL.size(), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                    vertical_card.WEATHER_LABEL.setPixmap(scaled)
                
                vertical_card.TEMP_LABEL.setText(f"{int(hour_data['main']['temp']-273)}°")
                
                if index + 1 < len(self.DAY_REQUEST_DATA["list"]):
                    next_hour = datetime.fromtimestamp(self.DAY_REQUEST_DATA["list"][index + 1]["dt"], timezone.utc).hour
                else:
                    next_hour = None

                if next_hour is not None and self.SUNRISE_TIME > datetime.fromtimestamp(hour_data["dt"], timezone.utc).hour and self.SUNRISE_TIME < next_hour:
                    sunrise_card = Sun_Move_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME, text = "Схід сонця")

                    
                if next_hour is not None and self.SUNSET_TIME > datetime.fromtimestamp(hour_data["dt"], timezone.utc).hour and self.SUNRISE_TIME < next_hour:
                    sunset_card = Sun_Move_Card(parent = weather_container.DAY_WEATHER_SCROLL_FRAME, text = "Захід сонця")
                
                
                
            
            json_write("current.json", self.REQUEST_DATA)
            json_write("daily.json", self.DAY_REQUEST_DATA)
            self.data_time()

            
            
            # city
            weather_container.LEFT_CITY_LABEL.setText(self.REQUEST_DATA["name"])
            # temperature
            weather_container.LEFT_WEATHER_LABEL.setText(f"{int(self.REQUEST_DATA['main']['temp']-273)}°")
            
            # description
            weather_container.LEFT_DESCRIPTION_LABEL1.setText(self.REQUEST_DATA["weather"][0]["description"].capitalize())
            # max min temp
            weather_container.LEFT_DESCRIPTION_LABEL2.setText(f"Макс.:{int(self.REQUEST_DATA['main']['temp_max']-273)}°, Мін.:{int(self.REQUEST_DATA['main']['temp_min']-273)}°")
            
            
            
            pixmap = gui.QPixmap(f"media/title_bar/weather_icons/{self.REQUEST_DATA['weather'][0]['icon']}.png")

            if not pixmap.isNull():
                scaled = pixmap.scaled(weather_container.LEFT_WEATHER_ICON_SIZE, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                weather_container.LEFT_WEATHER_ICON.setPixmap(scaled)

            weather_container.RIGHT_DATA_LABEL1.setText(self.DAY_STR.capitalize())
            
            weather_container.RIGHT_DATA_LABEL2.setText(self.DATE)
            
            weather_container.RIGHT_CLOCK_LABEL.setText(self.TIME_STR)
            
            weather_container.RIGHT_CLOCK_FRAME.setPixmap(gui.QPixmap(f"media/title_bar/clock.svg"))
            
            
            
            self.FRAME1_LABEL2.setText(self.TIME_STR)
            self.FRAME1_LABEL3.setText(self.REQUEST_DATA["weather"][0]["description"].capitalize())
            self.FRAME2_LABEL1.setText(f"{int(self.REQUEST_DATA['main']['temp']-273)}°")
            self.FRAME2_LABEL2.setText(f"Макс.:{int(self.REQUEST_DATA['main']['temp_max']-273)}°, Мін.:{int(self.REQUEST_DATA['main']['temp_min']-273)}°")
            
            for card in Cards.CARDS_LIST:
                if card.SELECTED:
                    card.setStyleSheet("background-color: transparent; border-radius: 8px;")
                    card.SELECTED = False

            self.setStyleSheet("background-color: rgba(0, 0, 0, 0.3); border-radius: 8px;")
            self.SELECTED = True
            
            
            
            
            # fruits = ['apple', 'banana', 'cherry']
            # for index, fruit in enumerate(fruits):
            #     print(f"Индекс: {index}, Фрукт: {fruit}")
