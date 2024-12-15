from elevator_car import ElevatorCar
from elevator_controller import ElevatorController

class ElevatorCreator:
    def __init__(self, n):
        self.controllers = []

        for i in range(n):
            elevator = ElevatorCar()
            elevator.id = i+1
            self.controllers.append(ElevatorController(elevator))