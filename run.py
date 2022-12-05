from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import random
import src.board as board

E = Encoding()

#============== Propositions ==================

#Proposition to hold all squares getting attacked
@proposition(E)
class Attack:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates  # tuple of coordinates

    def __repr__(self):
        return f"Attack({self.coordinates[0]}, {self.coordinates[1]})"

#Proposition to hold all squares that are empty
@proposition(E)
class Empty:
    def __init__(self, empty, coordinates):
        self.empty = empty
        self.coordinates = coordinates

    def __repr__(self):
        return f"Empty({self.coordinates[0]}, {self.coordinates[1]})"

#Proposition to hold all kings
@proposition(E)
class King:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"King({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"King({self.coordinates[0]}, {self.coordinates[1]})"

#Proposition to hold all bishops
@proposition(E)
class Bishop:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Bishop({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Bishop({self.coordinates[0]}, {self.coordinates[1]})"

#Proposition to hold all rooks
@proposition(E)
class Rook:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Rook({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Rook({self.coordinates[0]}, {self.coordinates[1]})"

#Proposition to hold all knights
@proposition(E)
class Knight:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Knight({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Knight({self.coordinates[0]}, {self.coordinates[1]})"

#Proposition to hold all queens
@proposition(E)
class Queen:
    def __init__(self, piece, coordinates):
        self.piece = piece
        self.coordinates = coordinates

    def __repr__(self):
        return f"Queen({self.coordinates[0]}, {self.coordinates[1]})"

    def __call__(self):
        return f"Queen({self.coordinates[0]}, {self.coordinates[1]})"


#============== Theory ====================
def theory(pieces):

    #================= Piece Constraints ==================
    for piece in pieces:

        x = piece.coordinates[0]
        y = piece.coordinates[1]

        #Make all the pieces in pieces true
        E.add_constraint(piece)

        #King attacks
        if piece.piece == "K":
            E.add_constraint(King("K", (x, y)) >> (
                  Attack("A", (x, y + 1)) #down
                & Attack("A", (x, y - 1)) #up
                & Attack("A", (x + 1, y)) #right
                & Attack("A", (x - 1, y)) #left
                & Attack("A", (x + 1, y + 1)) #down right
                & Attack("A", (x + 1, y - 1)) #up right 
                & Attack("A", (x - 1, y + 1)) #down left
                & Attack("A", (x - 1, y - 1)) #up left
            ))

        #Knight attacks
        if piece.piece == "H":
            E.add_constraint(Knight("H", (x, y)) >> (
                  Attack("A", (x + 2, y + 1)) #two right one down
                & Attack("A", (x + 2, y - 1)) #two right one up
                & Attack("A", (x - 2, y + 1)) #two left one down
                & Attack("A", (x - 2, y - 1)) #two left one up
                & Attack("A", (x + 1, y + 2)) #one right two down
                & Attack("A", (x + 1, y - 2)) #one right two up
                & Attack("A", (x - 1, y + 2)) #one left two down
                & Attack("A", (x - 1, y - 2)) #one left two up
            ))

        #Rook attacks
        if piece.piece == "R":
            #Add all the multiples of these four positions to the attacks
            for i in range(1, N):
                E.add_constraint(Rook("R", (x, y)) >> (
                      Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - i)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + i)) #Down
                ))

        #Bishop attacks
        if piece.piece == "B":
            #Add all the multiples of these four positions to the attacks
            for i in range(1, N):
                E.add_constraint(Bishop("B", (x, y)) >> (
                      Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))

        #Queen attacks
        if piece.piece == "Q":
            #Add all the multiples of these four positions to the attacks
            for i in range(1, N):
                #Cardinal directions
                E.add_constraint(Queen("Q", (x, y)) >> (
                      Attack("A", (x + i, y)) #Right
                    & Attack("A", (x, y - i)) #Up
                    & Attack("A", (x - i, y)) #Left
                    & Attack("A", (x, y + i)))) #Down
                #Diagonal directions
                E.add_constraint(Queen("Q", (x, y)) >> (
                    Attack("A", (x + i, y - i)) #Up and right
                    & Attack("A", (x - i, y - i)) #Up and left
                    & Attack("A", (x + i, y + i)) #Down and right
                    & Attack("A", (x - i, y + i)) #Down and left
                ))

    #================= General Constraints ==================

    #Use a new loop for clarity, has the same effect as keeping one loop
    for piece in pieces:
        #If a piece is a king, it is not any other piece
        if piece.piece == "K":
            E.add_constraint(
                piece >>
                  ~Rook("R", (x, y))
                & ~Bishop("B", (x, y))
                & ~Knight("H", (x, y))
                & ~Queen("Q", (x, y))
            )
        #If a piece is a rook, it is not any other piece
        elif piece.piece == "R":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Bishop("B", (x, y))
                & ~Knight("H", (x, y))
                & ~Queen("Q", (x, y))
            )
        #If a piece is a bishop, it is not any other piece
        elif piece.piece == "B":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Knight("H", (x, y))
                & ~Queen("Q", (x, y))
            )
        #If a piece is a knight, it is not any other piece
        elif piece.piece == "H":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Bishop("B", (x, y))
                & ~Queen("Q", (x, y))
            )
        #If a piece is a queen, it is not any other piece
        elif piece.piece == "Q":
            E.add_constraint(
                piece >>
                  ~King("K", (x, y))
                & ~Rook("R", (x, y))
                & ~Bishop("B", (x, y))
                & ~Knight("H", (x, y))
            )    
    
    #Return the finished theory
    return E


