# Flyweight Interface
class IRobot:
    def display(self, x, y):
        pass

class HumanRobot(IRobot):
    def __init__(self, type, body):
        self.__type = type
        self.__sprite = body
    
    def get_type(self):
        return self.__type
    
    def get_sprite(self):
        return self.__sprite

    def display(self, x, y):
        pass

class DogRobot(IRobot):
    def __init__(self, type, body):
        self.__type = type
        self.__sprite = body
    
    def get_type(self):
        return self.__type
    
    def get_sprite(self):
        return self.__sprite

    def display(self, x, y):
        pass

class Sprite:
    pass

robotic_cache = dict()

class RoboticFactory:
    
    def create_robot(robot_type):
        if  robot_type not in robotic_cache:
            if robot_type == 'HUMANOID':
                robotic_cache[robot_type] = HumanRobot(robot_type, Sprite())
            elif robot_type == 'DOG_ROBOT':
               robotic_cache[robot_type] = DogRobot(robot_type, Sprite()) 
            else:
                raise ValueError('Invalid Robot type')
        
        return robotic_cache[robot_type]


human_robot_1 = RoboticFactory.create_robot('HUMANOID')
human_robot_1.display(11, 22)

human_robot_2 = RoboticFactory.create_robot('HUMANOID')
human_robot_2.display(11, 22)
