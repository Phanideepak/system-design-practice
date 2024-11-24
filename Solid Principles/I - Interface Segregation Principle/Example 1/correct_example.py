class WaiterOperation:
    def serve_customer(self):
        pass
    def collect_bill(self):
        pass

class Waiter(WaiterOperation):
    def serve_customer(self):
        print('Serve Customer')
    
    def collect_bill(self):
        print('collect bill')

class ChefOperation:
    def collect_kitchen_ticket(self):
        pass
    def collect_food(self):
        pass

class Chef(ChefOperation):
    def collect_kitchen_ticket(self):
        print('collect kitchen ticket') 

    def collect_food(self):
        print('collect food')