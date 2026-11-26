print("Trapezoid Area and Perimeter Calculator\n")

side_a = float(input("Enter Side A: "))
side_b = float(input("Enter Side B (First Base): "))
side_b2 = float(input("Enter Side B2 (Second Base): "))
side_c = float(input("Enter Side C: "))
height = float(input("Enter Height: "))

# -----------------------

area = ((side_b + side_b2) * height) / 2
perimeter = side_a + side_b + side_b2 + side_c

# -----------------------

print("-" * 30)
print("Area:", area)
print("Perimeter:", perimeter)
