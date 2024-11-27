class Memento:
    def __init__(self, state):
        self.__state = state
    
    def get_state(self):
        return self.__state


class Originator:
    def __init__(self):
        self.__state = None
    
    def set_state(self, state):
        self.__state = state
    
    def get_state(self):
        return self.__state

    def save_state_to_memento(self):
        return Memento(self.__state)
    
    def get_state_from_memento(self, memento : Memento):
        self.__state = memento.get_state()


class CareTaker:
    def __init__(self):
        self.__mementos = []
    
    def add(self, state : Memento):
        self.__mementos.append(state)
    
    def get(self, index):
        return self.__mementos[index]


#Client Code.
originator = Originator()
caretaker = CareTaker()

originator.set_state('State 1')
caretaker.add(originator.save_state_to_memento())
originator.set_state('State 2')
caretaker.add(originator.save_state_to_memento())
originator.set_state('State 3')
caretaker.add(originator.save_state_to_memento())
originator.set_state('State 4')
caretaker.add(originator.save_state_to_memento())

print(f'Current state: {originator.get_state()}')

originator.get_state_from_memento(caretaker.get(0))
print(f'First saved state : {originator.get_state()}')

originator.get_state_from_memento(caretaker.get(1))
print(f'Second saved state : {originator.get_state()}')

originator.get_state_from_memento(caretaker.get(2))
print(f'Third saved state : {originator.get_state()}')
