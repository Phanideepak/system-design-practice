class AirConditioner:
    def __init__(self):
        self.__is_one = None
        self.__temperature = None
    
    def turn_on(self):
        self.__is_one = True
        print('AC is on')
    
    def turn_off(self):
        self.__is_one = False
        print('AC is off')
    
    def set_temperature(self, temp):
        self.__temperature = temp
        print(f'temperature changed to {self.__temperature}')


ac = AirConditioner()

ac.turn_on()
ac.set_temperature(32)
ac.turn_off()
