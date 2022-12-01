from bauhaus import Encoding, proposition, constraint
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
    for i in range(N):
        for j in range(N):

            E.add_constraint(Empty("_", (i, j)) | Attack("A", (i, j)) | King("K", (i, j)) | Bishop(
                "B", (i, j)) | Rooke("R", (i, j)) | Knight("N", (i, j)) | Queen("Q", (i, j)))
            # E.add_constraint(Empty("_", (i, j)) >> ~Attack("A", (i, j)))
            # E.add_constraint(Empty("_", (i, j)) >> ~King("K", (i, j)))
            # E.add_constraint(Empty("_", (i, j)) >> ~Bishop("B", (i, j)))
            # E.add_constraint(Empty("_", (i, j)) >> ~Rooke("R", (i, j)))
            # E.add_constraint(Empty("_", (i, j)) >> ~Knight("N", (i, j)))
            # E.add_constraint(Empty("_", (i, j)) >> ~Queen("Q", (i, j)))

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
                    for i in range(N):
                        E.add_constraint(Rooke("R", (k, l))) >> (
                            Attack("A", (k, i))
                            | Attack("A", (i, l))
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
                    if x == y and (x != i and y != j):
                        E.add_constraint(Queen("Q", (i, j)) >>
                                         (
                            Attack("A", (i, j))
                        )
                        )
            for x in range(N):
                for y in range(N):
                    if x == i and y != j:
                        E.add_constraint(Queen("Q", (i, j)) >>
                                         (
                            Attack("A", (i, y))
                        )
                        )
            for x in range(N):
                for y in range(N):
                    if y == j and x != i:
                        E.add_constraint(Queen("Q", (i, j)) >>
                                         (
                            Attack("A", (x, j))
                        )
                        )

    # E.add_constraint(Empty("_", (0, 0)) | Attack("A", (0, 0)) | King("K", (0, 0)) | Bishop("B", (0, 0)) | Rooke("R", (0, 0)) | Knight("N", (0, 0)) | Queen("Q", (0, 0)))

    # E.add_constraint(k1 >> q1)
    # E.add_constraint(y >> z)
    # Negate a formula
    # E.add_constraint((x & y).negate())
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
    for i in solution.keys():
        print(str(i) + "------" + str(solution[i]))

    # print("   Solution: %s" % T.solve())
    # print("\nVariable likelihoods:")
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
    #     # Ensure that you only send these functions NNF formulas
    #     # Literals are compiled to NNF here
    #     print(" %s: %.2f" % (vn, likelihood(T, v)))
