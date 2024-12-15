from external_button_dispatcher import ExternalButtonDispatcher

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.external_dispatcher = ExternalButtonDispatcher()
    
    def press_button(self, direction):
        self.external_button.press_button(self.floor_number, direction)