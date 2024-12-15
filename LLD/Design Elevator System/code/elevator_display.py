from direction import Direction

class ElevatorDisplay:
    def __init__(self):
        self.floor = None
        self.direction = None 
    
    def set_display(self, floor : int, direction : Direction):
        self.floor = floor
        self.direction = direction
    
    def show_display(self):
        print(f'Floor: {self.floor} Direction: {self.direction.name}')
