import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import clear_layout
from utils import scale
from ..app import application
from ..cards import Cards

class AppSize(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("APPSIZE")
        self.CHOOSED = False
        self.MODAL_WINDOW = self.window().findChild(widgets.QWidget,"MODAL_WINDOW")
        self.setFixedSize(158,35)
        self.setStyleSheet("background-color: transparent")
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 0, 8)
        self.setLayout(self.LAYOUT)
        
        self.LABEL1 = widgets.QLabel(text = "Розмір додакту")
        self.LABEL1.setFixedWidth(150)
        self.LABEL1.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        scale.setFontSize(self.LABEL1,16)
        self.LAYOUT.addWidget(self.LABEL1)
        
    def create_frame(self):
        self.SETTINGS_LAYOUT = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT
        self.SETTINGS_FRAME = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT
        
        self.SETTINGS_LAYOUT.setContentsMargins(0, 0, 305, 359)
        self.SETTINGS_LAYOUT.setSpacing(0)
        
        self.language = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER").LANGUAGE
        if self.language == "Українська":
            self.choose_size_label = "Оберіть розмір додатку"
            self.save_button_label = "Зберегти"
        elif self.language == "English" :
            self.choose_size_label  = "Select app size"
            self.save_button_label = "Save"
        
        
        self.SIZE_FRAME = widgets.QFrame(parent = self.SETTINGS_FRAME)
        self.SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(219))
        self.SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        self.SETTINGS_LAYOUT.addWidget(self.SIZE_FRAME )
        
        self.SIZE_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.SIZE_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.SIZE_FRAME_LAYOUT.setSpacing(24)
        self.SIZE_FRAME.setLayout(self.SIZE_FRAME_LAYOUT)

        self.CHOOSE_SIZE_LABEL = widgets.QLabel(text = self.choose_size_label)
        self.CHOOSE_SIZE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignLeft)
        self.CHOOSE_SIZE_LABEL.setFixedSize(scale.scale_x(239), scale.scale_y(21))
        self.CHOOSE_SIZE_LABEL.setStyleSheet("color: white; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        scale.setFontSize(self.CHOOSE_SIZE_LABEL,18)

        self.SIZE_FRAME_LAYOUT.addWidget(self.CHOOSE_SIZE_LABEL)

        
        self.LIST_OF_SIZE_FRAME = widgets.QFrame()
        self.LIST_OF_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(112))
        self.LIST_OF_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        self.SIZE_FRAME_LAYOUT.addWidget(self.LIST_OF_SIZE_FRAME)

        self.LIST_OF_SIZE_FRAME_LAYOUT = widgets.QVBoxLayout()
        self.LIST_OF_SIZE_FRAME_LAYOUT.setContentsMargins(0,0,0,0)
        self.LIST_OF_SIZE_FRAME_LAYOUT.setSpacing(16)
        self.LIST_OF_SIZE_FRAME.setLayout(self.LIST_OF_SIZE_FRAME_LAYOUT)

        self.FIRST_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.FIRST_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.FIRST_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.FIRST_SIZE_FRAME)
        
        self.STYLESHEET = """
            QRadioButton {
                color: white;
                border-radius: 0px;
                background-color: transparent;
                font-family: Roboto;
                font-weight: 400;
            }

            QRadioButton::indicator {
                
                image: url(media/title_bar/additional_elements/idle_radiobutton.png)
            }

            QRadioButton::indicator:checked {
                
                image: url(media/title_bar/additional_elements/selected_radiobutton.png)
            }
            """
            
        self.FIRST_SIZE_BUTTON = widgets.QRadioButton(parent = self.FIRST_SIZE_FRAME, text = "1200x800")
        self.FIRST_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.FIRST_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.FIRST_SIZE_BUTTON,14)
        
        self.SECOND_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.SECOND_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.SECOND_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.SECOND_SIZE_FRAME)

        self.SECOND_SIZE_BUTTON = widgets.QRadioButton(parent = self.SECOND_SIZE_FRAME, text = "1440x1024")
        self.SECOND_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.SECOND_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.SECOND_SIZE_BUTTON,14)
        
        self.THIRD_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.THIRD_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.THIRD_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.THIRD_SIZE_FRAME)

        self.THIRD_SIZE_BUTTON = widgets.QRadioButton(parent = self.THIRD_SIZE_FRAME, text = "1512x982")
        self.THIRD_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.THIRD_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.THIRD_SIZE_BUTTON,14)
        
        self.FOURTH_SIZE_FRAME = widgets.QFrame(parent = self.LIST_OF_SIZE_FRAME)
        self.FOURTH_SIZE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        self.FOURTH_SIZE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px")
        
        self.LIST_OF_SIZE_FRAME_LAYOUT.addWidget(self.FOURTH_SIZE_FRAME)

        self.FOURTH_SIZE_BUTTON = widgets.QRadioButton(parent = self.FOURTH_SIZE_FRAME, text = "1728x1117")
        self.FOURTH_SIZE_BUTTON.setStyleSheet(self.STYLESHEET)
        self.FOURTH_SIZE_BUTTON.setFixedSize(scale.scale_x(239), scale.scale_y(16))
        scale.setFontSize(self.FOURTH_SIZE_BUTTON,14)













        self.BUTTON_GROUP = widgets.QButtonGroup(self.SIZE_FRAME)
        self.BUTTON_GROUP.addButton(self.FIRST_SIZE_BUTTON)
        self.BUTTON_GROUP.addButton(self.SECOND_SIZE_BUTTON)
        self.BUTTON_GROUP.addButton(self.THIRD_SIZE_BUTTON)
        self.BUTTON_GROUP.addButton(self.FOURTH_SIZE_BUTTON)
        
        
        self.SAVE_BUTTON = widgets.QPushButton(self.SIZE_FRAME, text = self.save_button_label)
        self.SAVE_BUTTON.clicked.connect(self.change_size)
        self.SAVE_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))
        self.SAVE_BUTTON.setStyleSheet("background-color: rgba(0, 0, 0, 0.2); border-radius: 4px; color: white;font-family: 'Roboto'; font-weight: 400;")
        scale.setFontSize(self.SAVE_BUTTON,14)
        self.SIZE_FRAME_LAYOUT.addWidget(self.SAVE_BUTTON)
        
    def change_size(self):
        
        main_window = self.window()
        weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        search_field = main_window.findChild(widgets.QLineEdit, "SEARCH_FIELD")
        search_city = main_window.findChild(widgets.QFrame, "SEARCHCITY")
        app_icons = main_window.findChild(widgets.QFrame, "APPICONS")
        app_language = main_window.findChild(widgets.QFrame, "APPLANGUAGE")
        country_menu = main_window.findChild(widgets.QFrame, "CONTRYMENU")
        city_menu = main_window.findChild(widgets.QFrame, "CITYMENU")
        modal_window = main_window.findChild(widgets.QWidget, "MODAL_WINDOW")
        search_frame = main_window.findChild(widgets.QFrame, "SEARCH_FRAME")
        left_container = main_window.findChild(widgets.QFrame, "Left_container")
        
        
        size_text = self.BUTTON_GROUP.checkedButton().text()
        window_width, window_height = map(int, size_text.split("x"))
        screen = application.primaryScreen()
        screen_size = screen.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()
        center_x = (screen_width // 2) - (window_width // 2)
        center_y = (screen_height // 2) - (window_height // 2)

        main_window.setGeometry(center_x, center_y, window_width, window_height)
        
        scale.update_size(window_width,window_height)
        
        weather_container.setFixedSize(scale.scale_x(828), scale.scale_y(760))
        weather_container.TOP_FRAME.setFixedSize(scale.scale_x(790), scale.scale_y(36))
        weather_container.TOP_SETTINGS_FRAME.setFixedSize(scale.scale_x(144), scale.scale_y(36))
        weather_container.TOP_SETTINGS_FRAME_BUTTON.setFixedSize(scale.scale_x(36), scale.scale_y(36))
        weather_container.TOP_SETTINGS_FRAME_LABEL.setFixedSize(scale.scale_x(98), scale.scale_y(20))
        scale.setFontSize(weather_container.TOP_SETTINGS_FRAME_LABEL,14)
        weather_container.TOP_ADD_SEARCH_FRAME.setFixedSize(scale.scale_x(368), scale.scale_y(36))
        weather_container.ADD_FRAME.setFixedSize(scale.scale_x(97), scale.scale_y(36))
        weather_container.ADD_BUTTON.setFixedSize(scale.scale_x(97), scale.scale_y(36))
        weather_container.ADD_BUTTON_ICON.setFixedSize(scale.scale_x(16), scale.scale_y(22))
        weather_container.ADD_BUTTON_LABEL.setFixedSize(scale.scale_x(58), scale.scale_y(22))
        scale.setFontSize(weather_container.ADD_BUTTON_LABEL,17)
        weather_container.MAIN_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(677))
        weather_container.MOMENT_WEATHER_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(303))
        weather_container.LEFT_MOMENT_FRAME.setFixedSize(scale.scale_x(390), scale.scale_y(303))
        weather_container.LEFT_MOMENT_TOP_FRAME.setFixedSize(scale.scale_x(358), scale.scale_y(27))
        weather_container.LEFT_CITY_LABEL.setFixedSize(scale.scale_x(390), scale.scale_y(52))
        weather_container.LEFT_WEATHER_FRAME.setFixedSize(scale.scale_x(197), scale.scale_y(87))
        weather_container.LEFT_WEATHER_ICON.setFixedSize(scale.scale_x(76), scale.scale_y(87))
        weather_container.LEFT_WEATHER_LABEL11.setFixedSize(scale.scale_x(25), scale.scale_y(65))
        weather_container.LEFT_DESCRIPTION_FRAME.setFixedSize(scale.scale_x(259), scale.scale_y(57))
        weather_container.LEFT_DESCRIPTION_LABEL1.setFixedSize(scale.scale_x(259), scale.scale_y(28))
        weather_container.LEFT_DESCRIPTION_LABEL2.setFixedSize(scale.scale_x(259), scale.scale_y(19))
        weather_container.RIGHT_MOMENT_FRAME.setFixedSize(scale.scale_x(390), scale.scale_y(303))
        weather_container.RIGHT_TODAY_FRAME.setFixedSize(scale.scale_x(358), scale.scale_y(27))
        weather_container.RIGHT_TODAY_LABEL.setFixedSize(scale.scale_x(67), scale.scale_y(19))
        scale.setFontSize(weather_container.RIGHT_TODAY_LABEL,16)
        weather_container.RIGHT_DATA_FRAME.setFixedSize(scale.scale_x(358), scale.scale_y(44))
        weather_container.RIGHT_DATA_LABEL1.setFixedSize(scale.scale_x(123), scale.scale_y(28))
        weather_container.RIGHT_DATA_LABEL2.setFixedSize(scale.scale_x(123), scale.scale_y(28))
        weather_container.RIGHT_CLOCK_FRAME.setFixedSize(scale.scale_x(168), scale.scale_y(168))
        weather_container.RIGHT_CLOCK_LABEL.setFixedSize(scale.scale_x(74), scale.scale_y(34))
        weather_container.DAY_WEATHER_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(157))
        weather_container.DAY_WEATHER_TOP_LABEL.setFixedSize(scale.scale_x(756), scale.scale_y(27))
        scale.setFontSize(weather_container.DAY_WEATHER_TOP_LABEL,16)
        weather_container.DAY_WEATHER_MAIN_SCROLL_FRAME.setFixedSize(scale.scale_x(756), scale.scale_y(82))
        weather_container.SCROLL_LEFT_BUTTON.setFixedSize(scale.scale_x(16), scale.scale_y(16))
        weather_container.SCROLL_RIGHT_BUTTON.setFixedSize(scale.scale_x(16), scale.scale_y(16))
        weather_container.DAY_WEATHER_SCROLL_PARENT.setFixedSize(scale.scale_x(656), scale.scale_y(82))
        weather_container.DAY_WEATHER_SCROLL_AREA.setFixedSize(scale.scale_x(656), scale.scale_y(82))
        weather_container.DIAGRAM_WEATHER_FRAME.setFixedSize(scale.scale_x(788), scale.scale_y(197))
        weather_container.MAIN_DIAGRAM_FRAME.setFixedSize(scale.scale_x(756), scale.scale_y(165))
        weather_container.DIAGRAM_LABEL.setFixedSize(scale.scale_x(756), scale.scale_y(27))
        scale.setFontSize(weather_container.DIAGRAM_LABEL,16)
        weather_container.FORECAST_DIAGRAM_FRAME.setFixedSize(scale.scale_x(758), scale.scale_y(130))
        weather_container.FORECAST_DIAGRAM_ICON_PARENT_FRAME.setFixedSize(scale.scale_x(758), scale.scale_y(20))
        weather_container.FORECAST_DIAGRAM_ICON_FRAME.setFixedSize(scale.scale_x(730), scale.scale_y(20))
        weather_container.FORECAST_DIAGRAM_ICON_PARENT_CORNER_FRAME.setFixedSize(scale.scale_x(32), scale.scale_y(20))
        weather_container.FORECAST_DIAGRAM_AND_TEMPERATURE_FRAME.setFixedSize(scale.scale_x(758), scale.scale_y(110))
        weather_container.FORECAST_DIAGRAM_ITSELF_FRAME.setFixedSize(scale.scale_x(728), scale.scale_y(110))
        weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL.setFixedSize(scale.scale_x(30), scale.scale_y(110))
        scale.setFontSize(weather_container.FORECAST_TEMPERATURE_ITSELF_LABEL,12)
        
        central_widget = main_window.central_widget
        if central_widget:
            central_widget.setFixedSize(window_width, window_height)

        content_container = main_window.findChild(widgets.QFrame, "Content_container")
        if content_container:
            content_container.setFixedSize(window_width, window_height)

        for cardd in Cards.CARDS_LIST:
            if cardd:
                cardd.setFixedSize(scale.scale_x(330), scale.scale_y(98))
                cardd.FRAME1.setFixedSize(scale.scale_x(200), scale.scale_y(82))
                cardd.FRAME1_LABEL1.setFixedSize(scale.scale_x(200), scale.scale_y(28))
                scale.setFontSize(cardd.FRAME1_LABEL1,24)
                cardd.FRAME1_LABEL2.setFixedSize(scale.scale_x(105), scale.scale_y(14))
                scale.setFontSize(cardd.FRAME1_LABEL2,14)
                cardd.FRAME1_LABEL3.setFixedSize(scale.scale_x(105), scale.scale_y(14))
                scale.setFontSize(cardd.FRAME1_LABEL3,14)
                cardd.FRAME2.setFixedSize(scale.scale_x(110), scale.scale_y(82))
                cardd.FRAME22.setFixedSize(scale.scale_x(85), scale.scale_y(52))
                cardd.FRAME2_LABEL1.setFixedHeight(scale.scale_y(52))
                scale.setFontSize(cardd.FRAME2_LABEL1,44)
                cardd.FRAME2_LABEL11.setFixedHeight(scale.scale_y(44))
                scale.setFontSize(cardd.FRAME2_LABEL11,39)
                cardd.FRAME2_LABEL2.setFixedSize(scale.scale_x(110), scale.scale_y(14))
                scale.setFontSize(cardd.FRAME2_LABEL2,12)
                

                if cardd.SELECTED:
                    if hasattr(cardd, "DIAGRAMM_LIST"):
                        for diagramm in cardd.DIAGRAMM_LIST:
                            diagramm.setFixedWidth(scale.scale_x(8))
                            diagramm.setFixedHeight(scale.scale_y(cardd.heightt))
                            if cardd.weather_forecast_icon and hasattr(cardd, "weather_forecast_icon"):
                                cardd.weather_forecast_icon.setFixedSize(scale.scale_x(16), scale.scale_y(16))
                    if cardd and hasattr(cardd, "SUNMOVE_CARDS_LIST"):
                        for sun_card in cardd.SUNMOVE_CARDS_LIST:
                            if sun_card:
                                if sun_card:
                                    sun_card.setFixedSize(scale.scale_x(90), scale.scale_y(82))
                                    ###
                                    sun_card.TIME_LABEL.setFixedSize(scale.scale_x(90), scale.scale_y(19))
                                    scale.setFontSize(sun_card.TIME_LABEL,16)
                                    sun_card.ICON_LABEL.setFixedSize(scale.scale_x(90), scale.scale_y(24))
                                    sun_card.TEXT_LABEL.setFixedSize(scale.scale_x(90), scale.scale_y(19))
                                    scale.setFontSize(sun_card.TEXT_LABEL,16)
                    if cardd and hasattr(cardd, "VERTICAL_CARD_LIST"):
                        for vert_card in cardd.VERTICAL_CARD_LIST:
                            if vert_card:
                                vert_card.setFixedSize(scale.scale_x(45), scale.scale_y(82))
                                vert_card.TIME_LABEL.setFixedSize(scale.scale_x(45), scale.scale_y(19))
                                scale.setFontSize(vert_card.TIME_LABEL,16)
                                vert_card.WEATHER_LABEL.setFixedSize(scale.scale_x(24), scale.scale_y(24))
                                vert_card.TEMPERATURE_LABEL.setFixedSize(scale.scale_x(25), scale.scale_y(19))
                                scale.setFontSize(vert_card.TEMPERATURE_LABEL,16)
        
        if search_frame:
            search_frame.setFixedSize(scale.scale_x(261), scale.scale_y(36))
            search_frame.SEARCH_LABEL.setFixedSize(scale.scale_x(25), scale.scale_y(22))
            search_frame.CLEAR_BUTTON_FRAME.setFixedSize(scale.scale_x(20), scale.scale_y(20))
            search_frame.clear_button.setFixedSize(scale.scale_x(20), scale.scale_y(20))
            
        if search_field:
            search_field.setFixedSize(scale.scale_x(200), scale.scale_y(22))
            search_field.DROP_DOWN_SCROLL_AREA.setFixedSize(scale.scale_x(261), scale.scale_y(200))
        
        if modal_window:
            modal_window.setGeometry(scale.scale_x(391), scale.scale_y(66), scale.scale_x(790), scale.scale_y(688))
            modal_window.HEADER_FRAME.setFixedSize(scale.scale_x(742), scale.scale_y(28))
            modal_window.HEADER_FRAME_LABEL.setFixedSize(scale.scale_x(168), scale.scale_y(28))
            scale.setFontSize(modal_window.HEADER_FRAME_LABEL,24)
            modal_window.CLOSE_BUTTON.setFixedSize(scale.scale_x(24), scale.scale_y(24))
            modal_window.SETTINGS_CONTEINER.setFixedSize(scale.scale_x(742), scale.scale_y(578))
            modal_window.SETTINGS_CONTEINER_LEFT.setFixedSize(scale.scale_x(174), scale.scale_y(578))
            modal_window.SETTINGS_CONTEINER_LEFT_OPTIONS_FRAME.setFixedSize(scale.scale_x(158), scale.scale_y(140))
            modal_window.SETTINGS_CONTEINER_RIGHT.setFixedSize(scale.scale_x(544), scale.scale_y(578))
            
        if left_container:
            left_container.setFixedSize(scale.scale_x(370), scale.scale_y(800))
            left_container.leftcontainer_header.setFixedSize(scale.scale_x(370), scale.scale_y(44))
            left_container.CHANGE_THEME_BUTTON.setFixedSize(scale.scale_x(54), scale.scale_y(24))
            left_container.frame.setFixedSize(scale.scale_x(370), scale.scale_y(756))
            left_container.scroll_area.setFixedSize(scale.scale_x(370), scale.scale_y(730))

        if search_city:
            search_city.setFixedSize(scale.scale_x(158), scale.scale_y(35))
        
        if self:
            self.setFixedSize(scale.scale_x(158), scale.scale_y(35))
        
        if app_language:
            app_language.setFixedSize(scale.scale_x(158), scale.scale_y(35))        
        
        if app_icons:
            app_icons.setFixedSize(scale.scale_x(158), scale.scale_y(35))
        
        
        
        
        
        
        
        
        
        
        
    def mousePressEvent(self, event):
        self.list_of_options_frames = self.MODAL_WINDOW.LIST_OF_OPTIONS_FRAMES
        if event.button() == core.Qt.MouseButton.LeftButton and self.CHOOSED == False:
            clear_layout(self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT)
            self.create_frame()
            for option in self.list_of_options_frames :
                if option.CHOOSED:
                    option.setStyleSheet("background-color: transparent; border-radius: 0px")
                    option.CHOOSED = False
            self.CHOOSED = True
            self.setStyleSheet("background-color : rgba(0,0,0,0.2); border-radius : 4px")