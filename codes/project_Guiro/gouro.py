from sage.all import *

def gen_lambda4(arg):
    # Example de dimension 4
    # e0^2 = e0
    # e1^2 = 2e1
    # e1 * e2 = e2
    #
    y, z = var('y z', domain='integer')
    M0 = Matrix([[1,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0] ])
    M1 = Matrix([[0,0,0,0],[0,2,0,0],[0,0,1,0], [0,0,0,0]])
    M2 = Matrix([[0,0,0,0],[0,0,1,0],[0,0,0,0], [0,0,0,y] ])
    M3 = Matrix([[0,0,0,0],[0,0,0,0],[0,0,y,0], [0,0,0,z] ])

    my_algebres = []
    polynomial = 2*x*(x*(x*(x*x))) + x*((x*x)*(x*x)) - 3*x*(x*x)*(x*x)
    for i in set_xyz :
        for j in set_xyz :
            y = i
            z = j
            examp = [M0, M1, M2, M3]
            A4 = FiniteDimensionalAlgebra(QQ, examp)
            if not A4.is_associative() :
                elts = [A4.random_element() for k in range(20)]
                k = 1
                for x in elts:
                    if  polynomial== 0:
                        print(f"{k}. (y,z) = {(y,z)}", x)
                        my_algebres +=[A4]
                        break
                        k = k + 1

    e = A4.basis()


def main():
    # Example 2.1
    # e0^2 = e0
    # e1^2 = 2e1
    # e1 * e2 = e2

    M0 = Matrix([[1,0,0],[0,0,0],[0,0,0] ])
    M1 = Matrix([[0,0,0],[0,2,0],[0,0,1] ])
    M2 = Matrix([[0,0,0],[0,0,1],[0,0,0] ])

    a, b, g = var('a b g', domain=RR)
    C = FiniteDimensionalAlgebra(QQ, [M0, M1, M2])

    e = C.basis()
    e0, e1, e2 = e[0], e[1], e[2]

    assert e0*e0 == e0
    assert e1*e1 == 2*e1
    assert e1*e2 == e2

    x = e0 + e1 + 2*e2
    y = e0 + e1 + e2

    print(f"Is the algebra commutative? {C.is_associative()}")

    assert 2*x*(x*(x*(x*x))) + x*((x*x)*(x*x)) - 3*x*(x*x)*(x*x) == 0
    print(f"x*(x^2*y) + 2x(x(xy)) - 3x(x^2)y = {x*((x*x)*y) + 2*x*(x*(x*y)) - 3*(x*(x*x))*y}")

if __name__ == '__main__':
    main()
