class CyclicGroupOrder3:
    def __init__(self):
        # Elements are represented as integers 0, 1, 2
        # where 0 is the identity element.
        self.elements = {0, 1, 2}

    def _operation(self, a, b):
        # Group operation is addition modulo 3
        return (a + b) % 3

    def is_closed(self):
        for a in self.elements:
            for b in self.elements:
                if self._operation(a, b) not in self.elements:
                    return False
        return True

    def is_associative(self):
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if self._operation(self._operation(a, b), c) != self._operation(a, self._operation(b, c)):
                        return False
        return True

    def has_identity(self):
        # Identity element is 0
        identity = 0
        for a in self.elements:
            if self._operation(a, identity) != a or self._operation(identity, a) != a:
                return False
        return True

    def has_inverses(self):
        for a in self.elements:
            found_inverse = False
            for b in self.elements:
                if self._operation(a, b) == 0:  # 0 is the identity
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
    c3 = CyclicGroupOrder3()
    print(f"Is C3 a group? {c3.is_group()}")
    print(f"Is C3 closed? {c3.is_closed()}")
    print(f"Is C3 associative? {c3.is_associative()}")
    print(f"Does C3 have an identity element? {c3.has_identity()}")
    print(f"Does C3 have inverses for all elements? {c3.has_inverses()}")

if __name__ == '__main__':
    main()
