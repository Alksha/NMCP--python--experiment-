import numpy as np

def f(t):
    return 4 - 4 * np.exp(-5 * t)

a = 0
b = 0.1
n = 4

h = (b - a) / n

t = np.linspace(a, b, n+1)

I = f(t[0]) + f(t[n])

for i in range(1, n):
    if i % 2 == 0:
        I += 2 * f(t[i])
    else:
        I += 4 * f(t[i])

I = (h / 3) * I

print("Average Current =", round(I, 4))
output:
Average Current = 0.0853
