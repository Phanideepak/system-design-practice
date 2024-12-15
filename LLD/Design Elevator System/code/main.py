from floor import Floor
from building import Building
from elevator_creator import ElevatorCreator

floors = []

for i in range(5):
    floors.append(Floor(i+1))

building = Building(floors)

elevator_creator = ElevatorCreator(n = 2)