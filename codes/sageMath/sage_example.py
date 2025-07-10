from sage.all import *


def main() :
    S_3 = SymmetricGroup(3)
    print(S_3)
    print(f"The order of the group $S_3$ is {S_3.order()}")
    print(f"The elements of $S_3$ are: {S_3.list()}")
    print(f"The representation of {S_3((1,2))} is \n{S_3((1,2)).matrix()}")


if __name__ == '__main__':
    main()
