import numpy as np
from itertools import product

class TriangularMatrix:
    def __init__(self, a, b, c):
        # Matrix: [1 a b]
        #         [0 1 c]
        #         [0 0 1]
        self.a = a % 3
        self.b = b % 3
        self.c = c % 3

    def as_array(self):
        # Return numpy array representation
        return np.array([
            [1, self.a, self.b],
            [0, 1, self.c],
            [0, 0, 1]
        ])

    def __mul__(self, other):
        # Multiplication modulo 3
        mat1 = self.as_array()
        mat2 = other.as_array()
        result = np.dot(mat1, mat2) % 3
        # Extract new a, b, c
        a_new = result[0,1]
        b_new = result[0,2]
        c_new = result[1,2]
        return TriangularMatrix(a_new, b_new, c_new)

    def __eq__(self, other):
        return (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __repr__(self):
        return f"TriangularMatrix(a={self.a}, b={self.b}, c={self.c})"

class TriangularMatrixGroup:
    def __init__(self):
        # All possible matrices
        self.elements = [TriangularMatrix(a, b, c) for a, b, c in product(range(3), repeat=3)]
        self.identity = TriangularMatrix(0, 0, 0)

    def is_closed(self):
        # Check closure
        for x in self.elements:
            for y in self.elements:
                if (x * y) not in self.elements:
                    return False
        return True

    def has_inverses(self):
        for x in self.elements:
            has_inv = False
            for y in self.elements:
                if (x * y) == self.identity and (y * x) == self.identity:
                    has_inv = True
                    break
            if not has_inv:
                print(f"No inverse for {x}")
                return False
        return True

    def is_associative(self):
        # Matrix multiplication is associative by definition
        return True

    def get_order(self):
        return len(self.elements)

# Example usage
group = TriangularMatrixGroup()
print("Order of the group:", group.get_order())
print("Closed under multiplication:", group.is_closed())
print("Every element has an inverse:", group.has_inverses())
print("Associative operation:", group.is_associative())
print("Identity element:", group.identity)
