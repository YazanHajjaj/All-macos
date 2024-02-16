import math

# let 3the user to enter values for a, b, and c
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    # Two real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are {root1} and {root2}")
elif discriminant == 0:
    # One real root
    root = -b / (2*a)
    print(f"The root is {root}")
else:
    # No real roots
    print("The equation has no real roots")
