from abc import ABC, abstractmethod

class ApprovalHandler(ABC):
    def __init__(self, next_handler = None):
        self.next_handler : ApprovalHandler = next_handler
    
    @abstractmethod
    def handle_request(self, request):
        pass

class Manager(ApprovalHandler):
    def handle_request(self, request):
        if request <= 10:
            print(f'Manager approved the request of amount {request}')
        elif self.next_handler:
            print('Manager can not approve. Passing to the next level...')
            self.next_handler.handle_request(request)

class Director(ApprovalHandler):
    def handle_request(self, request):
        if request <= 50:
            print(f'Director approved the request of amount {request}')
        elif self.next_handler:
            print('Director can not approve. Passing to the next level...')
            self.next_handler.handle_request(request)

class CEO(ApprovalHandler):
    def handle_request(self, request):
        print(f'CEO approved the request of amount {request}')


ceo = CEO()
director = Director(ceo)
manager = Manager(director)


# Send requests
manager.handle_request(5)
manager.handle_request(20)
manager.handle_request(100)