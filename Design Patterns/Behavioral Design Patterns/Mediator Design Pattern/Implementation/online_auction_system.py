from abc import ABC, abstractmethod

class Collegue(ABC):
    @abstractmethod
    def place_bid(bid_amount):
        pass 

    @abstractmethod    
    def receive_bid_notification(bid_amount):
        pass 

    @abstractmethod  
    def get_name():
        pass


class AuctionMediator(ABC):
    @abstractmethod
    def add_bidder(self, bidder):
        pass 

    @abstractmethod    
    def place_bid(self, bidder, bid_amount):
        pass


class Auction(AuctionMediator):
    def __init__(self):
        self.__bidders = []
    
    def add_bidder(self, bidder):
        self.__bidders.append(bidder)
    
    def place_bid(self, bidder, bid_amount):
        for element in self.__bidders:
            if element.get_name() != bidder.get_name():
                element.receive_bid_notification(bid_amount)


class Bidder(Collegue):
    def __init__(self, name, auction_mediator):
        self.__name = name
        self.__auction_mediator = auction_mediator
    
    def place_bid(self, bid_amount):
        self.__auction_mediator.place_bid(self, bid_amount)
    
    def receive_bid_notification(self, bid_amount):
        print(f'Bidder : {self.__name} got the notifcation that some one has put bid of bidamount: {bid_amount}')
    
    def get_name(self):
        return self.__name


# Client Code

auction_mediator = Auction()

bidder1 = Bidder('Ram', auction_mediator)
bidder2 = Bidder('Chandra', auction_mediator)

auction_mediator.add_bidder(bidder1)
auction_mediator.add_bidder(bidder2)

bidder1.place_bid(400)
bidder2.place_bid(405)
