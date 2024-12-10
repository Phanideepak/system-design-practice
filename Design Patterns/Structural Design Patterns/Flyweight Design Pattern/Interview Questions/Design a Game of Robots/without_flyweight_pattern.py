class Robot:
    def __init__(self, x, y, robot_type, sprite_object):
        self.x = x 
        self.y = y 
        self.robot_type = robot_type
        self.sprite = sprite_object

class Sprite:
    pass

# Client Code

for i in range(500000):
    human_robot = Robot(i, i, 'HUMAN', Sprite())

for i in range(500000):
    dog_robot = Robot(i, i, 'DOG', Sprite())