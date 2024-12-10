import random

class FigureShape:
    def draw(self):
        pass 

class Circle(FigureShape):
    def __init__(self, color):
        self.__color = color 
        self.__x = None
        self.__y = None
        self.__radius = None 
    
    def set_x(self, x):
        self.__x = x 
    
    def set_y(self, y):
        self.__y = y
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def draw(self):
        print(f'Circle : Draw() [Color : {self.__color}, radius : {self.__radius}, x : {self.__x}, y : {self.__y}]')

circle_map = {}

class ShapeFactory:
    def get_color(color):
        circle = circle_map.get(color)

        if(circle is None):
            circle = Circle(color)
            circle_map[color] = circle
            print(f'creating the circle of color : {color}')
        else:
            print(f'circle of {color} is found')
        
        return circle

colors = ["Red", "Violet", "Green", "Indigo", "Yellow", "Orange", "Blue", "Brown", "Sky Blue"]

def get_random_color():
    return colors[random.randrange(0, len(colors))]

def get_random_x():
    return random.randint(50, 200)

def get_random_y():
    return random.randint(50, 200)


for i in range(20):
    circle = ShapeFactory.get_color(colors[i % len(colors)])
    circle.set_radius(100)
    circle.set_x(get_random_x())
    circle.set_y(get_random_y())
    circle.draw()



        