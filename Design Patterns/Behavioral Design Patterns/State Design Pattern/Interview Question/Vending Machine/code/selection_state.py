from state_abstract_class import State
from dispense_state import DispenseState
from idle_state import IdleState

class SelectionState(State):
    def __init__(self):
        print('Currently Vending machine is in SelectionState')
    
    def click_on_insert_coin_button(self, machine):
        raise Exception('you can not click on insert coin button in Selection state')
    
    def click_on_start_item_selection_button(self, machine):
        pass

    def insert_coin(self, machine, coin):
        raise Exception('you can not insert Coin in selection state')
    
    def choose_product(self, machine, code_number):
        item = machine.get_inventory().get_item(code_number)

        paid_by_user = 0

        for coin in machine.get_coin_list():
            paid_by_user += coin.name
        
        if paid_by_user < item.get_price():
            print(f'Insufficient amount , Product you selected is for price: {item.get_price()} and you paid {paid_by_user}')
            self.refund_full_money(machine)
            raise Exception('insufficent amount')
        else:
            if paid_by_user > item.get_price():
                self.get_change(paid_by_user - item.get_price())
            machine.set_vending_machine_state(DispenseState(machine, code_number))
    
    def get_change(self, return_change_money):
        print(f'Returned the change in coin dispense tray: {return_change_money}')
    
    def refund_full_money(self, machine):
       print('Returned the full amount back in the Coin Dispense Tray')
       machine.set_vending_machine_state(IdleState(machine))
       return machine.get_coin_list()
    
    def dispense_product(self, machine, code_number):
        raise Exception('product can not be dispensed Selection state')
    
    def update_inventory(self, machine, item, code_number):
       raise Exception('Inventory can not be updated in Selection state')