from abc import abstractmethod, ABC

# State Abstract Class
class State(ABC):
    @abstractmethod
    def click_on_insert_coin_button(self, machine):
        pass

    @abstractmethod    
    def click_on_start_item_selection_button(self, machine):
        pass

    @abstractmethod
    def insert_coin(self, machine, coin):
        pass 

    @abstractmethod    
    def choose_product(self, machine, code_number):
        pass 

    @abstractmethod    
    def get_change(self, return_change_money):
        pass

    @abstractmethod 
    def dispense_product(self, machine, code_number):
        pass

    @abstractmethod
    def refund_full_money(machine):
        pass

    @abstractmethod    
    def update_inventory(machine, item, code_number):
        pass 