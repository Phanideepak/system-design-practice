from direction import Direction
import heapq # default min queue

class ElevatorController:
    def __init__(self, elevator):
        self.elevator = elevator
        self.up_min_pq = [] 
        self.down_max_pq = []
    
    def submit_external_request(self, floor : int, direction : Direction):
        if direction == Direction.DOWN:
            heapq.heappush(self.down_max_pq, -1*floor)
        else:
            heapq.heappush(self.up_min_pq, floor)
    
    def submit_internal_request(self):
        pass

    def control(self):
        pass