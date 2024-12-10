class ConfigurationMemento:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height


class ConfigurationOriginator:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    
    def set_width(self, width):
        self.__width = width
    
    def set_height(self, height):
        self.__height = height
    
    def create_memento(self):
        return ConfigurationMemento(self.__height, self.__width)

    def restore_memento(self, memento : ConfigurationMemento):
        self.__height = memento.get_height()
        self.__width = memento.get_width()
    
    def __str__(self):
        return f'Originator : height = {self.__height} and width = {self.__width}'


class ConfigurationCareTaker:
    def __init__(self):
        self.__history = []

    def add_memento(self, memento):
        self.__history.append(memento)

    def undo(self):
        if self.__history :
            last_memento = self.__history[-1]
            self.__history.pop()

            return last_memento
        
        return None 



# Client Code

caretaker = ConfigurationCareTaker()

originator = ConfigurationOriginator(11, 22)

print(originator)

snapshot_1 = originator.create_memento()
caretaker.add_memento(snapshot_1)

originator.set_height(24)
originator.set_width(34)

print(originator)

snapshot_2 = originator.create_memento()
caretaker.add_memento(snapshot_2)

originator.set_height(46)
originator.set_width(98)

print(originator)

# UNDO
restored_memento = caretaker.undo()
originator.restore_memento(restored_memento)

print(originator)

