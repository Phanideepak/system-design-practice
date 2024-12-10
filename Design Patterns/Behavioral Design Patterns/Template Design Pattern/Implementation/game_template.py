from abc import abstractmethod, ABC

class Game(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod    
    def start(self):
        pass 

    @abstractmethod    
    def end(self):
        pass 
   
    def play(self):
        self.initialize()
        self.start()
        self.end()


class Chess(Game):
    def initialize(self):
        print('Chess Game initialized! Start Playing')
    
    def start(self):
        print('Game started. Welcome to in the chess game')
    
    def end(self):
        print('Game Finished')


class Soccer(Game):
    def initialize(self):
        print('Soccer Game initialized! Start Playing')
    
    def start(self):
        print('Game started. Welcome to in the soccer game')
    
    def end(self):
        print('Game Finished')


# Client Code

chess = Chess()
chess.play()

soccer = Soccer()
soccer.play()