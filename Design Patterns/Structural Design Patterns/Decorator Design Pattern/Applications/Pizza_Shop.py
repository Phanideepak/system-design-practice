from abc import abstractmethod, ABC

class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass 


class FarmHouse(BasePizza):
    def cost(self):
        return 200


class VegDelight(BasePizza):
    def cost(self):
        return 120

class Margherita(BasePizza):
    def cost(self):
        return 100


class ToppingDecorator(BasePizza, ABC):
    pass 


class ExtraCheese(ToppingDecorator):
    def __init__(self, pizza):
        self.__pizza = pizza
    
    def cost(self):
        return self.__pizza.cost() + 10

class Mushroom(ToppingDecorator):
    def __init__(self, pizza):
        self.__pizza = pizza
    
    def cost(self):
        return self.__pizza.cost() + 15


veg_pizza = VegDelight()

print(veg_pizza.cost())

cheese_mushroom_added_veg_pizza = Mushroom(ExtraCheese(veg_pizza))

print(cheese_mushroom_added_veg_pizza.cost())