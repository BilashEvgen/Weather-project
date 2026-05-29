import PyQt6.QtWidgets as widgets

class Horizontal_Scroll(widgets.QScrollArea):
    def wheelEvent(self, event):
        delta_y = event.angleDelta().y()
        if delta_y == 0:
            return super().wheelEvent(event)

        hbar = self.horizontalScrollBar()
        step = hbar.singleStep() or 20
        
        num_notches = delta_y / 120
        new_value = hbar.value() - int(num_notches * step)
        hbar.setValue(new_value)
        event.accept()