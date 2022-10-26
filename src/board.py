
def create_board(n):
    board = []
    b = []

    for i in range(n):
        for j in range(n):
            b.append(0)
        board.append(b.copy())
        b.clear()
    
    return board

def print_board(board):
    for row in board:
        for e in row:
            print(e, end="  ")
        print("")

if __name__ == "__main__":
    board = create_board(8)
    print("\n\n\n")


    board[2][4] = "H"

    print_board(board)