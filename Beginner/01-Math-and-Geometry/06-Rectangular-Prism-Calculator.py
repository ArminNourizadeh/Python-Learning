print("Rectangular Prism Volume and Surface Area Calculator\n")

length = float(input("Enter the Length of the Rectangular Prism: "))
width = float(input("Enter the Width of the Rectangular Prism: "))
height = float(input("Enter the Height of the Rectangular Prism: "))

# -----------------------

volume = length * width * height
surface_area = (2 * length * height) + (2 * width * height) + (2 * length * width)

# -----------------------

print("-" * 30)
print("Volume:", volume)
print("Surface Area:", surface_area)
