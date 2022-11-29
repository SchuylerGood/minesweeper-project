import pieces
import board as b

# I want this function to be just pass by value it should not modify the original attackList


def is_safe(b, piece):
    pos = [piece.i, piece.j]
    piece.attack(b.get_attacked)
    positions = b.get_positions
    positions.append(pos)
    if set(positions).intersection(b.get_attacked) > 0:
        return False
    else:
        return True
# I want this function to be pass by referance

def insert_place(b, piece):
    pos = [piece.i, piece.j]
    piece.attack(b.get_attacked)
    positions = b.get_positions
    positions.append(pos)

# I want this function to be pass by referance


def remove_piece(b, piece):
    pos = [piece.i, piece.j]
    piece.de_attack(b.get_attacked)
    positions = b.get_positions
    positions.remove(pos)


# Explaination for this function as it is the most important function in the whole implementation
def solution(b, pieces, n, solution):
    if (n == b.get_size):  # this is base case at this position we will have the solution
        # appending the solution as we have multiple solution and we find them all
        solution.append(b.get_position())
        return
    for i in range(b.get_size()):
        # get the piece at the nth location to be places in the nth row
        piece = pieces[n]
        piece.i = n  # assigning the row number to i
        piece.j = i  # assigning th column number to j
        if(is_safe(b, piece)):  # this function will check if placement of the piece is safe of not and will also place the piece
            # insert_place(b, piece)
            # then we call the recursion function for next row,
            solution(b, pieces, n+1)
            # while returning it will remove the piece from the board
            remove_piece(b, piece)
        else:
            # as is safe places the pices along with checking of the placment safety hence have to remove the piece if it not not a safe position
            remove_piece(b, piece)


def main():
    pass
main()
