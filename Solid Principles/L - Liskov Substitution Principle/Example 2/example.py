class Payment:
    def process(self, card_number):
        pass 

class CreditCardPayment(Payment):
    def process(self, card_number):
        print(f'Processing Credit Card Payment: {card_number}')

class PayPalPayment(Payment):
    def process(self, card_number):
        raise NotImplementedError("Paypal does not use card number")