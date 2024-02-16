
import math
def circle_area_and_perimeter(radius):

    area = math.pi * radius **2
    perimeter = 2 * radius * math.pi
    print(f"Radius :{radius}")
    print(f"Area of the circle: {area:.2f}")
    print(f"Perimeter of the circle:{perimeter:.2f}")

if  __name__ == "__main__":
    radius = float(input("Enter a radius of the circle:"))
    circle_area_and_perimeter(radius)