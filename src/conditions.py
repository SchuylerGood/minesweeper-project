import pieces 
import board 

def horizontal_conditions(n, board, coordinates):
    for i in range(n):
        if board[coordinates[1]][i] == "X":
            print("X on this spot") 

def vertical_conditions(n, board, coordinates):
    for i in range(n):
        if board[i][coordinates[1]] == "X":
            print("X on this spot") 

def diagonal_conditions(n, board, coordinates):
    for i in range(n):
        for j in range(n):
            # if board[]
            print("goofy ahh")

def checkConditions(n, piece):
    """
    Parameters: n - is the size of the board
                piece - should be of type piece
                coordinates - a tuple of the current placing of the piece
    """
    if type(piece) == pieces.queen:
        coordinates_list = []

        horizontal_conditions = 1
        vertical_conditions = 1
        diagonal_conditions = 1



    elif type(piece) == pieces.bishop:
        diagonal_conditions = 1

    elif type(piece) == pieces.rook:
        horizontal_conditions = 1
        vertical_conditions = 1
    
    elif type(piece) == pieces.knight:
        knight_conditions = 1
    
    elif type(piece) == pieces.king:
        king_conditions = 1
