from internal_button_dispatcher import InternalButtonDispatcher

class InternalButton:
    def __init__(self):
        self.dispatcher = InternalButtonDispatcher()
        self.button_selected = None
        self.available_buttons = [i+1 for i in range(10)]
    
    def press_button(self, destination, elevator_car):
        self.dispatcher.submit_internal_request(destination, elevator_car)