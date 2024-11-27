from datetime import datetime
from abc import ABC, abstractmethod

# Interface
class ApnaChatRoom:
    def show_message(self, msg, participant):
        pass

# ChatRoomImpl implements ChatRoom
class ApnaChatRoomImpl(ApnaChatRoom):
    def show_message(self, msg, participant):
        print(f'Participant - {participant.get_name()} gets message {msg}')
        print(datetime.now())
        return super().show_message(msg, participant)


# Participant Class
class Participant(ABC):
    @abstractmethod
    def set_name(self, name):
        pass  

    @abstractmethod
    def get_name(self):
        pass 

    @abstractmethod    
    def send_message(self, message):
        pass


class User(Participant):
    def __init__(self, chat):
        self.__chat : ApnaChatRoom = chat
        self.__name = None 
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def send_message(self, message):
        self.__chat.show_message(message, self)
    

# Client Code
chat_room = ApnaChatRoomImpl()

first_user = User(chat_room)
first_user.set_name('Vikram')
first_user.send_message('Hello Vikram, How are you')

second_user = User(chat_room)
second_user.set_name('Jaiswal')
second_user.send_message('I am fine. You tell!')