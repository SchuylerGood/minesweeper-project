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
class Rooke:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Rooke({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Rooke({self.coordinates[0]}, {self.coordinates[1]})"


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
r1 = Rooke("R", (0, 0))
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
    # This checkes for initial states
    for i in range(N):
        for j in range(N):
           # King Constraints
            E.add_constraint(King("K", (i, j)) >>
                             (
                Attack("A", (i, j+1))
                | Attack("A", (i, j-1))
                | Attack("A", (i+1, j))
                | Attack("A", (i-1, j))
                | Attack("A", (i+1, j+1))
                | Attack("A", (i+1, j-1))
                | Attack("A", (i-1, j+1))
                | Attack("A", (i-1, j-1))
            ))

    for i in range(N):
        for j in range(N):
            # Knight Constraints
            E.add_constraint(Knight("K", (i, j)) >>
                             (
                Attack("A", (i+2, j+1))
                | Attack("A", (i+2, j-1))
                | Attack("A", (i-2, j+1))
                | Attack("A", (i-2, j-1))
                | Attack("A", (i+1, j+2))
                | Attack("A", (i+1, j-2))
                | Attack("A", (i-1, j+2))
                | Attack("A", (i-1, j-2))
            )
            )
            # Rooke Constraints
    for x in range(N):
        for y in range(N):
            l = x
            k = y
            for i in range(1, N):
                E.add_constraint(Rooke("R", (k, l))) >> (
                    Attack("A", (k, i))
                    | Attack("A", (i, l))
                    | Attack("A", (k, -i))
                    | Attack("A", (-i, l))
                )

            # Bishop Constaints
    for x in range(N):
        for y in range(N):
            # digonal towards down and right
            if k != N-1 and l != N-1:
                k = x+1
                l = y+1
            while(k <= (N-1) and l <= 3):
                E.add_constraint(Bishop("B", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k += 1
                l += 1
            # digonal towards down and left
            if k != N-1 and l != 0:
                k += 1
                l -= 1
            while (k <= 3 and l >= 0):
                E.add_constraint(Bishop("B", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k += 1
                l -= 1

            # digonal towards up and right
            if k != 0 and l != N-1:
                k += 1
                l -= 1
            while (k >= 0 and l <= 3):
                E.add_constraint(Bishop("B", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k -= 1
                l += 1

            # digonal towards up and left
            if k != 0 and l != 0:
                k -= 1
                l -= 1
            while (k >= 0 and l >= 0):
                E.add_constraint(Bishop("B", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k -= 1
                l -= 1

    # Queen Constraints
    for x in range(N):
        for y in range(N):
            # digonal towards down and right
            if k != N-1 and l != N-1:
                k = x+1
                l = y+1
            while(k <= (N-1) and l <= 3):
                E.add_constraint(Queen("Q", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k += 1
                l += 1
            # digonal towards down and left
            if k != N-1 and l != 0:
                k += 1
                l -= 1
            while (k <= 3 and l >= 0):
                E.add_constraint(Queen("Q", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k += 1
                l -= 1

            # digonal towards up and right
            if k != 0 and l != N-1:
                k += 1
                l -= 1
            while (k >= 0 and l <= 3):
                E.add_constraint(Queen("Q", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k -= 1
                l += 1

            # digonal towards up and left
            if k != 0 and l != 0:
                k -= 1
                l -= 1
            while (k >= 0 and l >= 0):
                E.add_constraint(Queen("Q", (k, l))) >> (
                    Attack("A", (k, l))
                )
                k -= 1
                l -= 1
            l = x
            k = y
            for i in range(1, N):
                E.add_constraint(Queen("Q", (k, l))) >> (
                    Attack("A", (k, i))
                    | Attack("A", (i, l))
                    | Attack("A", (k, -i))
                    | Attack("A", (-i, l))
                )
    for i in range(N):
        for j in range(N):
            # I do not understand this constraint Please specify what does this constraint do
            E.add_constraint(Empty("_", (i, j)) | Attack("A", (i, j)) | King("K", (i, j)) | Bishop(
                "B", (i, j)) | Rooke("R", (i, j)) | Knight("N", (i, j)) | Queen("Q", (i, j)))

            # This constraint says that if we have King(i,j), Bishop(i,j), Queens(i,j) or Rooke(i,j) at implies to  Piece(i,j)
            E.add_constraint(King("K", (i, j)) | Bishop("B", (i, j)) | Rooke(
                "R", (i, j)) | Knight("N", (i, j)) | Queen("Q", (i, j)) >> Piece("P", (i, j)))

            # If we place a piece on the board how do we confirm that the Empty is converted to the piece or the attack?
            # because intially if Empty and then placed a piece then both empty and piece will be true and our constraint
            # of having only one state will spit false and ultimately we will get false as soon as we place the 1 Piece be it any?

            # possible solution for above problem
            E.add_constraint(Empty("_", (i, j)) & Attack(
                "A", (i, j)) >> ~Empty("_", (i, j)) & Attack("A", (i, j)))
            E.add_constraint(Empty("_", (i, j)) & Piece(
                "A", (i, j)) >> ~Empty("_", (i, j)) & Piece("A", (i, j)))

            # This is constraint says that at any position only one state of square is true that is is can be either (P, A, E) ( I used XOR to say it)
            E.add_constraint(Piece("P", (i, j)) & ~Attack("A", (i, j)) & ~Empty("_", (i, j)) | ~Piece("P", (i, j)) & Attack(
                "A", (i, j)) & ~Empty("_", (i, j)) | ~Piece("P", (i, j)) & ~Attack("A", (i, j)) & Empty("_", (i, j)))

            # The following constraints checks only one piece (either K, B, R, Q) be at one positon (i,j)
            E.add_constraint(King("K", (i, j)) & ~Bishop("B", (i, j)) & ~Rooke(
                "R", (i, j)) & ~Knight("N", (i, j)) & ~Queen("Q", (i, j)))
            E.add_constraint(~King("K", (i, j)) & Bishop("B", (i, j)) & ~Rooke(
                "R", (i, j)) & ~Knight("N", (i, j)) & ~Queen("Q", (i, j)))
            E.add_constraint(~King("K", (i, j)) & ~Bishop("B", (i, j)) & Rooke(
                "R", (i, j)) & ~Knight("N", (i, j)) & ~Queen("Q", (i, j)))
            E.add_constraint(~King("K", (i, j)) & ~Bishop("B", (i, j)) & ~Rooke(
                "R", (i, j)) & Knight("N", (i, j)) & ~Queen("Q", (i, j)))
            E.add_constraint(~King("K", (i, j)) & ~Bishop("B", (i, j)) & ~Rooke(
                "R", (i, j)) & ~Knight("N", (i, j)) & Queen("Q", (i, j)))

    constraint.implies_all(E)
    return E


# =================================
# =====        MAIN          ======
# =================================
if __name__ == "__main__":
    T = theory1()
    T = T.compile()

    board = makeBoard()
    printBoard(board)

    print("\nSatisfiable: %s" % T.satisfiable())
    # print("# Solutions: %d" % count_solutions(T))
    solution = T.solve()
    print(len(solution.keys()))
    print_theory(solution, "truth")
    for i in solution.keys():
        if solution[i] == True:
            print(i.coordinates)
    # print(solution[Attack(0, 1)])
    # print("   Solution: %s" % T.solve())
    # print("\nVariable likelihoods:")
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
    #     # Ensure that you only send these functions NNF formulas
    #     # Literals are compiled to NNF here
    #     print(" %s: %.2f" % (vn, likelihood(T, v)))
