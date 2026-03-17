# Gauss Jacobi Method for 3 equations

# Initial guesses
I1 = 0
I2 = 0
I3 = 0

print("Iteration\tI1\t\tI2\t\tI3")

for i in range(1, 6):
    I1_new = (14 + 8*I2) / 14
    I2_new = (-2 + 8*I1 + 5*I3) / 16
    I3_new = (28 + 5*I2) / 10

    print(i, "\t\t", round(I1_new,4), "\t", round(I2_new,4), "\t", round(I3_new,4))

    I1 = I1_new
    I2 = I2_new
    I3 = I3_new
  
