from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def get_notification(self):
        pass 

    @abstractmethod
    def send_notification(self, recipient):
        pass

class SMSNotification(Notification):
    def get_notification(self):
        return 'SMS'
    
    def send_notification(self, recipient):
        print(f'SMS sent to {recipient}')

class EmailNotification(Notification):
    def get_notification(self):
        return 'Email'
    
    def send_notification(self, recipient):
        print(f'Email sent to {recipient}')

class Order(ABC):
    @abstractmethod
    def get_order(self):
        pass 

    @abstractmethod    
    def mark_order_delivered(self):
        pass

class CustomerOrder(Order):
    def get_order(self):
        return 'Customer Order'
    
    def mark_order_delivered(self):
        print('Customer Order Marked Delivered')

class MerchantOrder(Order):
    def get_order(self):
        return 'Merchant Order'
    
    def mark_order_delivered(self):
        print('Merchant Order Delivered')

class AbstractFactory(ABC):
    @abstractmethod
    def getOrder(self, order):
        pass 

    @abstractmethod    
    def getNotification(self, notification):
        pass

class OrderFactory(AbstractFactory):
    def getOrder(self, order):
        if order == 'customer':
            return CustomerOrder()
        if order == 'merchant':
            return MerchantOrder()
        raise ValueError(f'Invalid Order type: {order}')
    
    def getNotification(self, notification):
        raise NotImplementedError('Invalid  operation')

class NotificationFactory(AbstractFactory):
    def getOrder(self, order):
       raise NotImplementedError('Invalid  operation')

    def getNotification(self, notification):
        if notification == 'sms':
            return SMSNotification()
        if notification == 'email':
            return EmailNotification()
        raise ValueError('Invalid Notification Type') 

class FactoryCreator:
    @staticmethod
    def getFactory(factory):
        if factory == 'order':
            return OrderFactory()
        if factory == 'notification':
            return NotificationFactory()
        raise ValueError('Invalid Factory type')

factory = FactoryCreator.getFactory('order')

order = factory.getOrder('customer')

order.mark_order_delivered()