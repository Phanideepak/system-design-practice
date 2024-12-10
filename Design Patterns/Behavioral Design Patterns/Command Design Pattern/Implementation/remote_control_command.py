from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass 

    @abstractmethod    
    def undo(self):
        pass


# Receiver
class Light:
    def turn_on(self):
        print('Light is On')
    
    def turn_off(self):
        print('Light is off')


# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.__light = light
    
    def execute(self):
        self.__light.turn_on()
    
    def undo(self):
        self.__light.turn_off()


# Concrete Command
class LightOffCommand(Command):
    def __init__(self, light):
        self.__light  = light
    
    def execute(self):
        self.__light.turn_off()
    
    def undo(self):
        self.__light.turn_on()
    

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None 
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()
    
    def press_undo(self):
        if self.command:
            self.command.undo()



# Client
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote : RemoteControl = RemoteControl()

remote.set_command(light_on)
remote.press_button()

remote.press_undo()

remote.set_command(light_off)
remote.press_button()

remote.press_undo()