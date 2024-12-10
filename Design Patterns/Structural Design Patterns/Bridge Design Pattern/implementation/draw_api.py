# Interface.
class DrawAPI:
    def draw_circle(radius, x, y):
        pass

class RedCircle(DrawAPI):
    def draw_circle(radius, x, y):
        print(f'red circle with radius: {radius}, x : {x}, y : {y} ')

class GreenCircle(DrawAPI):
    def draw_circle(radius, x, y):
        print(f'green circle with radius: {radius}, x : {x}, y : {y} ')

class Shape:
    def __init__(self, drawAPI):
        self.drawAPI = drawAPI
    
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius, drawAPI):
        super(drawAPI)
        self.x = x 
        self.y = y 
        self.radius = radius

    def draw(self):
        self.drawAPI.draw_circle(self.radius, self.x, self.y)

red_circle = Circle(10, 20, 5, RedCircle())
green_circle = Circle(20, 10, 10, GreenCircle())

red_circle.draw()
green_circle.draw()