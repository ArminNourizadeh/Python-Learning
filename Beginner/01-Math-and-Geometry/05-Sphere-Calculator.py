print("Sphere Volume and Surface Area Calculator\n")

radius = float(input("Enter the Radius of the Sphere: "))

# -----------------------

volume = (4 / 3) * 3.14 * (radius ** 3)
surface_area = 4 * 3.14 * (radius ** 2)

# -----------------------

print("-" * 30)
print("Volume:", volume)
print("Surface Area:", surface_area)
