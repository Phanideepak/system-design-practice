from abc import abstractmethod, ABC

# Observable Interface
class StocksObservable(ABC):
    @abstractmethod
    def add(self, observer):
        pass 

    @abstractmethod    
    def remove(self, observer):
        pass

    @abstractmethod    
    def notify(self):
        pass

    @abstractmethod    
    def get_stock_count(self):
        pass 

    @abstractmethod
    def set_stock_count(self, new_stock_added):
        pass



# Iphone Stock Observable Concrete class
class IphoneStocksObservable(StocksObservable):
    def __init__(self):
        self.__observers = []
        self.__stock_count = 0

    def add(self, observer):
        self.__observers.append(observer)
    
    def remove(self, observer):
        self.__observers.remove(observer)
    
    def notify(self):
        for observer in self.__observers:
            observer.update()
    
    def set_stock_count(self, new_stock_added):
        if self.__stock_count == 0:
            self.notify()
        self.__stock_count += new_stock_added

    def get_stock_count(self):
        return self.__stock_count 


# Notification Alert Observer interface
class NotificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, email_id, observable):
        self.__email_id = email_id
        self.__observable = observable
    
    def update(self):
        self.__send_mail('Product is in stock hurry up!')
    
    def __send_mail(self, msg):
        print(f'Mail : {msg} sent to {self.__email_id}')


class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, username, observable):
        self.__username = username
        self.__observable = observable
    
    def update(self):
        self.__send_sms('Product is in stock hurry up!')
    
    def __send_sms(self, msg):
        print(f'SMS : {msg} delivered to {self.__username}')



# Client Code
iphone_stock_observable = IphoneStocksObservable()

observer1 = EmailAlertObserver('abc@gmail.com', iphone_stock_observable)
observer2 = EmailAlertObserver('abc1@gmail.com', iphone_stock_observable)
observer3 = MobileAlertObserver('testing user', iphone_stock_observable)

iphone_stock_observable.add(observer1)
iphone_stock_observable.add(observer2)
iphone_stock_observable.add(observer3)

iphone_stock_observable.set_stock_count(20)