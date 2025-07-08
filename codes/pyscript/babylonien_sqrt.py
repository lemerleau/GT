from numpy import random, sqrt, round
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def bsqrt(s, iter=10):
    x = 1.
    for i in range(iter):
        y = (x*x +s)/(2*x)
        print(f"iter {i} avec x = {x}")
        if (y==x):
            break
        else :
            x = y
    return x, i

def main():
    doc_ = """
    This program uses the Babylonien Algorithm to compute the square root of any positive integer.
            """
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        argument_default=SUPPRESS,
        description=doc_)
    parser.add_argument(
        '--s',
        type=int,
        help="An integer input for which we compute the sqrt root.")
    parser.add_argument(
        '--iter',
        type=int,
        default = 10,
        help="The maximum number of iterations.")
    args = parser.parse_args()
    s = args.s
    iter = args.iter
    if s<0 :
        print("My program can't compute a square root of negative numbers. Please, input a positive integer.")
        exit(0)

    print("*"*51)
    print(" "*15 +"Runing my Babylonien algo"+(" "*15))
    print("*"*51 +"\n\n")
    mysqrt, i = bsqrt(s, iter)
    print(f"Program terminated after {i+1} iterations.")
    print("*"*51 +"\n\n")
    npsqrt = sqrt(s)
    print("*"*51)
    print(" "*22 +"Results"+(" "*22))
    print("*"*51)
    print("The input is s = {}".format(s))
    print("Your square root of {} is {}".format(s, mysqrt))
    print("The numpy square root of {} is {}".format(s, npsqrt))
    print("The error precision is ", abs(mysqrt - npsqrt))
    print("*"*51)

if __name__ == '__main__':
    main()
