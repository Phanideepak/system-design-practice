from inventory import Inventory
from state_abstract_class import State
from idle_state import IdleState


class VendingMachine:
    def __init__(self):
        self.__vending_machine_state = IdleState()
        self.__inventory = Inventory()
        self.__coin_list = []
    
    def get_vending_machine_state(self):
        return self.__vending_machine_state

    def set_vending_machine_state(self, state : State):
        self.__vending_machine_state = state
    
    def get_inventory(self):
        return self.__inventory
    
    def set_inventory(self, inventory):
        self.__inventory = inventory
    
    def get_coin_list(self):
        return self.__coin_list
    
    def set_coin_list(self, coin_list):
        self.__coin_list = coin_list