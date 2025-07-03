
import numpy as np
from itertools import product

def generate_triangular_matrices():
    matrices = []
    for a, b, c in product([0, 1, 2], repeat=3):
        M = np.array([
            [1, a, b],
            [0, 1, c],
            [0, 0, 1]
        ])
        matrices.append(M.tolist())
    return matrices


class HeisenbergGroup:
    def __init__(self):
        # Elements are represented as upper triangular matrices of integers
        self.elements = generate_triangular_matrices()
        self.identity = np.array([
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]
            ])

    def list(self):
        return self.elements

    def _operation(self, a, b):
        return np.dot(np.array(a),np.array(b))%3

    def is_closed(self):
        for a in self.elements:
            for b in self.elements:
                if self._operation(a, b).tolist() not in self.elements:
                    return False
        return True

    def is_associative(self):
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if not np.array_equal(self._operation(self._operation(a, b).tolist(), c).tolist(), self._operation(a, self._operation(b, c).tolist()).tolist()):
                        return False
        return True

    def has_identity(self):
        for a in self.elements:
            if not np.array_equal(self._operation(a, self.identity), a) or not np.array_equal(self._operation(self.identity, a),a):
                return False
        return True

    def has_inverses(self):
        for a in self.elements:
            found_inverse = False
            for b in self.elements:
                if np.array_equal(self._operation(a, b), self.identity):  # id_ is the identity
                    found_inverse = True
                    break
            if not found_inverse:
                return False
        return True

    def is_group(self):
        return (self.is_closed() and
                self.is_associative() and
                self.has_identity() and
                self.has_inverses())

def main():
    # Example Usage
    H = HeisenbergGroup()
    print(H.list())
    print(f"Est ce que H is un group? {H.is_group()}")
    print(f"Est ce que H est fermé? {H.is_closed()}")
    print(f"Est ce que H est associative? {H.is_associative()}")
    print(f"Est ce que H a un element neutre? {H.has_identity()}")
    print("Est ce que tout element de H a un inverse?:", H.has_inverses())
    print("Identity element:\n", H.identity)
if __name__ == '__main__':
    main()
