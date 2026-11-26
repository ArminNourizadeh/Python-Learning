print("Cylinder Volume and Surface Area Calculator\n")

radius = float(input("Enter the Radius of the Cylinder: "))
height = float(input("Enter the Height of the Cylinder: "))

# -----------------------

volume = 3.14 * (radius ** 2) * height
surface_area = (2 * 3.14 * radius * height) + (2 * 3.14 * (radius ** 2))

# -----------------------

print("-" * 30)
print("Volume:", volume)
print("Surface Area:", surface_area)
