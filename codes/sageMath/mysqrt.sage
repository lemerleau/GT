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
