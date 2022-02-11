from FiniteFieldP import FiniteFieldP, FiniteFieldPElement


def main():
    FF19 = FiniteFieldP(19)
    z = FiniteFieldPElement(FF19, 0)
    a5 = FiniteFieldPElement(FF19, 5)
    a7 = FiniteFieldPElement(FF19, 7)
    print(a5 + a7)
    print(a5 * a7)
    print(a7 - a5)
    print(a7 / a5)
    print(a5 + -a7)
    print(a5 == a7)
    print(z)


if __name__ == '__main__':
    main()
