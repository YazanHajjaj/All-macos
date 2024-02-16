#Q1
import math

def calculate_f(x, y):
    result = math.sqrt(x**3 + 4*x*y**2) / (2*x + 3*y)
    print("f(x, y) =", result)

# Example:
x = 2
y = 3
calculate_f(x, y)
#Q2 Task 1
def print_string(input_string, y):
    for _ in range(y):
        print(input_string)

# Example:
input_string = "When"
y =2
print_string(input_string, y)

#Q2 Task 2

def print_output(arg1, arg2):
    if isinstance(arg1, int) and isinstance(arg2, int):
        result = str(arg1) + str(arg2)
        print(result)
    elif isinstance(arg1, str) and isinstance(arg2, int):
        result = arg1 * arg2
        print(result)
    else:
        print("Invalid arguments")

# Example usage:
print_output(32, 5)
print_output("Yazan", 5)


#Q2 Task 3
def polygon_internal(n):
    if n < 3:
        print("A polygon must have at least 3 sides.")
    else:
        angle_degree = (n - 2) * 180 / n
        print(f"The degree measure of an internal angle of a {n}-sided polygon is {angle_degree} degrees.")

# Example :
polygon_internal(3)  # Triangle
polygon_internal(4)  # Square
polygon_internal(5)  # Pentagon
polygon_internal(8)  # Octagon

#Q2 Task 4
def count_and_print(number):
    if number < 0:
        print("Please provide a non-negative number.")
    else:
        print("Counting down:")
        for i in range(number, -1 , -1):
            print(i)

        print("Counting up:")
        for i in range(number + 1):
            print(i)

# Example :
count_and_print(7)

#Q2 TASK 5

def print_even(start, end):
    if start % 2 != 0 or end % 2 != 0:
        print("Both numbers should be even.")
    else:
        print("Even numbers between", start, "and", end, "using a for loop:")
        for num in range(start + 2, end, 2):
            print(num)

# Example:
print_even(10, 20)
