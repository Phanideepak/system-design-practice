from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod    
    def undo(self):
        pass

class TurnOnCommand(ICommand):
    def __init__(self, ac):
        self.__air_conditioner = ac 
    
    def execute(self):
        ac.turn_on()
    
    def undo(self):
        ac.turn_off()

class TurnOffCommand(ICommand):
    def __init__(self, ac):
        self.__air_conditioner = ac 
    
    def execute(self):
        ac.turn_off()
    
    def undo(self):
        ac.turn_on()


class AirConditioner:
    def __init__(self):
        self.__is_on = None
        self.__temperature = None
    
    def turn_on(self):
        self.__is_on = True
        print('AC is on')
    
    def turn_off(self):
        self.__is_on = False
        print('AC is off')
    
    def set_temperature(self, temp):
        self.__temperature = temp
        print(f'temperature changed to {self.__temperature}')


class RemoteControl:
    def __init__(self):
        self.__command = None
        self.__ac_command_history = []

    def set_command(self, command):
        self.__command = command
    
    def press_button(self):
        self.__command.execute()
        self.__ac_command_history.append(self.__command)
    
    def undo(self):
        if not self.__ac_command_history:
            last_command = self.__ac_command_history.pop()
            last_command.undo()


ac = AirConditioner()

remote_control = RemoteControl()

remote_control.set_command(TurnOnCommand(ac))

remote_control.press_button()

remote_control.undo()
