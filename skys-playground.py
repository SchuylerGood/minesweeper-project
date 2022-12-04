from bauhaus import Encoding, proposition, constraint, print_theory
from bauhaus.utils import count_solutions, likelihood

E = Encoding()

# =================================
# =====     GLOBAL VARS      ======
# =================================
N = 4

# =================================
# =====   ALL PROPOSITIONS   ======
# =================================


@proposition(E)
class Attack:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates  # tuple of coordinates

    def __repr__(self):
        return f"Attack({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Empty:
    def __init__(self, empty, coordinates):
        self.empty = empty
        self.coordinates = coordinates

    def __repr__(self):
        return f"Empty({self.coordinates[0]}, {self.coordinates[1]})"

@proposition(E)
class Piece:
    def __init__(self, empty, coordinates):
        self.empty = empty
        self.coordinates = coordinates

    def __repr__(self):
        return f"Piece({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class King:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"King({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"King({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Bishop:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Bishop({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Bishop({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Rook:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Rook({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Rook({self.coordinates[0]}, {self.coordinates[1]})"


@proposition(E)
class Knight:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Knight({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Knight({self.coordinates[0]}, {self.coordinates[1]})"

@proposition(E)
class Queen:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Queen({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Queen({self.coordinates[0]}, {self.coordinates[1]})"


# =================================
# ====  PROPOSITION INSTANCES  ====
# =================================
attack = Attack("A", (0, 0))
empty = Empty("E", (0, 0))
k1 = King("K", (0, 0))
b1 = Bishop("B", (0, 0))
r1 = Rook("R", (0, 0))
n1 = Knight("N", (0, 0))
q1 = Queen("Q", (0, 0))


def makeBoard():
    board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = Empty("E", (i, j))
    return board


def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="  ")
        print(" ")
# =================================
# =====        THEORY        ======
# =================================


def theory1():
    # King Constraints
    for x in range(N):
        for y in range(N):
            E.add_constraint(King("K", (x, y)) >> (
                  Attack("A",   (x, y + 1))
                & Attack("A", (x, y - 1))
                & Attack("A", (x + 1, y))
                & Attack("A", (x - 1, y))
                & Attack("A", (x + 1, y + 1))
                & Attack("A", (x + 1, y - 1))
                & Attack("A", (x - 1, y + 1))
                & Attack("A", (x - 1, y - 1))
            ))


    # Knight Constraints
    for x in range(N):
        for y in range(N):
            E.add_constraint(Knight("K", (x, y)) >> (
                  Attack("A", (x + 2, y + 1))
                & Attack("A", (x + 2, y - 1))
                & Attack("A", (x - 2, y + 1))
                & Attack("A", (x - 2, y - 1))
                & Attack("A", (x + 1, y + 2))
                & Attack("A", (x + 1, y - 2))
                & Attack("A", (x - 1, y + 2))
                & Attack("A", (x - 1, y - 2))
            ))

            
    # Rook Constraints
    for x in range(N):
        for y in range(N):
            for i in range(1, N):
                E.add_constraint(Rook("R", (x, y)) >> (
                      Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - 1)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + 1)) #Down
                ))


    # Bishop Constaints
    for x in range(N):
        for y in range(N):
            for i in range(1, N):
                E.add_constraint(Bishop("B", (x, y)) >> (
                      Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))


    # Queen Constraints
    for x in range(N):
        for y in range(N):
            for i in range(1, N):
                #Cardinal directions
                E.add_constraint(Queen("Q", (x, y)) >> (
                      Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - 1)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + 1)) #Down
                ))
                #Diagonals
                E.add_constraint(Queen("Q", (x, y)) >> (
                      Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))

    # General/Board Constraints 
    for x in range(N):
        for y in range(N):
            # At any coordinate (i,j) it can either be Empty, Attack, King, Bishop, Rook, Knight, or Queen
            E.add_constraint(
                  Empty("_", (x, y)) 
                | Attack("A", (x, y)) 
                | King("K", (x, y)) 
                | Bishop("B", (x, y)) 
                | Rook("R", (x, y)) 
                | Knight("N", (x, y)) 
                | Queen("Q", (x, y))
            )

            # The following constraints allows only one piece (either K, B, R, Q) at one positon (x,y)
            E.add_constraint(
                  King("K", (x, y)) >>
                  ~Bishop("B", (x, y))
                & ~Rook("R", (x, y)) 
                & ~Knight("N", (x, y)) 
                & ~Queen("Q", (x, y))
            )

            E.add_constraint(
                  Bishop("B", (x, y)) >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Knight("N", (x, y))
                & ~Queen("Q", (x, y))
            )

            E.add_constraint(
                  Rook("R", (x, y)) >>
                  ~Bishop("B", (x, y))
                & ~King("K", (x, y))
                & ~Knight("N", (x, y)) 
                & ~Queen("Q", (x, y))
            )

            E.add_constraint(
                  ~King("K", (x, y)) >>
                  ~Bishop("B", (x, y))
                & ~Rook("R", (x, y))
                & Knight("N", (x, y))
                & ~Queen("Q", (x, y))
            )
            
            E.add_constraint(
                  Queen("Q", (x, y)) >>
                  ~King("K", (x, y))
                & ~Bishop("B", (x, y))
                & ~Rook("R", (x, y))
                & ~Knight("N", (x, y))
            )

            # This constraint says that if we have King(i,j), Bishop(i,j), Queens(i,j) or 
            # Rook(i,j) at implies Piece(i,j)
            E.add_constraint(
                King("K", (x, y))
                | Bishop("B", (x, y))
                | Rook("R", (x, y))
                | Knight("N", (x, y))
                | Queen("Q", (x, y)) >> 
                  Piece("P", (x, y))
            )

            # If we place a piece on the board how do we confirm that the Empty is converted to the piece or the attack?
            # because intially if Empty and then placed a piece then both empty and piece will be true and our constraint
            # of having only one state will spit false and ultimately we will get false as soon as we place the 1 Piece be it any?

            # possible solution for above problem
            E.add_constraint(
                Empty("_", (x, y)) & Attack("A", (x, y)) >> ~Empty("_", (x, y))
            )
            
            E.add_constraint(
                Empty("_", (x, y)) & Piece("A", (x, y)) >> ~Empty("_", (x, y))
            )

            E.add_constraint(
                Piece("A", (x, y)) >> ~Empty("_", (x, y))
            )

            E.add_constraint(
                Empty("_", (x, y)) >> ~Piece("A", (x, y))
            )

            # E.add_constraint(
            #       Piece("P", (x, y)) >> 
            #       ~Attack("A", (x, y))
            #     & ~Empty("_", (x, y))
            # )
            
            # E.add_constraint(
            #       ~Piece("P", (x, y))
            #     & Attack("A", (x, y))
            #     & ~Empty("_", (x, y))
            # )
            
            # E.add_constraint(
            #     Empty("_", (x, y)) >>
            #       ~Piece("P", (x, y))
            #     & ~Attack("A", (x, y))
            # )

    return E


