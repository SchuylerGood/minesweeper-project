from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

E = Encoding()
#============== Propositions ==================

# Attack position proposition
@proposition(E)
class attack_position_proposition:
    def __init__(self, i, j, f, r):
        self.i = i
        self.j = j
        self.f = f
        self.r = r
        # self.ij = position
    
    def __repr__(self):
        return f"X({self.i},{self.j})"

# Position proposition
@proposition(E)
class piece_position_proposition:
    def __init__(self, i, j, f, r):
        self.i = i
        self.j = j
        self.f = f
        self.r = r
    
    def __repr__(self):
        return f"P({self.i},{self.j})"

# King Position proposition
@proposition(E)
class king_position_proposition:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __repr__(self):
        return f"K({self.i},{self.j})"

# Bishop Position proposition
@proposition(E)
class bishop_position_proposition:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __repr__(self):
        return f"B({self.i},{self.j})"

# Rook Position proposition
@proposition(E)
class rook_position_proposition:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __repr__(self):
        return f"R({self.i},{self.j})"

# Knight Position proposition
@proposition(E)
class knight_position_proposition:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __repr__(self):
        return f"H({self.i},{self.j})"

# Queen Position proposition
@proposition(E)
class queen_position_proposition:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def __repr__(self):
        return f"Q({self.i},{self.j})"

#===============================================


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html


# Example of fancy propositions
# @constraint.at_least_one(E)
# @proposition(E)
# class FancyPropositions:

#     def __init__(self, data):
#         self.data = data

#     def __repr__(self):
#         return f"A.{self.data}"

# Temporary varialbes that will be replaced with actual values later on
n = "Size of the board"
f = "file" # file is a chess term for column of the board
r = "row"
m = "m scalar for i & j, (diagonals)"
i = "i-position"
j = "j-position"

# Base propositions, to be used in the constraints
x = attack_position_proposition(i,j,f,r) # Is true if a piece can attack the position (i, j).
p = piece_position_proposition(i,j,f,r) # Is true when any piece is in position (i, j).
k = king_position_proposition(i,j) # Is true if there is a King in position (i, j).
b = bishop_position_proposition(i,j) # Is true if there is a Bishop in position (i, j).
r = rook_position_proposition(i,j) # Is true if there is a Rook in position (i, j).
h = knight_position_proposition(i,j) # Is true if there is a Knight in position (i, j).
q = queen_position_proposition(i,j) # Is true if there is a Queen in position (i, j).




# At least one of these will be true
# x = FancyPropositions("x")
# y = FancyPropositions("y")
# z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():

    #==========  Current Constraints  ================

    # Queen Constraint 1:
    E.add_constraint(q >> ("∀.f" (x.i ,x.f)) & ("∀.r" (x.r,x.j)) & ("∀.m" (x.i+m,x.j+m) & (x.i+m,x.j-m) & (x.i-m,x.j+m) & (x.i-m,x.j-m)))
    E.add_constraint(q >> (p) & ~(k | h | r | b))

    # Queen Constraint 2:
    E.add_constraint(("∀.f" (~p.i,x.f)) & ("∀.r" (~p.r,~p.j)) & ("∀.m" (~(p.i+m, p.j+m) | ~(p.i+m, p.j-m) | ~(p.i-m, p.j+m) | ~(p.i-m, p.j-m))) >> q)


    # King Constraint 1:
    E.add_constraint(k >> ((x.i-1,x.j-1) & (x.i-1,x.j) & (x.i-1,x.j+1) & (x.i,x.j-1) & (x.i,x.j+1) & (x.i+1,x.j-1) & (x.i+1,x.j) & (x.i+1,x.j+1)))
    E.add_constraint(k >> (p) & ~(q | h | r | b))

    # King Constraint 2:
    E.add_constraint(~(p.i-1, p.j-1 | p.i-1, p.j | p.i-1, p.j+1 | p.i, p.j-1 | p.i,p.j+1 | p.i+1, p.j-1 | p.i+1, p.j | p.i+1, p.j+1) >> k)


    # Knight Constraint 1:
    E.add_constraint(h >> ((x.i-2,x.j-1) & (x.i-2,x.j+1) & (x.i-1,x.j-2) & (x.i-1,x.j+2) & (x.i+1,x.j-2) & (x.i+1,x.j+2) & (x.i+2,x.j-1) & (x.i+2,x.j+1)))
    E.add_constraint(h >> (p) & ~(k | q | r | b))

    # Knight Constraint 2:
    E.add_constraint(~(p.i-2, p.j-1 | p.i-2, p.j+1 | p.i-1, p.j-2 | p.i-1, p.j+2 | p.i+1, p.j-2 | p.i+1, p.j+2 | p.i+2, p.j-1 | p.i+2, p.j+1) >> h)


    # Rook Constraint 1:
    E.add_constraint(r >> ("∀.f" (x.i,f)) & ("∀.r" (x.r,j)))
    E.add_constraint(r >> (p) & ~(k | q | h | b))

    # Rook Constraint 2:
    E.add_constraint(("∀.f" (~p.i, p.f)) & ("∀.r" (~p.r,p.j)) >> r)


    # Bishop Constraint 1:
    E.add_constraint(b >> ("∀.m" (x.i+m,x.j+m) & (x.i+m,x.j-m) & (x.i-m,x.j+m) & (x.i-m,x.j-m)))
    E.add_constraint(b >> (p) & ~(k | q | r | h))

    # Bishop Constraint 2:
    E.add_constraint(("∀.m" (~(p.i+m, p.j+m) | ~(p.i+m, p.j-m) | ~(p.i-m, p.j+m) | ~(p.i-m, p.j-m)) >> b))

    #=================================================


    #============ Example constraints ================
    # # Add custom constraints by creating formulas with the variables you created. 
    # E.add_constraint((a | b) & ~x)

    # # Implication
    # E.add_constraint(y >> z)

    # # Negate a formula
    # E.add_constraint((x & y).negate())

    # # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    # constraint.add_exactly_one(E, a, b, c)

    # return E
    #=================================================


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
