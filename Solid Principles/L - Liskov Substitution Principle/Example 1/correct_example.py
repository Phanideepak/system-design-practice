class Bike:
    def accelerate(self):
       pass

class EngineBike(Bike):
    def turn_on_engine(self):
       pass

class MotorCycle(EngineBike):
    def __init__(self, is_engine_on, speed):
        self.is_engine_on = is_engine_on
        self.speed = speed
    
    def turn_on_engine(self):
        self.is_engine_on = True
    
    def accelerate(self):
        self.speed += 10

class Cycle(Bike):
    def __init__(self, speed):
        self.speed = speed
    
    def accelerate(self):
        self.speed += 2

class Main:

    def accelerate_bike(bike : Bike):
        print('Accelaration Started')
        bike.accelerate()
        print('Succesfully Accelerated')
    
    if __name__ == '__main__':
        cycle = Cycle(15)
        accelerate_bike(cycle)