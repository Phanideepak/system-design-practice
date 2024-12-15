from state_abstract_class import State
from accept_money_state import AcceptMoneyState

class IdleState(State):
    def __init__(self, machine):
        print('Currently vending machine is in `IdleState`')
        if machine:
            machine.set_coin_list([])

    def click_on_insert_coin_button(self, machine):
        machine.set_vending_machine_state(AcceptMoneyState())
    
    def click_on_start_item_selection_button(self, machine):
        raise Exception('first you need to click on insert coin button')
    
    def insert_coin(self, machine, coin):
        raise Exception('You can not insert coin in `Idle` state')
    
    def choose_product(self, machine, code_number):
        raise Exception('You can not choose product in `Idle` state')

    def get_change(self, return_change_money):
        raise Exception('You can not get change in `Idle` state')
    
    def refund_full_money(machine):
        raise Exception('You can not get reffunded in `Idle` state')

    def dispense_product(self, machine, code_number):
        raise Exception('You can not get dispensed in `Idle` state')
    
    def update_inventory(self, machine, item, code_number):
        machine.get_inventory().add_item(item, code_number)
    
