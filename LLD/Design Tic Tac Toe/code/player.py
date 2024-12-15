from piece import Piece

class Player:
    def __init__(self, name, piece : Piece):
        self.__name = name 
        self.__playing_piece = piece
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_piece(self):
        return self.__playing_piece
    
    def set_piece(self, piece):
        self.__playing_piece = piece