from sage.all import *


def main():
     a1, a2, a3, a4= var("a1 a2 a3 a4")
     b1, b2, b3, b4= var("b1 b2 b3 b4")
     c1, c2, c3, c4= var("c1 c2 c3 c4")
     d1, d2, d3, d4= var("d1 d2 d3 d4")
     eqs = [b1==0, b3==0, d1==0, d3==0,
         a1*b4==0,c3*b4==0,
         a1**2+a2**2==2*a1*b2,
         c1**2+c3**2==2*c3*b2,
         (c1+a3)*b4==0,
         (a1*c1+a3*c3)==(c1+a3)/b2]

     sol = solve(eqs, a1, a2, a3, a4, b2, b4,c1, c2, c3, c4, d2, d4)
     print(eqs)
     print(f'the solution of eqs is: \n', sol)


if __name__ == '__main__':
    main()