def writeSolutionToFile(solution, fileName):
    """
    Writes all the output of solution into a file

    Parameters:
        solution (list): The solution to write to file
        fileName (str): The name of the file to write to
    
    Returns:
        None
    """

    #Open the file
    with open(fileName, 'w') as f:
        #Write the number of solutions
        f.write(str(len(solution.keys())) + "\n")
        #Write each solution
        for line in solution.keys():
            #Optional modifiers
            #if "A" not in str(line) and "E" not in str(line) and "P" not in str(line):
                #if solution[line] == True:
                    f.write(f"{line}  \t {solution[line]} \n")


def makeBoard():
    """
    Makes a board of size N x N

    Parameters:
        None

    Returns:
        board (list): A list of lists representing the board
    """

    #Generate a board of size N x N
    board = [[0 for i in range(N)] for j in range(N)]

    #Iterate through the board and set it to all empty spaces
    for i in range(N):
        for j in range(N):
            board[i][j] = Empty("E", (i, j))

    #Return the board    
    return board


def printBoard(board):
    """
    Prints the board

    Parameters:
        board (list): The board to print
    
    Returns:
        None
    """

    #Iterate through the rows
    for x in range(N):
        #Iterate through the columns
        for y in range(N):
            #Print the piece
            if "Empty" in str(board[x][y]):
                print(" _", end="  ")
            elif "King" in str(board[x][y]):
                print(" K", end="  ")
            elif "Bishop" in str(board[x][y]):
                print(" B", end="  ")
            elif "Rook" in str(board[x][y]):
                print(" R", end="  ")
            elif "Knight" in str(board[x][y]):
                print(" H", end="  ")
            elif "Queen" in str(board[x][y]):
                print(" Q", end="  ")
            elif "Attack" in str(board[x][y]):
                print(" X", end="  ")
        print(" ")

def listToBauhaus(lis):
    """
    Converts a list of lists to a list usable by the bauhaus solver

    Parameters:
        lis (list): The list to convert
    
    Returns:
        bauhaus (list): The converted list
    """

    #Create a new list
    bauhaus = []

    #Iterate through the list
    for y, row in enumerate(lis):
        #Iterate through the row
        for x, elem in enumerate(row):
            #Convert the element to a proposition and add it to the list
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
    #Return the new list
    return bauhaus

def determineValidity(solutions, pieces):
    """
    Determines if the solutions given by the theory are valid

    Parameters:
        solutions (list): The solutions to check
        pieces (list): The pieces to check

    Returns:
        valid (bool): Whether the solutions are valid or not
    """

    #Loop through all the items in solutions
    for p in solutions:
        #If the item is an attack
        if p.piece == "A":
            #Loop through all the pieces
            for piece in pieces:
                #If the piece is on the same square as the attack
                if p.coordinates == piece.coordinates:
                    #Return false
                    return False
    #Otherwise, return true
    return True

