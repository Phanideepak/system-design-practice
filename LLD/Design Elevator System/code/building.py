from floor import Floor

class Building:
    def __init__(self, floors):
        self.__floors = floors
    
    def add_floor(self, floor : Floor):
        self.__floors.append(floor)
    
    def remove_floor(self, floor : Floor):
        self.__floors.remove(floor)
    
    def get_floor_list(self):
        return self.__floors