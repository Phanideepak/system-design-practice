from piece_type import PieceType

class Piece:
    def __init__(self, piece_type):
        self.piece_type = piece_type
    
    def __str__(self):
        return self.piece_type.name

class CrossPiece(Piece):
    def __init__(self):
        super().__init__(PieceType.X)

class CirclePiece(Piece):
    def __init__(self):
        super().__init__(PieceType.O)
