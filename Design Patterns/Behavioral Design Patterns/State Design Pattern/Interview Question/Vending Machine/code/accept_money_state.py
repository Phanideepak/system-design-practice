from state_abstract_class import State
from coin import Coin
from idle_state import IdleState
from selection_state import SelectionState

class AcceptMoneyState(State):
    def __init__(self):
        print('Currenlty Vending machine is in HasMoneyState')
    
    def click_on_insert_coin_button(self, machine):
        pass 

    def click_on_start_item_selection_button(self, machine):
        machine.set_vending_machine_state(SelectionState())
    
    def insert_coin(self, machine, coin : Coin):
        print('Accepted Coin')
        machine.get_coin_list.append(coin)
    
    def choose_product(self, machine, code_number):
        raise Exception('You need to click on start item selection button first')
    
    def get_change(self, return_change_money):
        raise Exception('You cannot get change in hasMoney state')
    
    def dispense_product(self, machine, code_number):
        raise Exception('product cannot be dispensed in hasMoney state')
    
    def refund_full_money(self, machine):
        print('returned full amount back in coin dispense tray')
        machine.set_vending_machine_state(IdleState())
        return machine.get_coin_list()

    def update_inventory(self, machine, item, code_number):
        raise Exception('You can not update inventory in hasMoney State')
