print("Triangle Area and Perimeter Calculator\n")
#-----------------------------
side_a = float(input("Enter a Side A of the Triangle : "))
side_b = float(input("Enter a Side B of the Triangle : "))
side_c = float(input("Enter a Side C of the Triangle : "))
height = float(input("Enter a height of the Triangle : "))

# Calculate area and perimeter
area = (side_b * height) / 2
perimeter = side_a + side_b + side_c

print("-" * 30)
print("Area:", area)
print("Perimeter:", perimeter)
