class board():

    def __init__(self, size = 8):
        """
        Initializes the board, also creates the rows and columns automatically.\n
        Parameters:\n
            size: int - the width and height of the board (note, the board is always of form n x n)\n
        Returns:\n
            None\n
        Raises:\n
            ValueError: If size is less than 0.
        """

        if (size < 0):
            raise ValueError("size must be greater than or equal to 0")

        self.size = size
        self.b = []

        self.b = self.create_board(self.size)
    
    def print(self):
        """
        Prints the board as if it were on a table in front of you.\n
        Parameters:\n
            None\n
        Returns:\n
            None\n
        Raises:\n
            None\n
        """
        for row in self.b:
            for e in row:
                print(e, end="  ")
            print("")
    
    def create_board(self, n = 8):
        """
        Creates a board of size n. This function is automatically called on initialization.\n
        Parameters:\n
            n: int - the width and height of the board (note, the board is always of form n x n)\n
        Returns:\n
            b: Board - finished board. The values are all defaulted to 0. The board is stored as a 2D array.\n
        Raises:\n
            ValueError: if n is less than 0\n
        """

        if (n < 0):
            raise ValueError("n must be greater than or equal to 0")

        final = []
        r = []
        for i in range(n):
            for j in range(n):
                r.append(0)
            final.append(r.copy())
            r.clear()
        
        return final

    def set(self, pos = (0, 0), item = 0):
        """
        Sets a value on the board.\n
        Parameters:\n
            item: String - Item to place at pos.\n
            pos: 2D Tuple - The point to place the item at.\n
        Returns:\n
            None\n
        Raises:\n
            ValueError: if pos is not of length 2 or the values are out of bounds.\n
        """

        if (len(pos) != 2):
            raise ValueError("pos must be of length 2")
        
        if (pos[0] < 0 or pos[0] > self.size - 1 or pos[1] < 0 or pos[1] > self.size - 1):
            raise ValueError("pos must not contain values less than zero or larger than board size.")

        self.b[pos[0]][pos[1]] = item
    
    def get(self, pos = (0, 0)):
        """
        Gets a value on the board.\n
        Parameters:\n
            None\n
        Returns:\n
            item: String - String representation of the item at pos.\n
        Raises:\n
            ValueError: if pos is not of length 2 or the values are out of bounds.\n
        """

        if (len(pos) != 2):
            raise ValueError("pos must be of length 2")
        
        if (pos[0] < 0 or pos[0] > self.size - 1 or pos[1] < 0 or pos[1] > self.size - 1):
            raise ValueError("pos must not contain values less than zero or larger than board size.")

        return self.b[pos[0]][pos[1]]

if __name__ == "__main__":
    b = board(8)
    print("\n\n\n")

    b.set((3, 4), "H")
    b.print()

    print(b.get((3, 4)))