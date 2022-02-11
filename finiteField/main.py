from FiniteFieldP import FiniteFieldP, FiniteFieldPElement


def main():
    FF19 = FiniteFieldP(19)
    z = FiniteFieldPElement(FF19, 0)
    a5 = FiniteFieldPElement(FF19, 4)
    a7 = FiniteFieldPElement(FF19, 2)
    print(a5 + a7)
    print(a5 * a7)
    print(a7 - a5)
    print(a7 / a5)
    print(a5 + -a7)
    print(a5 == a7)
    print(a5.p)


if __name__ == '__main__':
    main()
