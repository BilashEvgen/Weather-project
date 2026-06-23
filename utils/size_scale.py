
class SizeScale():
    def __init__(self):
        self.BASE_WIDTH = 1200
        self.BASE_HEIGHT = 800

        self.x = 1.0
        self.y = 1.0

    
    def update_size(self,window_width,window_height):
        self.x = window_width / self.BASE_WIDTH
        self.y = window_height / self.BASE_HEIGHT

    
    def scale_x(self, value):
        return round(value * self.x)

    
    def scale_y(self, value):
        return round(value * self.y)
    
    
    def scale_font(self, value):
        return round(value * min(self.x, self.y))
    
   
    def setFontSize(self, widget, size):
        font = widget.font()
        font.setPixelSize(self.scale_font(size))
        widget.setFont(font)
scale = SizeScale()