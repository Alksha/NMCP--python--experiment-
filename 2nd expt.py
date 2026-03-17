# f(x) = x^3 - 5x + 1

def f(x):
    return x**3 - 5*x + 1

def df(x):
    return 3*x**2 - 5


# 🔵 Bisection Method
def bisection(a, b, n):
    print("\nBisection Method:")
    for i in range(1, n+1):
        c = (a + b) / 2
        print(f"Iteration {i}: x = {c:.6f}, f(x) = {f(c):.6f}")
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"Final Root (Bisection) = {c:.6f}")


# 🟢 Regula Falsi Method
def regula_falsi(a, b, n):
    print("\nRegula Falsi Method:")
    for i in range(1, n+1):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        print(f"Iteration {i}: x = {c:.6f}, f(x) = {f(c):.6f}")
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print(f"Final Root (Regula Falsi) = {c:.6f}")


# 🔴 Newton-Raphson Method
def newton_raphson(x0, n):
    print("\nNewton-Raphson Method:")
    x = x0
    for i in range(1, n+1):
        x = x - f(x)/df(x)
        print(f"Iteration {i}: x = {x:.6f}, f(x) = {f(x):.6f}")
    print(f"Final Root (Newton-Raphson) = {x:.6f}")


# Main program
a = 0
b = 1
iterations = 5

bisection(a, b, iterations)
regula_falsi(a, b, iterations)
newton_raphson(0.5, iterations)