def filterUseful(solution):
    """
    Filters out the useful items from the returned solution. Used for debugging

    Parameters:
        solution (list): The solution to filter

    Returns:
        filtered (list): The filtered solution
    """

    #Create a list to store the filtered items
    validCoords = []
    #Loop through all the items in the solution
    for line in solution.keys():
        #If the item is true
        if solution[line] == True:
            #If the item is in range
            if line.coordinates[0] < N and line.coordinates[1] < N and line.coordinates[0] >= 0 and line.coordinates[1] >= 0:
                #Append the item to the list
                validCoords.append(line)
    #Return the filtered list
    return validCoords

def setBoard(listOfPropositions, board):
    """
    Sets the board to the given propositions

    Parameters:
        listOfPropositions (list): The propositions to set the board to
        board (list): The board to set
    
    Returns:
        None
    """

    for proposition in listOfPropositions:
        board[proposition.coordinates[1]][proposition.coordinates[0]] = proposition

def test1():
    """
    Tests the theory with the first test case

    Parameters:
        None

    Returns:
        None
    """

    #Create a board
    lis = [
        ["_", "H", "_", "_"],
        ["_", "_", "_", "_"],
        ["K", "Q", "_", "_"],
        ["_", "_", "_", "B"],
    ]

    #Print the board
    for row in lis:
        print(row)

    #Return the converted board
    return listToBauhaus(lis)

def test2():
    """
    Tests the theory with the second test case

    Parameters:
        None

    Returns:
        None
    """

    #Create a board
    lis = [
        ["_", "_", "_", "_"],
        ["_", "_", "R", "_"],
        ["_", "R", "_", "_"],
        ["H", "_", "_", "B"],
    ]

    #Print the board
    for row in lis:
        print(row)

    #Return the converted board
    return listToBauhaus(lis)

def test3():
    """
    Tests the theory with the third test case

    Parameters:
        None

    Returns:
        None
    """

    #Create a board
    lis = [
        ["_", "R", "_"],
        ["K", "_", "_"],
        ["_", "Q", "_"],
    ]

    #Print the board
    for row in lis:
        print(row)

    #Return the converted board
    return listToBauhaus(lis)

def test4():
    """
    Tests the theory with the fourth test case

    Parameters:
        None

    Returns:
        None
    """

    #Create a board
    lis = [
        ["B", "_", "_"],
        ["_", "_", "R"],
        ["_", "R", "_"],
    ]

    #Print the board
    for row in lis:
        print(row)

    #Return the converted board
    return listToBauhaus(lis)

if __name__ == "__main__":

    print("\n\nIs this board a solution?\n")

    #Mapping of test to size is as follows:
    #1 - 4
    #2 - 4
    #3 - 3
    #4 - 3

    #Change this to test different boards (1 - 4)
    pieces = test1()

    #Board size
    N = 4

    #Print the pieces being used
    print(pieces)
    print()

    #Instantiate the theory 
    T = theory(pieces) 
    print(u'\u2713' + " ---> Theory Created")
    
    #Compile the theory
    T = T.compile()
    print(u'\u2713' + " ---> Theory Compiled")
    
    #Solve the theory and check if it is satisfiable
    solution = T.solve() 
    print(u'\u2713' + " ---> Theory Solution Found")
    print(u'\u2713' + " ---> Theory Satisfiable: %s" % T.satisfiable())

    #Write the solution to the file. Used for debugging
    # writeSolutionToFile(solution, "Total_Solutions.txt")
    # print(u'\u2713' + " ---> Solution Written to File")
    
    #Determine if the solution is valid and print it
    result = determineValidity(solution, pieces)
    print(u'\u2713' + " ---> Is Solution Valid: %s" % result)

    #If the solution is valid print accordingly
    if result:
        print("\nThis is a valid solution!\n")
    else:
        print("\nThis is not a valid solution.\n")