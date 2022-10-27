import pieces
import board as b


def main():
    list_of_pieces = pieces.generate_n_pieces(n)
    n = 8
    board = b.board(n)
    
    for i in range(n):
        board.set((0,i), list_of_pieces[i])

    board.print()

main()