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


def solution(b, pieces, n):
    if (n == b.get_size):
        return
    for i in range(b.get_size()):
        piece = pieces[n]
        piece.i = n
        piece.j = i
        if(is_safe(b, piece)):
            # insert_place(b, piece)
            solution(b, pieces, n+1)
            remove_piece(b, piece)
        else:
            remove_piece(b, piece)


def main():
    list_of_pieces = pieces.generate_n_pieces(n)
    n = 8
    board = b.board(n)

    for i in range(n):
        board.set((0, i), list_of_pieces[i])

    board.print()


main()
