import numpy as np
import matplotlib.pyplot as plt

# Given data
t = np.array([0, 2, 4, 6, 8, 10])
V = np.array([0, 33, 55, 70, 80, 85])

# Fit quadratic curve (degree = 2)
coeff = np.polyfit(t, V, 2)

# Extract coefficients
c, b, a = coeff  # polyfit gives [c, b, a]

print("Fitted Equation:")
print(f"V = {a:.2f} + {b:.2f}t + {c:.2f}t^2")

# Predicted values
V_pred = a + b*t + c*t**2

# R-squared calculation (goodness of fit)
ss_res = np.sum((V - V_pred)**2)
ss_tot = np.sum((V - np.mean(V))**2)
r2 = 1 - (ss_res / ss_tot)

print("R^2 value:", r2)

# Generate smooth curve for plotting
t_new = np.linspace(0, 10, 100)
V_new = a + b*t_new + c*t_new**2

# Plot
plt.scatter(t, V)
plt.plot(t_new, V_new)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.title("Curve Fitting using Least Squares")
plt.show()
output 
Fitted Equation:
V = 2.38 + 12.21t + -0.63t^2

R^2 value: 0.998
