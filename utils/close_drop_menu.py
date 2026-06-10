import PyQt6.QtWidgets as widgets



def close_drop_menu(main_window) :
    try :
        main_window.findChild(widgets.QLineEdit, "SEARCH_FIELD").DROP_DOWN_FRAME.hide()
        main_window.findChild(widgets.QFrame, "DROP_COUNTRY_MODAL").DROP_DOWN_FRAME.hide()
        main_window.findChild(widgets.QFrame, "DROP_CITY_MODAL").DROP_DOWN_FRAME.hide()
    except :
        pass