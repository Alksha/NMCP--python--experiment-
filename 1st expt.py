import math

# Given value
x = 1
n = 10   # number of terms

# Exact value
exact = math.exp(x)

# Compute e^x using series expansion
approx = 0
factorial = 1

for i in range(n):
    if i > 0:
        factorial *= i
    approx += (x ** i) / factorial

# Truncation error
truncation_error = abs(exact - approx)

# Round-off error (simulated using rounding to 6 decimal places)
approx_rounded = round(approx, 6)
roundoff_error = abs(approx - approx_rounded)

# Display results
print("Exact value of e^x:", exact)
print("Approximate value (10 terms):", approx)
print("Truncation Error:", truncation_error)
print("Rounded Approx Value:", approx_rounded)
print("Round-off Error:", roundoff_error)
output
Exact value of e^x: 2.718281828459045
Approximate value (10 terms): 2.7182815255731922
Truncation
