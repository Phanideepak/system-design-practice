from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('Drawing a Circle')

class Rectangle(Shape):
    def draw(self):
        print('Drawing Rectangle')

class ShapeFactory:
    @staticmethod
    def getShape(shape):
        if shape == 'circle':
            return Circle()
        if shape == 'rectangle':
            return Rectangle()
        raise NotImplementedError('Shape Not Defined')


circle = ShapeFactory.getShape('circle')

circle.draw()