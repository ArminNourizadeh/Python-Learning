print("Rectangle Area and Perimeter Calculator\n")

length = float(input("Enter the Length of the Rectangle: "))
width = float(input("Enter the Width of the Rectangle: "))

# -----------------------

area = length * width
perimeter = (2 * length) + (2 * width)

# -----------------------

print("-" * 30)
print("Area:", area)
print("Perimeter:", perimeter)
