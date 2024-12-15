from piece import CrossPiece, CirclePiece
from player import Player
from board import Board

class Game:
    def __init__(self):
        self.players = None
        self.game_board = None
    
    def initialize_game(self, board_size = 3, number_of_players = 2):
        self.players = [None for i in range(number_of_players)]
        cross_piece = CrossPiece()
        self.players[0] = Player('First Player', cross_piece)

        circle_piece = CirclePiece()
        self.players[1] = Player('Second Player', circle_piece)


        self.game_board = Board(board_size)
    
    def start_game(self):
        no_winner = True 

        while no_winner:
            player_turn = self.players.pop(0)

            # Player on turn looks at the board. He looks for free spaces
            self.game_board.print_board()

            free_spaces = self.game_board.get_free_cells()

            if not free_spaces:
                no_winner = False
                continue

            row_col_inputs = input(f'Player: {player_turn.get_name()}  Enter row, column: ')

            (row, col) = (int(el.strip()) for el in row_col_inputs.split(' '))

            print(row, col)

            is_piece_added = self.game_board.add_piece(row, col, player_turn.get_piece())

            if not is_piece_added:
                print('incorrect position chosen, try again !!')
                self.players.insert(0, player_turn)
            else:
                self.players.append(player_turn)

            winner_found = self.is_there_winner(row, col, player_turn.get_piece().piece_type)
            if winner_found:
                return player_turn.get_name()
        
        return 'tie'
    

    def is_there_winner(self, row, col, piece_type):
        row_match = True
        col_match = True
        diagonal_match = True
        anti_diagonal_match = True

        for i in range(self.game_board.get_size()):
            if self.game_board.get_board()[row][i] is None or  self.game_board.get_board()[row][i].piece_type != piece_type:
                row_match = False

        for i in range(self.game_board.get_size()):
            if self.game_board.get_board()[i][col] is None or  self.game_board.get_board()[i][col].piece_type != piece_type:
                col_match = False
        

        i = 0
        j = 0

        while i < self.game_board.get_size():
            if self.game_board.get_board()[i][j] is None or  self.game_board.get_board()[i][j].piece_type != piece_type:
                diagonal_match = False
            i += 1
            j += 1
        
        i = 0
        j = -1
        
        while i < self.game_board.get_size():
            if self.game_board.get_board()[i][j] is None or  self.game_board.get_board()[i][j].piece_type != piece_type:
                anti_diagonal_match = False
            i += 1
            j -= 1

        return row_match or col_match or diagonal_match or anti_diagonal_match
