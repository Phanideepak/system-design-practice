class ILetter:
    def display(self, row, column):
        pass

class DocumentCharacter(ILetter):
    def __init__(self, character, font_type, size):
        self.__character = character
        self.__font_type = font_type
        self.__size = size
    
    def get_character(self):
        return self.__character
    
    def get_font_type(self):
        return self.__font_type
    
    def get_size(self):
        return self.__size

    def display(self, row, column):
        # Printing character at particular row and column
        pass


letter_cache = {}

class LetterFactory:
    def create_letter(character_value):
        if character_value not in letter_cache:
            character_obj = DocumentCharacter(character_value, 'Arial', 10)
            letter_cache[character_value] = character_obj
        
        return letter_cache[character_value]

letter_object_1 = LetterFactory.create_letter('i')
letter_object_1.display(1, 2)

letter_object_2 = LetterFactory.create_letter('i')
letter_object_2.display(2, 3)
    