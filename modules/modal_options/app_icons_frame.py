import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import clear_layout
from .modal_tools import IconPackFrame
from ..cards import Cards
from utils import scale
from utils import close_drop_menu

class AppIcons(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.WEATHER_ICONS_PACK = "main"
        self.setObjectName("APPICONS")
        self.PACK_CHOOSED = None
        self.CHOOSED = False
        self.MODAL_WINDOW = self.window().findChild(widgets.QWidget,"MODAL_WINDOW")
        self.setFixedSize(158,35)
        self.setStyleSheet("background-color: transparent")
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 0, 8)
        self.setLayout(self.LAYOUT)

        self.LABEL3 = widgets.QLabel(text = "Списки зображень")
        self.LABEL3.setFixedWidth(150)
        self.LABEL3.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        scale.setFontSize(self.LABEL3,16)
        self.LAYOUT.addWidget(self.LABEL3)
    
    def create_frame(self):
        
        self.ICON_PACKS_LIST = []
        self.language = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER").LANGUAGE
        if self.language == "Українська":
            self.save_button_label = "Зберегти"
            self.images_list_label = "Список зображень"
            self.add_button_label = "Додати"
        elif self.language == "English" :
            self.save_button_label = "Save"
            self.images_list_label = "List of images"
            self.add_button_label = "Add"
            
        self.SETTINGS_LAYOUT = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT
        self.SETTINGS_FRAME = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT
        
        self.SETTINGS_LAYOUT.setContentsMargins(0,0,scale.scale_x(54),scale.scale_y(129))
        self.SETTINGS_LAYOUT.setSpacing(scale.scale_y(24))
        
        self.IMAGES_LIST = widgets.QLabel(parent = self.SETTINGS_FRAME, text = self.images_list_label)
        self.IMAGES_LIST.setFixedSize(scale.scale_x(490), scale.scale_y(21))
        self.IMAGES_LIST.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Regular; font-weight: 400;")
        scale.setFontSize(self.IMAGES_LIST,18)
        self.SETTINGS_LAYOUT.addWidget(self.IMAGES_LIST)
        
        self.ADD_FRAME = widgets.QFrame(self.SETTINGS_FRAME)
        self.ADD_FRAME.setStyleSheet("background-color: transparent; border-radius: 4px;")
        self.ADD_FRAME.setFixedSize(scale.scale_x(105), scale.scale_y(38))
        self.SETTINGS_LAYOUT.addWidget(self.ADD_FRAME)
        
        self.ADD_FRAME_LAYOUT = widgets.QHBoxLayout(self.ADD_FRAME)
        self.ADD_FRAME_LAYOUT.setContentsMargins(scale.scale_x(8), scale.scale_y(7),scale.scale_x(8), scale.scale_y(7))
        self.ADD_FRAME_LAYOUT.setSpacing(scale.scale_x(7))
        self.ADD_FRAME_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.ADD_FRAME.setLayout(self.ADD_FRAME_LAYOUT)
        
        self.ADD_BUTTON = widgets.QPushButton(self.ADD_FRAME)
        self.ADD_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        self.ADD_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))

        self.ADD_BUTTON_ICON = widgets.QLabel(self.ADD_FRAME)
        self.ADD_BUTTON_ICON.setFixedSize(scale.scale_x(16), scale.scale_y(22))
        
        add_pixmap = gui.QPixmap(f"media/title_bar/additional_elements/plus_circle.png")
        if not add_pixmap.isNull():
            scaled_pixmap = add_pixmap.scaled(scale.scale_x(16), scale.scale_y(16), core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
            self.ADD_BUTTON_ICON.setPixmap(scaled_pixmap)
        
        self.ADD_BUTTON_ICON.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.ADD_BUTTON_ICON.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.ADD_FRAME_LAYOUT.addWidget(self.ADD_BUTTON_ICON, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        self.ADD_BUTTON_LABEL = widgets.QLabel(self.ADD_FRAME, text = self.add_button_label)
        self.ADD_BUTTON_LABEL.setFixedSize(scale.scale_x(58), scale.scale_y(22))
        self.ADD_BUTTON_LABEL.setStyleSheet("color: white;border-radius: 0px;background-color: transparent; font-family: 'Roboto';font-weight: 400;")
        scale.setFontSize(self.ADD_BUTTON_LABEL,17)
        self.ADD_BUTTON_LABEL.setAttribute(core.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.ADD_FRAME_LAYOUT.addWidget(self.ADD_BUTTON_LABEL, alignment = core.Qt.AlignmentFlag.AlignRight)
        
        self.IMAGES_PACK_CHOOSE_FRAME = widgets.QFrame(self.SETTINGS_FRAME)
        self.IMAGES_PACK_CHOOSE_FRAME.setFixedSize(scale.scale_x(490), scale.scale_y(282))
        self.IMAGES_PACK_CHOOSE_FRAME.setStyleSheet("background-color: transparent")
        self.SETTINGS_LAYOUT.addWidget(self.IMAGES_PACK_CHOOSE_FRAME)
        
        self.IMAGES_PACK_CHOOSE_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.IMAGES_PACK_CHOOSE_FRAME_LAYOUT.setSpacing(scale.scale_y(10))
        self.IMAGES_PACK_CHOOSE_FRAME_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.IMAGES_PACK_CHOOSE_FRAME.setLayout(self.IMAGES_PACK_CHOOSE_FRAME_LAYOUT)
        
        self.ICON_PACK_FRAME1 = IconPackFrame(parent = self.IMAGES_PACK_CHOOSE_FRAME, icon_pack = "main", pack_number = 1)
        self.ICON_PACKS_LIST.append(self.ICON_PACK_FRAME1)
        self.ICON_PACK_FRAME2 = IconPackFrame(parent = self.IMAGES_PACK_CHOOSE_FRAME, icon_pack = "additional", pack_number = 2)
        self.ICON_PACKS_LIST.append(self.ICON_PACK_FRAME2)
        for pack in self.ICON_PACKS_LIST:
            if pack.WEATHER_ICONS_PACK == self.PACK_CHOOSED :
                pack.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);")
        self.IMAGES_PACK_CHOOSE_FRAME_LAYOUT.addWidget(self.ICON_PACK_FRAME1)
        self.IMAGES_PACK_CHOOSE_FRAME_LAYOUT.addWidget(self.ICON_PACK_FRAME2)
        
        self.SAVE_BUTTON = widgets.QPushButton(self.SETTINGS_FRAME, text = self.save_button_label)
        self.SAVE_BUTTON.clicked.connect(self.icon_change)
        self.SAVE_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))
        self.SAVE_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px")
        scale.setFontSize(self.SAVE_BUTTON,14)
        self.SETTINGS_LAYOUT.addWidget(self.SAVE_BUTTON)
        
    def mousePressEvent(self, event):
        self.list_of_options_frames = self.MODAL_WINDOW.LIST_OF_OPTIONS_FRAMES
        if event.button() == core.Qt.MouseButton.LeftButton and self.CHOOSED == False:
            close_drop_menu(self.window())
            clear_layout(self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT)
            self.create_frame()
            for option in self.list_of_options_frames :
                if option.CHOOSED:
                    option.setStyleSheet("background-color: transparent; border-radius: 0px")
                    option.CHOOSED = False
            
            self.CHOOSED = True
            self.setStyleSheet("background-color : rgba(0,0,0,0.2); border-radius : 4px")
            
    def icon_change(self):
        weather_container = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER")
        for pack in self.ICON_PACKS_LIST:
            if pack.PACK_SELECTED :
                self.WEATHER_ICONS_PACK = pack.WEATHER_ICONS_PACK 
                self.PACK_CHOOSED = pack.WEATHER_ICONS_PACK 
                for card in Cards.CARDS_LIST:
                    if card.SELECTED:
                        pixmap = gui.QPixmap(f"media/title_bar/weather_icons/weather_icons_{self.WEATHER_ICONS_PACK}/{card.REQUEST_DATA["weather"][0]["icon"]}.png")
                        if not pixmap.isNull():
                            
                            
                            
                            
                            
                            
                            scaled = pixmap.scaled(weather_container.LEFT_WEATHER_ICON_SIZE, core.Qt.AspectRatioMode.KeepAspectRatio, core.Qt.TransformationMode.SmoothTransformation)
                            weather_container.LEFT_WEATHER_ICON.setPixmap(scaled)