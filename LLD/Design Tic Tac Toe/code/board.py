from piece import Piece

class Board:
    def __init__(self, size):
        self.__size = size
        self.__board = [[None for i in range((size))] for j in range((size))]
    
    def get_size(self):
        return self.__size

    def get_board(self):
        return self.__board
    
    def add_piece(self, row, col, playing_piece : Piece):
        if self.__board[row][col]:
            return False
        
        self.__board[row][col] = playing_piece

        return True

    def get_free_cells(self):
        free_cells = []

        for i in range((self.__size)):
            for j in range((self.__size)):
                if not self.__board[i][j] :
                    free_cells.append((i,j))

        return free_cells

    def print_board(self):
        for i in range((self.__size)):
            for j in range((self.__size)):
                if self.__board[i][j]:
                    print(f'{self.__board[i][j]} ', end='')
                else:
                    print('  ', end='')
                    
                print(' | ', end = '')
            print()