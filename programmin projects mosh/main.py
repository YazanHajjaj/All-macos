class Class1:
    def __init__(self, ayshe, number, alt):
        self.ayshe = ayshe
        self.number = number
        self.alt = alt

    def print_type(self):
        print("Class 1")

class Class2:
    def __init__(self, ayshe, number, alt):
        self.ayshe = ayshe
        self.number = number
        self.alt = alt

    def print_type(self):
        print("Class 2")

class Class3:
    def __init__(self, ayshe, number, alt):
        self.ayshe = ayshe
        self.number = number
        self.alt = alt

    def print_type(self):
        print("Class 3")

# Example usage:
cls1 = Class2(ayshe='ayshe', number=2313141, alt='alt')
cls2 = Class3(ayshe='ayshe', number=2313141, alt='alt')
cls3 = Class1(ayshe='ayshe', number=2313141, alt='alt')

# Accessing attributes
print(cls1.ayshe)
print(cls2.number)
print(cls3.alt)

# Printing types
cls1.print_type()
cls2.print_type()
cls3.print_type()
