from .clear_layout import clear_layout

def clear_weather_frame(weather_container) :

    if weather_container:
        if hasattr(weather_container, 'LEFT_CITY_LABEL'):
            weather_container.LEFT_CITY_LABEL.setText("")
        if hasattr(weather_container, 'LEFT_WEATHER_LABEL'):
            weather_container.LEFT_WEATHER_LABEL.setText("")
        if hasattr(weather_container, 'LEFT_WEATHER_LABEL11'):
            weather_container.LEFT_WEATHER_LABEL11.setText("")
        if hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL1'):
            weather_container.LEFT_DESCRIPTION_LABEL1.setText("")
        if hasattr(weather_container, 'LEFT_DESCRIPTION_LABEL2'):
            weather_container.LEFT_DESCRIPTION_LABEL2.setText("")
        if hasattr(weather_container, 'LEFT_WEATHER_ICON'):
            weather_container.LEFT_WEATHER_ICON.clear()
        if hasattr(weather_container, 'RIGHT_DATA_LABEL1'):
            weather_container.RIGHT_DATA_LABEL1.setText("")
        if hasattr(weather_container, 'RIGHT_DATA_LABEL2'):
            weather_container.RIGHT_DATA_LABEL2.setText("")
        if hasattr(weather_container, 'RIGHT_CLOCK_LABEL'):
            weather_container.RIGHT_CLOCK_LABEL.setText("")
        if hasattr(weather_container, 'RIGHT_CLOCK_FRAME'):
            weather_container.RIGHT_CLOCK_FRAME.clear()
        if hasattr(weather_container, 'DAY_WEATHER_SCROLL_FRAME_LAYOUT'):
            clear_layout(weather_container.DAY_WEATHER_SCROLL_FRAME_LAYOUT)
        if hasattr(weather_container, 'FORECAST_DIAGRAM_ICON_FRAME_LAYOUT'):
            clear_layout(weather_container.FORECAST_DIAGRAM_ICON_FRAME_LAYOUT)
        if hasattr(weather_container, 'FORECAST_DIAGRAM_ITSELF_LAYOUT'):
            clear_layout(weather_container.FORECAST_DIAGRAM_ITSELF_LAYOUT)