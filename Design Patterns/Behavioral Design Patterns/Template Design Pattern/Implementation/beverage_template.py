from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print('Boiling Water ....')

    def pour_in_cup(self):
        print('Pouring into the cup')
    
    @abstractmethod
    def brew(self):
        pass 

    @abstractmethod    
    def add_condiments(self):
        pass

class Tea(Beverage):
    def brew(self):
        print('Steeping the tea')
    
    def add_condiments(self):
       print('Adding Lemon .. ')

class Coffee(Beverage):
    def brew(self):
        print('Dripping coffee through filter')
    
    def add_condiments(self):
        print('Adding milk and Sugar')


# Client Code
print('Preparing Coffee')

coffee = Coffee()
coffee.prepare()


print('Preparing Tea')

tea = Tea()
tea.prepare()

