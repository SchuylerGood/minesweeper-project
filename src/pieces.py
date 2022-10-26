# This is the OOP structure for the pieces


class piece:
    def __init__(self, name):
        self.name = name

class queen(piece):
    def __init__(self, horizontal_conditions, vertical_conditions, diagonal_conditions, *args, **kwargs):
        super(queen, self).__init__(*args, **kwargs)
        self.horizontal_conditions = horizontal_conditions
        self.vertical_conditions = vertical_conditions
        self.diagonal_conditions = diagonal_conditions

class bishop(queen):
    def __init__(self, *args, **kwargs):
        super(bishop, self).__init__(*args, **kwargs)


class rook(queen):
    def __init__(self, *args, **kwargs):
        super(rook, self).__init__(*args, **kwargs)

class knight(piece):
    def __init__(self, knight_conditions):
        self.knight_conditions  = knight_conditions

class king(piece):
    def __init__(self, king_conditions):
        self.king_conditions = king_conditions










