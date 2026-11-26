print("Square and Rectangular Pyramid Volume Calculator\n")

length = float(input("Enter Length of the Base: "))
width = float(input("Enter Width of the Base: "))
height = float(input("Enter Vertical Height: "))

# -----------------------

volume = (length * width * height) / 3

# -----------------------

print("-" * 30)
print("Volume:", volume)
