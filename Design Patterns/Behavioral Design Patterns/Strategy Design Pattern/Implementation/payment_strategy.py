from abc import abstractmethod, ABC

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        print(f'Paid {amount} using Credit Card ending in {self.card_number[-4:]}')

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email 
    
    def pay(self, amount):
        print(f'Paid {amount} using Paypal account : {self.email}')

class BitCoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f'Paid {amount} using Bitcoin strategy')

# Context
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0.0 
    
    def add_item(self, item, price):
        self.items.append(item)
        self.total += price 
    
    def checkout(self, payment_strategy : PaymentStrategy):
        payment_strategy.pay(self.total)


# Client
cart = ShoppingCart()
cart.add_item('Laptop', 999.55)
cart.add_item('Mouse', 20.19)

payment_method = PayPalPayment('abc123@gmail.com')
cart.checkout(payment_method)