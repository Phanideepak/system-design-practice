# Base Vehicle
class Vehicle:
    def drive(self):
        print('Normal Driving Capability')

class SportsVehicle(Vehicle):
    def drive(self):
        # Sports Vehicle need sports driving capability
        print('Sports Driving Capability')

class OffLoadVehicle(Vehicle):
    def drive(self):
        # OffLoad Vehicle also requires sports driving capability
        print('Sports Driving Capability')

class PassengerVehicle(Vehicle):
    # Passenger Vehicle required normal driving capability
    pass

class GoodsVehicle(Vehicle):
    # Goods Vehicle require normal driving capability
    pass
