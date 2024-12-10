class Product:
    def __init__(self, name = None, price = None):
        self.__name = name
        self.__price = price 


class ProductDao:
    def get_product(self, product_id):
        return Product()


class Payment:
    def make_payment(self):
        return True

class Invoice:
    def generate_invoice(self):
        pass


class SendNotification:
    def  send_notification(self):
        pass


class OrderFacade:
    def __init__(self):
        self.__product_dao = ProductDao()
        self.__invoice = Invoice()
        self.__payment = Payment()
        self.__notification = SendNotification()
    
    def create_order(self):
        product = self.__product_dao.get_product(1)
        self.__payment.make_payment()
        self.__invoice.generate_invoice()
        self.__notification.send_notification()


# Client Code
order_facade = OrderFacade()

order_facade.create_order()