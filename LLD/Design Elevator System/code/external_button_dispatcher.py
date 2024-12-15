from direction import Direction

class ExternalButtonDispatcher:
    def __init__(self):
        self.controllers = []
    
    def submit_external_request(self, floor_num, direction : Direction):
        for controller in self.controllers:
            elevator_id = controller.elevator.id
            if elevator_id % 2 == floor_num%2:
                controller.submit_external_request(floor_num, direction)
