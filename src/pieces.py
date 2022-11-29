# This is the OOP structure for the pieces

from random import randint


class piece:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def attack(self, attackList):
        pass

    def de_attack(self, attackList):
        pass


class bishop(piece):
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return "B"

    def attack(self, attackList):
        """
        Calculates the attack positions given the current position of the bishop\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
            n: int - size of the board\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0 
        """
        # Diagonal attacking spaces
        k = self.i + 1
        l = self.j + 1
        while (k <= 3 and l <= 3):
            attackList.append([k, l])
            k += 1
            l += 1
        k = self.i+1
        l = self.j-1
        while (k <= 3 and l >= 0):
            attackList.append([k, l])
            k += 1
            l -= 1
        k = self.i - 1
        l = self.j + 1
        while (k >= 0 and l <= 3):
            attackList.append([k, l])
            k -= 1
            l += 1
        k = self.i - 1
        l = self.j - 1
        while (k >= 0 and l >= 0):
            attackList.append([k, l])
            k -= 1
            l -= 1

    def de_attack(self, attackList):
        """
        Calculates the attack positions given the current position of the bishop\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
            n: int - size of the board\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0 
        """
        # Diagonal attacking spaces
        k = self.i + 1
        l = self.j + 1
        while (k <= 3 and l <= 3):
            attackList.remove([k, l])
            k += 1
            l += 1
        k = self.i+1
        l = self.j-1
        while (k <= 3 and l >= 0):
            attackList.remove([k, l])
            k += 1
            l -= 1
        k = self.i - 1
        l = self.j + 1
        while (k >= 0 and l <= 3):
            attackList.remove([k, l])
            k -= 1
            l += 1
        k = self.i - 1
        l = self.j - 1
        while (k >= 0 and l >= 0):
            attackList.remove([k, l])
            k -= 1
            l -= 1


class rook(piece):
    def __init__(self, horizontal_conditions, vertical_conditions, i, j):
        self.horizontal_conditions = horizontal_conditions
        self.vertical_conditions = vertical_conditions
        self.i = i
        self.j = j

    def __str__(self):
        return "R"

    def attack(self, attackList):
        """
        Calculates the attack positions given the current position of the rook\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
            n: int - size of the board\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0
        """
        # Vertical and Horizontal attacking spaces
        for n in range(0, 4):
            attackList.append([n, self.j])
            attackList.append([self.i, n])

    def de_attack(self, attackList):
        """
        Calculates the attack positions given the current position of the rook\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
            n: int - size of the board\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0
        """
        # Vertical and Horizontal attacking spaces
        for n in range(0, 4):
            attackList.remove([n, self.j])
            attackList.remove([self.i, n])


class queen(rook):
    def __init__(self, horizontal_conditions, vertical_conditions, diagonal_conditions, i, j):
        super().__init__(horizontal_conditions, vertical_conditions, i, j)
        self.diagonal_conditions = diagonal_conditions
        self.i = i
        self.j = j

    def __str__(self):
        return "Q"

    def attack(self, attackList):
        # Vertical and Horizontal attacking spaces
        for n in range(0, 4):
            attackList.append([n, self.j])
            attackList.append([self.i, n])

        # Diagonal attacking spaces
        k = self.i + 1
        l = self.j + 1
        while (k <= 3 and l <= 3):
            attackList.append([k, l])
            k += 1
            l += 1
        k = self.i+1
        l = self.j-1
        while (k <= 3 and l >= 0):
            attackList.append([k, l])
            k += 1
            l -= 1
        k = self.i - 1
        l = self.j + 1
        while (k >= 0 and l <= 3):
            attackList.append([k, l])
            k -= 1
            l += 1
        k = self.i - 1
        l = self.j - 1
        while (k >= 0 and l >= 0):
            attackList.append([k, l])
            k -= 1
            l -= 1

    def de_attack(self, attackList):
        # Vertical and Horizontal attacking spaces
        for n in range(0, 4):
            attackList.remove([n, self.j])
            attackList.remove([self.i, n])

        # Diagonal attacking spaces
        k = self.i + 1
        l = self.j + 1
        while (k <= 3 and l <= 3):
            attackList.remove([k, l])
            k += 1
            l += 1
        k = self.i+1
        l = self.j-1
        while (k <= 3 and l >= 0):
            attackList.remove([k, l])
            k += 1
            l -= 1
        k = self.i - 1
        l = self.j + 1
        while (k >= 0 and l <= 3):
            attackList.remove([k, l])
            k -= 1
            l += 1
        k = self.i - 1
        l = self.j - 1
        while (k >= 0 and l >= 0):
            attackList.remove([k, l])
            k -= 1
            l -= 1


