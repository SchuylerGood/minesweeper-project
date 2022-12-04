from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import random
import src.board as board

N = 5

E = Encoding()

#============== Propositions ==================
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

#===============================================






#============== Theory ====================
def theory(pieces):

    #================= Piece Constraints ==================

    for piece in pieces:

        x = piece.coordinates[0]
        y = piece.coordinates[1]

        #Make all the pieces in pieces true
        E.add_constraint(piece)

        #King constraints
        if piece.piece == "K":
            E.add_constraint(King("K", (x, y)) >> (
                Attack("A", (x, y + 1))
                & Attack("A", (x, y - 1))
                & Attack("A", (x + 1, y))
                & Attack("A", (x - 1, y))
                & Attack("A", (x + 1, y + 1))
                & Attack("A", (x + 1, y - 1))
                & Attack("A", (x - 1, y + 1))
                & Attack("A", (x - 1, y - 1))
            ))

        #Knight constraints
        if piece.piece == "H":
            E.add_constraint(Knight("H", (x, y)) >> (
                Attack("A", (x + 2, y + 1))
                & Attack("A", (x + 2, y - 1))
                & Attack("A", (x - 2, y + 1))
                & Attack("A", (x - 2, y - 1))
                & Attack("A", (x + 1, y + 2))
                & Attack("A", (x + 1, y - 2))
                & Attack("A", (x - 1, y + 2))
                & Attack("A", (x - 1, y - 2))
            ))

        #Rook constraints
        if piece.piece == "R":
            for i in range(1, N):
                E.add_constraint(Rook("R", (x, y)) >> (
                    Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - i)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + i)) #Down
                ))

        #Bishop constraints
        if piece.piece == "B":
            for i in range(1, N):
                E.add_constraint(Bishop("B", (x, y)) >> (
                    Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))

            #Queen constraints
        if piece.piece == "Q":
            for i in range(1, N):
                E.add_constraint(Queen("Q", (x, y)) >> (
                    Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - i)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + i)))) #Down
                E.add_constraint(Queen("Q", (x, y)) >> (
                    Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))

    #================= General Constraints ==================

    for piece in pieces:
        if piece.piece == "K":
            E.add_constraint(
                piece >>
                  ~Rook("R", (x, y))
                & ~Bishop("B", (x, y))
                & ~Knight("H", (x, y))
                & ~Queen("Q", (x, y))
            )  
        elif piece.piece == "R":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Bishop("B", (x, y))
                & ~Knight("H", (x, y))
                & ~Queen("Q", (x, y))
            )
        elif piece.piece == "B":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Knight("H", (x, y))
                & ~Queen("Q", (x, y))
            )
        elif piece.piece == "H":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Bishop("B", (x, y))
                & ~Queen("Q", (x, y))
            )
        elif piece.piece == "Q":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Bishop("B", (x, y))
                & ~Knight("H", (x, y))
            )    
    
    return E


def writeSolutionToFile(solution, fileName):
    with open(fileName, 'w') as f:
        f.write(str(len(solution.keys())) + "\n")
        for line in solution.keys():
            #if "A" not in str(line) and "E" not in str(line) and "P" not in str(line):
                #if solution[line] == True:
                    f.write(f"{line}  \t {solution[line]} \n")


def makeBoard():
    board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = Empty("E", (i, j))
    return board


def printBoard(board):
    for i in range(N):
        for j in range(N):
            if "Empty" in str(board[i][j]):
                print(" _", end="  ")
            elif "King" in str(board[i][j]):
                print(" K", end="  ")
            elif "Bishop" in str(board[i][j]):
                print(" B", end="  ")
            elif "Rook" in str(board[i][j]):
                print(" R", end="  ")
            elif "Knight" in str(board[i][j]):
                print(" H", end="  ")
            elif "Queen" in str(board[i][j]):
                print(" Q", end="  ")
            elif "Attack" in str(board[i][j]):
                print(" X", end="  ")
        print(" ")

def listToBauhaus(lis):
    bauhaus = []
    for y, row in enumerate(lis):
        for x, elem in enumerate(row):
            if elem == "K":
                bauhaus.append(King("K", (x, y)))
            elif elem == "B":
                bauhaus.append(Bishop("B", (x, y)))
            elif elem == "R":
                bauhaus.append(Rook("R", (x, y)))
            elif elem == "H":
                bauhaus.append(Knight("H", (x, y)))
            elif elem == "Q":
                bauhaus.append(Queen("Q", (x, y)))
    return bauhaus

def determineValidity(solutions, pieces):
    for p in solutions:
        if p.piece == "A":
            for piece in pieces:
                if p.coordinates == piece.coordinates:
                    return False
    return True

def filterUsefull(solution):
    validCoords = []
    for line in solution.keys():
        if solution[line] == True:
            if line.coordinates[0] < N and line.coordinates[1] < N and line.coordinates[0] >= 0 and line.coordinates[1] >= 0:
                validCoords.append(line)
    return validCoords

def setBoard(listOfPropositions, board):
    for proposition in listOfPropositions:
        board[proposition.coordinates[1]][proposition.coordinates[0]] = proposition

def test1():
    lis = [
        ["_", "H", "_", "_"],
        ["_", "_", "_", "_"],
        ["K", "Q", "_", "_"],
        ["_", "_", "_", "B"],
    ]

    for row in lis:
        print(row)

    return listToBauhaus(lis)

def test2():
    lis = [
        ["_", "_", "_", "_"],
        ["_", "_", "R", "_"],
        ["_", "R", "_", "_"],
        ["H", "_", "_", "B"],
    ]

    for row in lis:
        print(row)

    return listToBauhaus(lis)

def test3():
    lis = [
        ["_", "R", "_"],
        ["K", "_", "_"],
        ["_", "Q", "_"],
    ]

    for row in lis:
        print(row)

    return listToBauhaus(lis)

def test4():
    lis = [
        ["B", "_", "_"],
        ["_", "_", "R"],
        ["_", "R", "_"],
    ]

    for row in lis:
        print(row)

    return listToBauhaus(lis)

if __name__ == "__main__":

    print("\n\nIs this board a solution?\n")

    #Change this to test different boards (1 - 4)
    pieces = test1()

    print(pieces)
    print()

    T = theory(pieces) # Instantiates the theory 
    print(u'\u2713' + " ---> Theory Created")
    
    T = T.compile() # Compiles the theory
    print(u'\u2713' + " ---> Theory Compiled")
    
    solution = T.solve() # Solves the theory
    print(u'\u2713' + " ---> Theory Solution Found")
    print(u'\u2713' + " ---> Theory Satisfiable: %s" % T.satisfiable())

    writeSolutionToFile(solution, "Total_Solutions.txt") # Writes full list of bauhaus solutions to a file
    print(u'\u2713' + " ---> Solution Written to File")
    
    result = determineValidity(solution, pieces)
    print(u'\u2713' + " ---> Is Solution Valid: %s" % result)

    if result:
        print("This is a valid solution!\n\n")
    else:
        print("This is not a valid solution.\n\n")