class FiniteFieldP:
    def __init__(self, p):
        # primality test for <p>
        self.p = p
        self.elements = [FiniteFieldPElement(self, e) for e in range(self.p)]


class FiniteFieldPElement:
    def __init__(self, parent, a):
        self.parent = parent
        self.p = parent.p
        if not isinstance(a, int):
            raise TypeError("Field element must be integer")
        self.rep = a % self.p

    def __add__(self, other):
        return FiniteFieldPElement(self.parent, (self.rep + other.rep) % self.p)

    def __mul__(self, other):
        return FiniteFieldPElement(self.parent, (self.rep * other.rep) % self.p)

    def __pow__(self, exp):
        return FiniteFieldPElement(self.parent, self.rep.__pow__(exp, self.p))

    def __str__(self):
        return "FFE" + str(self.rep)

    def __repr__(self):
        return str(self.rep)

    def __sub__(self, other):
        return FiniteFieldPElement(self.parent, (self.rep - other.rep) % self.p)

    def __truediv__(self, other):
        try:
            return FiniteFieldPElement(self.parent, self.rep.__pow__(other.rep, self.p))
        except ZeroDivisionError:
            print('Cannot divide by zero')

    def __neg__(self):
        return FiniteFieldPElement(self.parent, -self.p)

    def __eq__(self, other):
        if isinstance(other, FiniteFieldPElement) and self.rep == other.rep:
            return True
        return False

