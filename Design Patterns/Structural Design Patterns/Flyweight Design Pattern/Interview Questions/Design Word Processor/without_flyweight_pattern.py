class Character:

    def __init__(self, character, font_type, size, row, col):
        self.character = character
        self.font_type = font_type
        self.size = size
        self.row = row 
        self.col = col


# Client Code 
ch1 = Character('a', 'Arial', 10, 0, 0)
ch2 = Character('a', 'Arial', 10, 0, 1)
ch3 = Character('b', 'Arial', 10, 1, 2)