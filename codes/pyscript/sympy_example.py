import sympy as sym


def main():
    x = sym.Symbol('x')
    f = x**3 + 2 * x**2 + x + 1

    print(f"The function is f(x) = {f} ")

    df_dx = sym.diff(f, x)
    print(f"Derivative of f(x): {df_dx}")

    integral_f = sym.integrate(f, x)
    print(f"Indefinite integral of f(x): {integral_f}")

    definite_integral = sym.integrate(f, (x, 0, 1))
    print(f"Definite integral of f(x) from 0 to 1: {definite_integral}")


if __name__ == "__main__":
    main()
