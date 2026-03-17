# Newton Forward Interpolation

import numpy as np

# Given data
t = np.array([0, 2, 4, 6, 8, 10], dtype=float)
V = np.array([0, 33, 55, 70, 80, 85], dtype=float)

n = len(t)

# Create forward difference table
diff_table = np.zeros((n, n))
diff_table[:,0] = V

for j in range(1, n):
    for i in range(n - j):
        diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]

# Value to interpolate
x = 1
h = t[1] - t[0]
u = (x - t[0]) / h

# Interpolation
result = diff_table[0][0]
u_term = 1

for i in range(1, n):
    u_term = u_term * (u - (i - 1)) / i
    result += u_term * diff_table[0][i]

print("Interpolated voltage at t = 1 ms is:", round(result, 2)
      output:
Interpolated voltage at t = 1 ms is: 18.20
