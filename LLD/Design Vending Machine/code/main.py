from vending_machine import VendingMachine
from coin import Coin
from typing import List
from item_shelf import ItemShelf
from item import Item
from item_type import ItemType

def fill_up_inventory(vending_machine : VendingMachine):
    slots : List[ItemShelf]  = vending_machine.get_inventory().get_inventory()

    for i in range(len(slots)):
        new_item = Item()
        if i >= 0 and i < 3:
            new_item.set_price(12)
            new_item.set_type(ItemType.COKE)
        elif i>=3 and i < 5:
            new_item.set_price(9)
            new_item.set_type(ItemType.PEPSI)
        elif i>=5 and i<7:
            new_item.set_price(13)
            new_item.set_type(ItemType.JUICE)
        elif i>=7 and i < 10:
            new_item.set_type(ItemType.SODA)
            new_item.set_price(7)
        
        slots[i].set_item(new_item)
        slots[i].set_sold_out(False)

def display_inventory(vending_machine : VendingMachine):
    slots : List[ItemShelf] = vending_machine.get_inventory().get_inventory()
    for slot in slots:
        print(f'Code number: {slot.get_code()} Item: {slot.get_item().get_type().name} Price: {slot.get_item().get_price()} isAvailable: {slot.is_sold_out()}')

if __name__ == '__main__':
    vending_machine = VendingMachine()
    try:
        print('|')
        print('filling up inventory')
        print('|')
        fill_up_inventory(vending_machine)
        display_inventory(vending_machine)

        print('|')
        print('clicking on InsertCoinButton')
        print('|') 

        vending_state = vending_machine.get_vending_machine_state()
        vending_state.click_on_insert_coin_button(vending_machine)

        vending_state = vending_machine.get_vending_machine_state()
        vending_state.insert_coin(vending_state, Coin.NICKEL)
        vending_state.insert_coin(vending_state, Coin.QUARTER)

        print('|')
        print('clicking on ProductSelectionButton')
        print('|') 
        vending_state.click_on_start_item_selection_button(vending_machine)

        vending_state = vending_machine.get_vending_machine_state()
        vending_state.choose_product(vending_machine, 102)

        display_inventory(vending_machine)


    except Exception:
        display_inventory(vending_machine)