import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as gui
import PyQt6.QtCore as core
from utils import clear_layout, close_drop_menu
from ..cards import Cards
from utils import scale

class AppLanguage(widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName("APPLANGUAGE")
        self.CHOOSED = False
        self.WEATHER_CONTAINER = self.window().findChild(widgets.QFrame, "WEATHER_CONTAINER")
        self.MODAL_WINDOW = self.window().findChild(widgets.QWidget, "MODAL_WINDOW")
        self.setFixedSize(158,35)
        self.setStyleSheet("background-color: transparent")
        self.LAYOUT = widgets.QVBoxLayout()
        self.LAYOUT.setContentsMargins(8, 8, 0, 8)
        self.setLayout(self.LAYOUT)
        
        self.LABEL2 = widgets.QLabel(text = "Мова додатку")
        self.LABEL2.setFixedWidth(150)
        self.LABEL2.setStyleSheet("color: white;border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        scale.setFontSize(self.LABEL2,16)
        self.LAYOUT.addWidget(self.LABEL2)
        
    def create_frame(self):
        if not self.MODAL_WINDOW or not hasattr(self.MODAL_WINDOW, "SETTINGS_CONTEINER_RIGHT_LAYOUT") or not hasattr(self.MODAL_WINDOW, "SETTINGS_CONTEINER_RIGHT"):
            return
        self.language = self.window().findChild(widgets.QFrame,"WEATHER_CONTAINER").LANGUAGE
        if self.language == "Українська":
            self.choose_language_label = "Оберіть мову додатку"
            self.app_language_label = "Мова додатку"
            self.save_language_button = "Зберегти"
        elif self.language == "English" :
            self.choose_language_label = "Select app language"
            self.app_language_label = "App language"
            self.save_language_button = "Save"
        self.CHOOSED = True

        self.SETTINGS_LAYOUT = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT_LAYOUT
        self.SETTINGS_FRAME = self.MODAL_WINDOW.SETTINGS_CONTEINER_RIGHT
        
        self.SETTINGS_LAYOUT.setContentsMargins(0,0,scale.scale_x(305),scale.scale_y(417))
        
        self.CHOOSE_LANGUAGE_FRAME = widgets.QFrame()
        self.CHOOSE_LANGUAGE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(161))
        self.CHOOSE_LANGUAGE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")
        self.SETTINGS_LAYOUT.addWidget(self.CHOOSE_LANGUAGE_FRAME)

        self.CHOOSE_LANGUAGE_LAYOUT = widgets.QVBoxLayout()
        self.CHOOSE_LANGUAGE_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.CHOOSE_LANGUAGE_LAYOUT.setSpacing(scale.scale_y(24))
        self.CHOOSE_LANGUAGE_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignTop)

        self.CHOOSE_LANGUAGE_FRAME.setLayout(self.CHOOSE_LANGUAGE_LAYOUT)
        
        self.CHOOSE_LANGUAGE_LABEL = widgets.QLabel(text = self.choose_language_label)
        self.CHOOSE_LANGUAGE_LABEL.setStyleSheet("color: white; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 400;")
        scale.setFontSize(self.CHOOSE_LANGUAGE_LABEL,18)
        self.CHOOSE_LANGUAGE_LABEL.setFixedSize(scale.scale_x(239), scale.scale_y(21))

        self.CHOOSE_LANGUAGE_LAYOUT.addWidget(self.CHOOSE_LANGUAGE_LABEL, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
        self.APP_LANGUAGE_FRAME = widgets.QFrame()
        self.APP_LANGUAGE_FRAME.setFixedSize(scale.scale_x(239), scale.scale_y(54))
        self.APP_LANGUAGE_FRAME.setStyleSheet("background-color: transparent; border-radius: 0px;")

        self.APP_LANGUAGE_LAYOUT = widgets.QVBoxLayout()
        self.APP_LANGUAGE_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.APP_LANGUAGE_LAYOUT.setSpacing(0)
        self.APP_LANGUAGE_FRAME.setLayout(self.APP_LANGUAGE_LAYOUT)

        self.CHOOSE_LANGUAGE_LAYOUT.addWidget(self.APP_LANGUAGE_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)

        self.APP_LANGUAGE_LABEL = widgets.QLabel(text = self.app_language_label )
        self.APP_LANGUAGE_LABEL.setFixedSize(scale.scale_x(93), scale.scale_y(22))
        self.APP_LANGUAGE_LABEL.setStyleSheet("color: white; border-radius: 0px; background-color: transparent; font-family: Roboto; font-weight: 500;")
        scale.setFontSize(self.APP_LANGUAGE_LABEL,14)
        self.APP_LANGUAGE_LAYOUT.addWidget(self.APP_LANGUAGE_LABEL, alignment = core.Qt.AlignmentFlag.AlignLeft)

        self.APP_LANGUAGE_DROP_DOWN_MENU = widgets.QComboBox(self.APP_LANGUAGE_FRAME)
        self.APP_LANGUAGE_DROP_DOWN_MENU.setFixedSize(scale.scale_x(239), scale.scale_y(32))
        self.APP_LANGUAGE_DROP_DOWN_MENU.setStyleSheet("background-color: white; color: black; border-radius: 4px; padding-left: 8px;")
        scale.setFontSize(self.APP_LANGUAGE_DROP_DOWN_MENU, 12)
        
        if self.WEATHER_CONTAINER.LANGUAGE == "Українська":
            self.APP_LANGUAGE_DROP_DOWN_MENU.addItem("Українська")
            self.APP_LANGUAGE_DROP_DOWN_MENU.addItem("English")
        elif self.WEATHER_CONTAINER.LANGUAGE == "English":
            self.APP_LANGUAGE_DROP_DOWN_MENU.addItem("English")
            self.APP_LANGUAGE_DROP_DOWN_MENU.addItem("Українська")    
        
        self.APP_LANGUAGE_LAYOUT.addWidget(self.APP_LANGUAGE_DROP_DOWN_MENU)

        
        self.SAVE_LANGUAGE_BUTTON = widgets.QPushButton(text = self.save_language_button)
        self.SAVE_LANGUAGE_BUTTON.setFixedSize(scale.scale_x(105), scale.scale_y(38))
        self.SAVE_LANGUAGE_BUTTON.setStyleSheet("background-color: rgba(0,0,0,0.2); border-radius: 4px; color: white; font-family: Roboto; font-weight: 400;")
        scale.setFontSize(self.SAVE_LANGUAGE_BUTTON,14)
        self.SAVE_LANGUAGE_BUTTON.clicked.connect(self.change_language)
        
        self.CHOOSE_LANGUAGE_LAYOUT.addWidget(self.SAVE_LANGUAGE_BUTTON, alignment = core.Qt.AlignmentFlag.AlignLeft)
        
    def change_language(self):
        if self.WEATHER_CONTAINER and hasattr(self.WEATHER_CONTAINER, 'LANGUAGE'):
            self.WEATHER_CONTAINER.LANGUAGE = self.APP_LANGUAGE_DROP_DOWN_MENU.currentText()
            language = self.WEATHER_CONTAINER.LANGUAGE
        else:
            language = self.APP_LANGUAGE_DROP_DOWN_MENU.currentText()

        main_window = self.window()
        weather_container = main_window.findChild(widgets.QFrame, "WEATHER_CONTAINER")
        search_field = main_window.findChild(widgets.QLineEdit, "SEARCH_FIELD")
        search_city = main_window.findChild(widgets.QFrame, "SEARCHCITY")
        app_size = main_window.findChild(widgets.QFrame, "APPSIZE")
        app_icons = main_window.findChild(widgets.QFrame, "APPICONS")
        country_menu = main_window.findChild(widgets.QFrame, "CONTRYMENU")
        city_menu = main_window.findChild(widgets.QFrame, "CITYMENU")
        modal_window = main_window.findChild(widgets.QWidget, "MODAL_WINDOW")

        
        def safe_set_text(widget, text):
            try:
                widget.setText(text)
            except RuntimeError:
                pass
        
        if language == "English":
            
            for cardd in Cards.CARDS_LIST:
                if cardd and hasattr(cardd, "REQUEST_DATA") :
                    self.REQUEST_DATA = cardd.REQUEST_DATA
                    self.GEOCODING_DATA = cardd.GEOCODING_DATA
                    weather_eng = self.REQUEST_DATA["weather"][0]["main"].capitalize()
                    city_name = cardd.CITY_NAME
                    if cardd.SELECTED:
                        if cardd and hasattr(cardd, "FIRST_VERTICAL_CARD"):
                            safe_set_text(cardd.FIRST_VERTICAL_CARD.TIME_LABEL, "Now")
                        if cardd and hasattr(cardd, "SUNMOVE_CARDS_LIST"):
                            for sun_card in cardd.SUNMOVE_CARDS_LIST:
                                if sun_card and hasattr(sun_card, "TEXT_LABEL"):
                                    try:
                                        text = sun_card.TEXT_LABEL.text()
                                        if text == "Захід сонця":
                                            safe_set_text(sun_card.TEXT_LABEL, "Sunset")
                                        elif text == "Схід сонця":
                                            safe_set_text(sun_card.TEXT_LABEL, "Sunrise")
                                    except RuntimeError:
                                        pass
                        if weather_container and hasattr(weather_container, 'LEFT_CITY_LABEL'):
                            safe_set_text(weather_container.LEFT_CITY_LABEL, city_name)
                        if weather_container and hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL1') and self.REQUEST_DATA:
                            safe_set_text(weather_container.LEFT_DESCRIPTION_LABEL1, weather_eng)
                        if weather_container and hasattr(weather_container, 'RIGHT_DATA_LABEL1'):
                            safe_set_text(weather_container.RIGHT_DATA_LABEL1, cardd.DAY_STR)
                        if weather_container and hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL2') and self.REQUEST_DATA:
                            safe_set_text(weather_container.LEFT_DESCRIPTION_LABEL2, f"Max.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Min.:{int(self.REQUEST_DATA["main"]["temp_min"])}°")
                    if cardd and hasattr(cardd, "FRAME1_LABEL1"):
                        safe_set_text(cardd.FRAME1_LABEL1, city_name)
                    if cardd and hasattr(cardd, "FRAME2_LABEL2") and self.REQUEST_DATA:
                        safe_set_text(cardd.FRAME2_LABEL2, f"Max.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Min.:{int(self.REQUEST_DATA["main"]["temp_min"])}°")
                    if cardd and hasattr(cardd, "FRAME1_LABEL3") and self.REQUEST_DATA:
                        safe_set_text(cardd.FRAME1_LABEL3, weather_eng)
                
            
            
            if weather_container and hasattr(weather_container, 'TOP_SETTINGS_FRAME_LABEL'):
                safe_set_text(weather_container.TOP_SETTINGS_FRAME_LABEL, "Settings")
            if weather_container and hasattr(weather_container, 'RIGHT_TODAY_LABEL'):
                safe_set_text(weather_container.RIGHT_TODAY_LABEL, "Today")
            if weather_container and hasattr(weather_container, 'ADD_BUTTON_LABEL'):
                safe_set_text(weather_container.ADD_BUTTON_LABEL, "Add")
            if weather_container and hasattr(weather_container, 'DAY_WEATHER_TOP_LABEL'):
                safe_set_text(weather_container.DAY_WEATHER_TOP_LABEL, "Expected weather forecast for 5 days")
            if weather_container and hasattr(weather_container, 'DIAGRAM_LABEL'):
                safe_set_text(weather_container.DIAGRAM_LABEL, "Forecast for 36 hours")
            if search_field and hasattr(search_field, 'DROP_DOWN_LABEL'):
                safe_set_text(search_field.DROP_DOWN_LABEL, "Search results")
            if search_field:
                try:
                    search_field.setPlaceholderText("Search")
                except RuntimeError:
                    pass
            if search_city and hasattr(search_city, 'LABEL'):
                safe_set_text(search_city.LABEL, "City search")
            if search_city and hasattr(search_city, 'SEARCH_CITY_LABEL'):
                safe_set_text(search_city.SEARCH_CITY_LABEL, "City search")
            if search_city and hasattr(search_city, 'COUNTRY_LABEL'):
                safe_set_text(search_city.COUNTRY_LABEL, "Country")
            if search_city and hasattr(search_city, 'CITY_LABEL'):
                safe_set_text(search_city.CITY_LABEL, "City")
            if search_city and hasattr(search_city, 'COORDINATE_LABEL1'):
                safe_set_text(search_city.COORDINATE_LABEL1, "Coordinates")
            if search_city and hasattr(search_city, 'SAVE_BUTTON'):
                safe_set_text(search_city.SAVE_BUTTON, "Save")
            if search_city and hasattr(search_city, 'BOTTOM_FRAME_LABEL'):
                safe_set_text(search_city.BOTTOM_FRAME_LABEL, "Added cities")
            if hasattr(self, 'LABEL2'):
                safe_set_text(self.LABEL2, "App language")
            if app_size and hasattr(app_size, 'LABEL1'):
                safe_set_text(app_size.LABEL1, "App size")
            if app_icons and hasattr(app_icons, 'LABEL3'):
                safe_set_text(app_icons.LABEL3, "Lists of images")
            safe_set_text(self.CHOOSE_LANGUAGE_LABEL, "Select app language")
            safe_set_text(self.APP_LANGUAGE_LABEL, "App language")
            safe_set_text(self.SAVE_LANGUAGE_BUTTON, "Save")
            if country_menu and hasattr(country_menu, 'COUNTRY_LINEEDIT'):
                try:
                    country_menu.COUNTRY_LINEEDIT.setPlaceholderText("Select coutry")
                except RuntimeError:
                    pass
            if city_menu and hasattr(city_menu, 'CITY_LINEEDIT'):
                try:
                    city_menu.CITY_LINEEDIT.setPlaceholderText("Select city")
                except RuntimeError:
                    pass
            if modal_window and hasattr(modal_window, 'HEADER_FRAME_LABEL'):
                safe_set_text(modal_window.HEADER_FRAME_LABEL, "Settings")
                
        elif language == "Українська":
            
            
            for cardd in Cards.CARDS_LIST:
                if cardd and hasattr(cardd, "REQUEST_DATA") and hasattr(cardd, "GEOCODING_DATA"):
                    self.REQUEST_DATA = cardd.REQUEST_DATA
                    self.GEOCODING_DATA = cardd.GEOCODING_DATA
                    weather_ua = self.REQUEST_DATA["weather"][0]["description"].capitalize()
                    try:
                        city_name_ua = self.GEOCODING_DATA[0]["local_names"]["uk"]  
                    except:
                        city_name_ua = cardd.CITY_NAME
                    if cardd.SELECTED:
                        if cardd and hasattr(cardd, "FIRST_VERTICAL_CARD"):
                            safe_set_text(cardd.FIRST_VERTICAL_CARD.TIME_LABEL, "Зараз")
                        if cardd and hasattr(cardd, "SUNMOVE_CARDS_LIST"):
                            for sun_card in cardd.SUNMOVE_CARDS_LIST:
                                if sun_card and hasattr(sun_card, "TEXT_LABEL"):
                                    try:
                                        text = sun_card.TEXT_LABEL.text()
                                        if text == "Sunset":
                                            safe_set_text(sun_card.TEXT_LABEL, "Захід сонця")
                                        elif text == "Sunrise":
                                            safe_set_text(sun_card.TEXT_LABEL, "Схід сонця")
                                    except RuntimeError:
                                        pass
                        if weather_container and hasattr(weather_container, 'LEFT_CITY_LABEL'):
                            safe_set_text(weather_container.LEFT_CITY_LABEL, city_name_ua)
                        if weather_container and hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL1') and self.REQUEST_DATA:
                            safe_set_text(weather_container.LEFT_DESCRIPTION_LABEL1, weather_ua)
                        if weather_container and hasattr(weather_container, 'RIGHT_DATA_LABEL1'):
                            safe_set_text(weather_container.RIGHT_DATA_LABEL1, cardd.UA_DAY_STR)
                        if weather_container and hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL2') and self.REQUEST_DATA:
                            safe_set_text(weather_container.LEFT_DESCRIPTION_LABEL2, f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°")
                    if cardd and hasattr(cardd, "FRAME1_LABEL1"):
                        safe_set_text(cardd.FRAME1_LABEL1, city_name_ua)
                    if cardd and hasattr(cardd, "FRAME2_LABEL2") and self.REQUEST_DATA:
                        safe_set_text(cardd.FRAME2_LABEL2, f"Макс.:{int(self.REQUEST_DATA["main"]["temp_max"])}°, Мін.:{int(self.REQUEST_DATA["main"]["temp_min"])}°")
                    if cardd and hasattr(cardd, "FRAME1_LABEL3") and self.REQUEST_DATA:
                        safe_set_text(cardd.FRAME1_LABEL3, weather_ua)
            
            
            if weather_container and hasattr(weather_container, 'TOP_SETTINGS_FRAME_LABEL'):
                safe_set_text(weather_container.TOP_SETTINGS_FRAME_LABEL, "Налаштування")
            if weather_container and hasattr(weather_container, 'RIGHT_TODAY_LABEL'):
                safe_set_text(weather_container.RIGHT_TODAY_LABEL, "Сьогодні")
            if weather_container and hasattr(weather_container, 'ADD_BUTTON_LABEL'):
                safe_set_text(weather_container.ADD_BUTTON_LABEL, "Додати")
            if weather_container and hasattr(weather_container, 'DAY_WEATHER_TOP_LABEL'):
                safe_set_text(weather_container.DAY_WEATHER_TOP_LABEL, "Очікуваний прогноз погоди на 5 днів")
            if weather_container and hasattr(weather_container, 'DIAGRAM_LABEL'):
                safe_set_text(weather_container.DIAGRAM_LABEL, "Прогноз на 36 годин")
            if search_field and hasattr(search_field, 'DROP_DOWN_LABEL'):
                safe_set_text(search_field.DROP_DOWN_LABEL, "Результати пошуку")
            if search_field:
                try:
                    search_field.setPlaceholderText("Пошук")
                except RuntimeError:
                    pass
            if search_city and hasattr(search_city, 'LABEL'):
                safe_set_text(search_city.LABEL, "Пошук міста")
            if search_city and hasattr(search_city, 'SEARCH_CITY_LABEL'):
                safe_set_text(search_city.SEARCH_CITY_LABEL, "Пошук міста")
            if search_city and hasattr(search_city, 'COUNTRY_LABEL'):
                safe_set_text(search_city.COUNTRY_LABEL, "Кріїна")
            if search_city and hasattr(search_city, 'CITY_LABEL'):
                safe_set_text(search_city.CITY_LABEL, "Місто")
            if search_city and hasattr(search_city, 'COORDINATE_LABEL1'):
                safe_set_text(search_city.COORDINATE_LABEL1, "Координати")
            if search_city and hasattr(search_city, 'SAVE_BUTTON'):
                safe_set_text(search_city.SAVE_BUTTON, "Зберегти")
            if search_city and hasattr(search_city, 'BOTTOM_FRAME_LABEL'):
                safe_set_text(search_city.BOTTOM_FRAME_LABEL, "Додані міста")
            if hasattr(self, 'LABEL2'):
                safe_set_text(self.LABEL2, "Мова додатку")
            if app_size and hasattr(app_size, 'LABEL1'):
                safe_set_text(app_size.LABEL1, "Розмір додатку")
            if app_icons and hasattr(app_icons, 'LABEL3'):
                safe_set_text(app_icons.LABEL3, "Списки зображень")
            safe_set_text(self.CHOOSE_LANGUAGE_LABEL, "Оберіть мову додатку")
            safe_set_text(self.APP_LANGUAGE_LABEL, "Мова додатку")
            safe_set_text(self.SAVE_LANGUAGE_BUTTON, "Зберегти")
            if country_menu and hasattr(country_menu, 'COUNTRY_LINEEDIT'):
                try:
                    country_menu.COUNTRY_LINEEDIT.setPlaceholderText("Виберіть країну")
                except RuntimeError:
                    pass
            if city_menu and hasattr(city_menu, 'CITY_LINEEDIT'):
                try:
                    city_menu.CITY_LINEEDIT.setPlaceholderText("Виберіть місто")
                except RuntimeError:
                    pass
            if modal_window and hasattr(modal_window, 'HEADER_FRAME_LABEL'):
                safe_set_text(modal_window.HEADER_FRAME_LABEL, "Налаштування")
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