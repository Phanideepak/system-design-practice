class Bike:
    def turn_on_engine(self):
       pass

    def accelerate(self):
       pass

class MotorCycle(Bike):
    def __init__(self, is_engine_on, speed):
        self.is_engine_on = is_engine_on
        self.speed = speed
    
    def turn_on_engine(self):
        self.is_engine_on = True
    
    def accelerate(self):
        self.speed += 10

class Cycle(Bike):
    def __init__(self, is_engine_on, speed):
        self.is_engine_on = is_engine_on
        self.speed = speed
    
    def turn_on_engine(self):
        raise NotImplementedError('Cycle has no Engine')
    
    def accelerate(self):
        self.speed += 2
    

def switch_on_engine(bike : Bike):
    print('Turning on the engine')
    bike.turn_on_engine()
    print('Engine successfully turned on')

cycle = Cycle(None, 15)

switch_on_engine(cycle)
    
        