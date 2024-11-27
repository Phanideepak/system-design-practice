# Legacy Code
class OldPaymentGateway:
    def process_payment(self, amount):
        return f'Processing Payment of ${amount} through old gateway'

# Target Interface
class NewPaymentGateway:
    def make_payment(self, amount):
        pass

# Payment Adapter that inherits NewPaymentGateway and contains object of OldPaymentGateway
class PaymentAdapter(NewPaymentGateway):
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway
    
    def make_payment(self, amount):
        return self.old_gateway.process_payment(amount)

old_gateway = OldPaymentGateway()
adapter = PaymentAdapter(old_gateway)

print(adapter.make_payment(1000))
        
