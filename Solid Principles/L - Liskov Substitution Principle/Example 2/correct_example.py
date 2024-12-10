class Payment:
    def process(self):
        pass 

class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def process(self):
        print(f'Processing Credit Card Payment: {self.card_number}')

class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email

    def process(self):
         print(f'Processing PayPal Payment for account email = {self.email}')