print("Cone Volume and Surface Area Calculator\n")

radius = float(input("Enter the Radius of the Cone: "))
height = float(input("Enter the Vertical Height of the Cone: "))

# -----------------------

slant_height = (radius ** 2 + height ** 2) ** 0.5

volume = (3.14 * (radius ** 2) * height) / 3
surface_area = 3.14 * radius * (radius + slant_height)

# -----------------------

print("-" * 30)
print("Volume:", volume)
print("Surface Area:", surface_area)
