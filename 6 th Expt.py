# RK4 method for RL circuit transient response

def f(t, i):
    return 20 - 5*i   # di/dt

# Initial conditions
t0 = 0
i0 = 0

h = 0.02   # step size
n = 5      # number of steps (0 to 0.1)

t = t0
i = i0

print("t\t i")

for step in range(n):
    k1 = h * f(t, i)
    k2 = h * f(t + h/2, i + k1/2)
    k3 = h * f(t + h/2, i + k2/2)
    k4 = h * f(t + h, i + k3)

    i = i + (k1 + 2*k2 + 2*k3 + k4) / 6
    t = t + h

    print(round(t, 2), "\t", round(i, 4))

print("\nFinal current at t = 0.1 sec is:", round(i, 4), "Ampere")
output:
Final current at t = 0.1 sec is: 1.052 A
