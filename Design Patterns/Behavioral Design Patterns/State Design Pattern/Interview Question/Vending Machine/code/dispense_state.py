from state_abstract_class import State
from idle_state import IdleState

class DispenseState(State):

    def __init__(self, machine, code_number):
        print('Currently Vending machine is in DispenseState')
        self.dispense_product(machine, code_number)
    
    def click_on_insert_coin_button(self, machine):
        raise Exception('insert coin button can not clicked on Dispense state')

    def click_on_start_item_selection_button(self, machine):
        raise Exception('product selection buttion can not be clicked in Dispense state')
    
    def insert_coin(self, machine, coin):
        raise Exception('coin can not be inserted in Dispense state')
    
    def choose_product(self, machine, code_number):
        raise Exception('product can not be choosen in Dispense state')

    def get_change(self, return_change_money):
        raise Exception('change can not returned in Dispense state')
    
    def refund_full_money(self, machine):
        raise Exception('refund can not be happen in Dispense state')
    
    def dispense_product(self, machine, code_number):
        print('Product has been dispensed')
        item = machine.get_inventory().get_item(code_number)
        machine.get_inventory().update_sold_out_item(code_number)
        machine.set_vending_machine_state()
        return item