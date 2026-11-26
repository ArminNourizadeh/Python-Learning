print("Cube Volume and Surface Area Calculator\n")

side = float(input("Enter the Side Length of the Cube: "))

# -----------------------

volume = side ** 3
surface_area = 6 * (side ** 2)

# -----------------------

print("-" * 30)
print("Volume:", volume)
print("Surface Area:", surface_area)
