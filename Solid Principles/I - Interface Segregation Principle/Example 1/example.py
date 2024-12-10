class RestaurantEmployee:
    def bill_order(self):
        pass
    def cook_food(self):
        pass
    def serve_customer(self):
        pass

class Waiter(RestaurantEmployee):
    def bill_order(self):
        raise NotImplementedError('Bill Order Not Supported for Waiter')

    def cook_food(self):
        raise NotImplementedError('Cook Food Not Supported for Waiter')

    def serve_customer(self):
        print('Serve Customer')


if __name__ == '__main__':
    def bill_order_operations(emp : RestaurantEmployee):
        emp.bill_order()
    
    waiter = Waiter()
    bill_order_operations(waiter)