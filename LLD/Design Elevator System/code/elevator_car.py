from elevator_display import ElevatorDisplay
from internal_button import InternalButton
from elevator_status import ElevatorStatus
from direction import Direction
from elevator_door import ElevatorDoor

class ElevatorCar:
    def __init__(self):
        self.id = None
        self.display = ElevatorDisplay()
        self.internal_button = InternalButton()
        self.elevator_status = ElevatorStatus.IDLE
        self.current_floor = 0
        self.direction = Direction.UP
        self.door = ElevatorDoor()
    
    def set_display(self):
        self.display.set_display(self.current_floor, self.direction)

    def show_display(self):
        self.display.show_display()
    
    def press_button(self, destination_floor):
        self.internal_button.press_button(destination_floor, self)
    
    def move(self, destination_floor, direction : Direction):
        start_floor = self.current_floor

        if direction == Direction.UP:
            for i in range(start_floor, destination_floor+1):
                self.current_floor = i
                self.set_display()
                self.show_display()
                if self.current_floor == destination_floor:
                    return True
        else:
            for i in range(start_floor, destination_floor-1, -1):
                self.current_floor = i
                self.set_display()
                self.show_display()
                if self.current_floor == destination_floor:
                    return True

        return False
       