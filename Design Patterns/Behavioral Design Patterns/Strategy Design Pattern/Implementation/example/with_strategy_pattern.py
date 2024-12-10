# Base Vehicle
class Vehicle:
    def __init__(self, drive_strategy):
        self.strategy = drive_strategy
        
    def drive(self):
        self.strategy.drive()

# interface
class DriveStrategy:
    def drive(self):
        pass 

class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print('Normal Driving Capability')

class SportDriveStrategy(DriveStrategy):
    def drive(self):
        print('Sports Driving Capability') 


class SportsVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportDriveStrategy())


class OffLoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SportDriveStrategy())

class PassengerVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())


class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDriveStrategy())
