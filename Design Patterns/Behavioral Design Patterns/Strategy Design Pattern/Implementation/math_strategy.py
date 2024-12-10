from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def calculation(a, b):
        pass


class Addition(Strategy):
    def calculation(a, b):
        return a + b 

class Substraction(Strategy):
    def calculation(a, b):
        return a - b


class Context:
    def __init__(self, strategy):
        self.__strategy = strategy
    
    def execute_strategy(self, a, b):
        return self.__strategy.calculation(a, b)
    

# Client 
a = 45.619
b = 98.454

context = Context(Addition())
print(context.execute_strategy(a, b))

context = Context(Substraction())
print(context.execute_strategy(a, b))


