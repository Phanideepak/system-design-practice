from abc import ABC

class Shape:
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print('Drawing Shape : Rectangle')

class Circle(Shape):
    def draw(self):
        print('Drawing Shape: Circle')

# You need to decorate the shape. 
class ShapeDecorator(Shape, ABC):
    def __init__(self, decorated_shape):
        self._decorated_shape = decorated_shape
    
    def draw(self):
        return self._decorated_shape.draw()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self, decorated_shape):
        super().__init__(decorated_shape)
    
    def __set_red_border(self, decorated_shape):
        print('Border Color red')

    def draw(self):
        self._decorated_shape.draw()
        self.__set_red_border(self._decorated_shape)

circle = Circle()

print('circle of default color')
circle.draw()

red_circle = RedShapeDecorator(Circle())
print('circle of red color')
red_circle.draw()

red_rectangle = RedShapeDecorator(Rectangle())
print('rectang of red color')
red_rectangle.draw()