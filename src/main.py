import pieces
import board as b


def is_safe(b, piece):
    pos = [piece.i, piece.j]
    piece.attack(b.get_attacked)
    positions = b.get_positions
    if set(positions).intersection(b.get_attacked) > 0:
        return False
    else:
        return True


def remove_piece(b, piece):
    pass


def solution(b, pieces, n):
    if (n == b.get_size):
        return
    if (is_safe):
        solution(b, pieces, n+1)

    pass


def main():
    list_of_pieces = pieces.generate_n_pieces(n)
    n = 8
    board = b.board(n)

    for i in range(n):
        board.set((0, i), list_of_pieces[i])

    board.print()


main()
