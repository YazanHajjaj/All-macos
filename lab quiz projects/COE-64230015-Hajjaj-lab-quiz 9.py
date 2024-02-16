class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

equilateral = Triangle(4, 4, 4)
print(equilateral.is_equilateral())

non_equilateral = Triangle(4, 4, 5)
print(non_equilateral.is_equilateral())



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has started.")


my_car = Car("Dodge", "Challenger", 2020)

my_car.start_engine()









