# This is the OOP structure for the pieces

from random import randint

class piece:
    def __init__(self):
        self



class bishop(piece):
    def __init__(self, diagonal_conditions):
        self.diagonal_conditions = diagonal_conditions

    def __str__(self):
        return "B"

class rook(piece):
    def __init__(self, horizontal_conditions, vertical_conditions):
        self.horizontal_conditions = horizontal_conditions
        self.vertical_conditions = vertical_conditions

    def __str__(self):
        return "R"


class queen(rook):
    def __init__(self, horizontal_conditions, vertical_conditions, diagonal_conditions):
        super().__init__(horizontal_conditions, vertical_conditions)
        self.diagonal_conditions = diagonal_conditions

    def __str__(self):
        return "Q"

class knight(piece):
    def __init__(self, knight_conditions):
        self.knight_conditions  = knight_conditions

    def __str__(self):
        return "H"

class king(piece):
    def __init__(self, king_conditions):
        self.king_conditions = king_conditions

    def __str__(self):
        return "K"



def generate_n_pieces(n):
    list_of_pieces = []
    dictionary_of_pieces = {
        0:queen(True,True,True),
        1:bishop(True),
        2:rook(True,True),
        3:knight(True),
        4:king(True)
    }
    for i in range(n):
        random_num = randint(0,4)
        list_of_pieces.append(dictionary_of_pieces[random_num])
    
    return list_of_pieces









