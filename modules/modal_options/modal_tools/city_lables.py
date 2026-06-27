import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from PyQt6.sip import isdeleted
from utils.clear_layout  import clear_layout
from modules.cards import Cards
from utils.clear_weather_frame import clear_weather_frame
from utils import scale
class CityListLable(widgets.QFrame):
    CITY_LIST = []
    def __init__(self, parent, card, city_name):
        super().__init__(parent)
        CityListLable.CITY_LIST.append(self)
        self.CITY_LIST_LAYOUT = self.window().findChild(widgets.QFrame,"SEARCHCITY")

        self.setObjectName("CityListLable")
        
        self.card = card
        self.CITY_NAME = city_name
        
        self.setFixedSize(scale.scale_x(512), scale.scale_y(32))
        self.setStyleSheet("background-color: transparent; border: none;")
        self.CITY_LIST_LAYOUT.CITY_LIST_SCROLL_AREA_FRAME_LAYOUT.addWidget(self)
        
        self.CITY_LAYOUT = widgets.QHBoxLayout()
        self.CITY_LAYOUT.setContentsMargins(0, scale.scale_y(8), 0, scale.scale_y(8))
        self.CITY_LAYOUT.setSpacing(0)
        self.setLayout(self.CITY_LAYOUT)
        
        self.CITY_LABEL = widgets.QLabel(parent = self, text = city_name)
        self.CITY_LABEL.setFixedSize(scale.scale_x(496), scale.scale_y(20))
        self.CITY_LABEL.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        scale.setFontSize(self.CITY_LABEL,14)
        self.CITY_LAYOUT.addWidget(self.CITY_LABEL)
        
        self.DELETE_BUTTON = widgets.QPushButton(self)
        self.DELETE_BUTTON.setFixedSize(scale.scale_x(16), scale.scale_y(16))
        self.DELETE_BUTTON.setStyleSheet("background-color: transparent; border: none;")
        
        self.DELETE_ICON = gui.QPixmap("media/title_bar/additional_elements/trash.png")
        if not self.DELETE_ICON.isNull():
                scaled_pixmap = self.DELETE_ICON.scaled(scale.scale_x(16),scale.scale_y(16), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
        self.DELETE_BUTTON.setIcon(gui.QIcon(scaled_pixmap))
        self.DELETE_BUTTON.clicked.connect(self.delete)
        self.CITY_LAYOUT.addWidget(self.DELETE_BUTTON)
        
        self.CITY_NAME = city_name
        
    def delete(self):
        main_window = self.window()
        if not main_window:
            return

        weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        left_container = main_window.findChild(widgets.QFrame, "Left_container")

        if weather_container and hasattr(weather_container, 'LIST_OF_SETTINGS_CARDS'):
            if self.card in weather_container.LIST_OF_SETTINGS_CARDS:
                weather_container.LIST_OF_SETTINGS_CARDS.remove(self.card)

        if left_container and hasattr(left_container, 'scroll_frame_layout'):
            left_container.scroll_frame_layout.removeWidget(self.card)

        if self.card in Cards.CARDS_LIST:
            Cards.CARDS_LIST.remove(self.card)

        if self.card in weather_container.LIST_OF_SETTINGS_CARDS:
            weather_container.LIST_OF_SETTINGS_CARDS.remove(self.card)

        self.card.setParent(None)
        self.card.deleteLater()

        parent_layout = self.parent().layout() if self.parent() else None
        if parent_layout:
            parent_layout.removeWidget(self)
            
        if self in CityListLable.CITY_LIST:
            CityListLable.CITY_LIST.remove(self)
        
        self.setParent(None)
        self.deleteLater()
        
        clear_weather_frame(weather_container=weather_container)
    def change_size(self, scale):
        if isdeleted(self):
            return
        self.setFixedSize(scale.scale_x(512), scale.scale_y(32))

        self.CITY_LABEL.setFixedSize(
            scale.scale_x(496),
            scale.scale_y(20)
        )
        scale.setFontSize(self.CITY_LABEL,14)
        self.DELETE_BUTTON.setFixedSize(
            scale.scale_x(16),
            scale.scale_y(16)
        )

        self.DELETE_BUTTON.setIcon(
            gui.QIcon(
                self.DELETE_ICON.scaled(
                    scale.scale_x(16),
                    scale.scale_y(16),
                    core.Qt.AspectRatioMode.KeepAspectRatio, 
                    core.Qt.TransformationMode.SmoothTransformation
                )
            )
        )
