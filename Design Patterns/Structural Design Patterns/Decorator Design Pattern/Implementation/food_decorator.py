from abc import ABC

class Food:
    def prepare_food(self):
        pass 
    def food_price(self):
        pass

class VegFood(Food):
    def prepare_food(self):
        return 'Veg Food'
    
    def food_price(self):
        return 50.0

# Adding Decorator to add Non Veg items to Veg Items
class FoodDecorator(Food, ABC):
    def __init__(self, new_food):
        self.__new_food = new_food

    def prepare_food(self):
        return self.__new_food.prepare_food()
    
    def food_price(self):
        return self.__new_food.food_price()

# Non veg items that neeeds to be added to veg item
class NonVegFood(FoodDecorator):
    def __init__(self, new_food):
        super().__init__(new_food)
    
    def prepare_food(self):
        return super().prepare_food() + ' with roasted chicken and curry'
    
    def food_price(self):
        return super().food_price() + 150

food1 = VegFood()

print(food1.prepare_food(), food1.food_price())


food2 = NonVegFood(food1)

print(food2.prepare_food(), food2.food_price())