class knight(piece):
    def __init__(self, knight_conditions, i, j):
        self.knight_conditions = knight_conditions
        self.i = i
        self.j = j

    def __str__(self):
        return "H"

    def attack(self, attackList):
        """
        Calculates the attack positions given the current position of the knight\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0
        """
        attackList.append([self.i-2, self.j-1])
        attackList.append([self.i-2, self.j+1])
        attackList.append([self.i-1, self.j-2])
        attackList.append([self.i-1, self.j+2])
        attackList.append([self.i+1, self.j-2])
        attackList.append([self.i+1, self.j+2])
        attackList.append([self.i+2, self.j-1])
        attackList.append([self.i+2, self.j+1])

    def de_attack(self, attackList):
        """
        Calculates the attack positions given the current position of the knight\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0
        """
        attackList.remove([self.i-2, self.j-1])
        attackList.remove([self.i-2, self.j+1])
        attackList.remove([self.i-1, self.j-2])
        attackList.remove([self.i-1, self.j+2])
        attackList.remove([self.i+1, self.j-2])
        attackList.remove([self.i+1, self.j+2])
        attackList.remove([self.i+2, self.j-1])
        attackList.remove([self.i+2, self.j+1])


class king(piece):
    def __init__(self, king_conditions, i, j):
        self.king_conditions = king_conditions
        self.i = i
        self.j = j

    def __str__(self):
        return "K"

    def attack(self, attackList):
        """
        Calculates the attack positions given the current position of the king\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0
        """
        attackList.append([self.i + 1, self.j])
        attackList.append([self.i - 1, self.j])
        attackList.append([self.i, self.j+1])
        attackList.append([self.i, self.j-1])
        attackList.append([self.i + 1, self.j+1])
        attackList.append([self.i + 1, self.j-1])
        attackList.append([self.i - 1, self.j+1])
        attackList.append([self.i - 1, self.j-1])

    def attack(self, attackList):
        """
        Calculates the attack positions given the current position of the king\n
        Parameters:\n
            i: int - the current row position of the rook\n
            i: int - the current column position of the rook\n
        Returns:\n
            attack_spaces: array - Returns an array of all the positions (i,j) that the rook can attack\n
        Raises:\n
            ValueError: if n is less than 0
        """
        attackList.remove([self.i + 1, self.j])
        attackList.remove([self.i - 1, self.j])
        attackList.remove([self.i, self.j+1])
        attackList.remove([self.i, self.j-1])
        attackList.remove([self.i + 1, self.j+1])
        attackList.remove([self.i + 1, self.j-1])
        attackList.remove([self.i - 1, self.j+1])
        attackList.remove([self.i - 1, self.j-1])


def generate_n_pieces(n):
    list_of_pieces = []
    dictionary_of_pieces = {
        0: queen(True, True, True, 0, 0),
        1: bishop(0, 0),
        2: rook(True, True, 0, 0),
        3: knight(True, 0, 0),
        4: king(True, 0, 0)
    }
    for i in range(n):
        random_num = randint(0, 4)
        list_of_pieces.append(dictionary_of_pieces[random_num])

    return list_of_pieces
