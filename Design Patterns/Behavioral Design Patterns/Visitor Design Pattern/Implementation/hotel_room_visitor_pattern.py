from abc import ABC, abstractmethod

class RoomElement(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleRoom(RoomElement):
    def __init__(self):
        self.__room_price = 0
    
    def get_price(self):
        return self.__room_price

    def set_price(self, room_price):
        self.__room_price = room_price
    
    def accept(self, visitor):
        visitor.visit(single_room = self)

class DoubleRoom(RoomElement):
   def __init__(self):
        self.__room_price = 0
    
   def get_price(self):
        return self.__room_price
   
   def set_price(self, room_price):
        self.__room_price = room_price
    
   def accept(self, visitor):
        visitor.visit(double_room = self) 

class DeluxeRoom(RoomElement):
   def __init__(self):
        self.__room_price = 0
    
   def get_price(self):
        return self.__room_price

   def set_price(self, room_price):
        self.__room_price = room_price
    
   def accept(self, visitor):
       visitor.visit(deluxe_room = self)


class RoomVisitor(ABC):
    @abstractmethod
    def visit(self, single_room : SingleRoom = None, double_room : DoubleRoom = None, deluxe_room : DeluxeRoom = None):
        pass

class RoomPricingVisitor(RoomVisitor):
    def visit(self, single_room : SingleRoom = None, double_room : DoubleRoom = None, deluxe_room : DeluxeRoom = None):
        if single_room:
            print('Pricing computation logic of single room')
            single_room.set_price(1000)
        if double_room:
            print('Pricing Computation logic of double room')
            double_room.set_price(1000)
        if deluxe_room:
            print('Pricing computation logic of deluxe room')
            deluxe_room.set_price(1000)

class RoomMaintanenceVisitor(RoomVisitor):
    def visit(self, single_room : SingleRoom = None, double_room : DoubleRoom = None, deluxe_room : DeluxeRoom = None):
        if single_room:
            print('Performance maintainance of single room')
        if double_room:
            print('Performance maintainance of double room')
        if deluxe_room:
            print('Performance maintainance of deluxe room')



single_room = SingleRoom()
double_room = DoubleRoom()
deluxe_room = DeluxeRoom()
    

room_price_visitor = RoomPricingVisitor()
single_room.accept(room_price_visitor)
print(single_room.get_price())
double_room.accept(room_price_visitor)
print(double_room.get_price())
deluxe_room.accept(room_price_visitor)
print(deluxe_room.get_price())

room_maintanance_visitor = RoomMaintanenceVisitor()
single_room.accept(room_maintanance_visitor)
double_room.accept(room_maintanance_visitor)
deluxe_room.accept(room_maintanance_visitor)