# =================================
# =====        MAIN          ======
# =================================
if __name__ == "__main__":
    T = theory1()
    print("1. Theory Created")

    T = T.compile()
    print("2. Theory Compiled")

    solution = T.solve()
    print("3. Theory Solution Found")
    print("\n4. Satisfiable: %s" % T.satisfiable())
    # print("# Solutions: %d" % count_solutions(T))

    # board = makeBoard()
    # printBoard(board)

    # print_theory(solution, "truth")
    


    # list_of_cords = []

    for i in solution.keys():

        print(i, solution[i])
    print(len(solution.keys()))

    # output all of the solutions to a text file
    # with open("output.txt", "w") as f:
    #     for i in solution.keys():
    #         f.write(str(i) + " " + str(solution[i]) + "\n")

    with open('your_file.txt', 'w') as f:
        for line in solution.keys():
            f.write(f"{line}\n")



    # set_of_cords = set(list_of_cords)

    # for i in range(len(list_of_cords)):

    #     if list_of_cords[i][1]:
    #         print(list_of_cords)

    # print(len(list_of_cords))
    # print(solution[Attack(0, 1)])
    # print("   Solution: %s" % T.solve())


    # print("\nVariable likelihoods:")    
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
    #     # Ensure that you only send these functions NNF formulas
    #     # Literals are compiled to NNF here
    #     print(" %s: %.2f" % (vn, likelihood(T, v)))



