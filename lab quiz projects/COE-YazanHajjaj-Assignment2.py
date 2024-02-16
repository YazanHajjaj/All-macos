import random

# Question1
def array(size): # Function that gives array numbers
    return [random.randint(1, 100)
            for _ in range(size)]


def main():
    N = int(input("Enter the value of N: "))  # Function that requires you to input and integer to give the array
    data_array = array(N)

    print(f"Generated Array: {data_array}")

    def calculate_sum(numbers): # Function that calculates the sum in the generated array
        return sum(numbers)

    print(f"The sum of all numbers is: {calculate_sum(data_array)}")

    def average(numbers):
        return sum(numbers) / len(numbers)

    print(f"The average of the numbers is: {average(data_array):.2f}")

    def product(numbers): # Function that calculates the product in the generated array
        result = 1
        for num in numbers:
            result *= num
        return result

    print(f"The product of all numbers is: {product(data_array)}")

    def find_maximum(numbers): # Function that find tha maximum number in the generated array
        return max(numbers)

    print(f"The maximum number is: {find_maximum(data_array)}")

    def find_minimum(numbers):  # Function that find tha minimum number in the generated array
        return min(numbers)

    print(f"The minimum number is: {find_minimum(data_array)}")

    def prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primes_numbers(numbers):
        return sum(1 for num in numbers if prime(num))

    print(f"The count of prime numbers is: {primes_numbers(data_array)}")


if __name__ == "__main__":
    main()


# Question2

def average(marks):
    if len(marks) < 4:
        return sum(marks) / len(marks)

    else:
        sorted_marks = sorted(marks, reverse=True)[3:]  # Removes the three worst marks
        return sum(sorted_marks) / len(sorted_marks)


lab_marks = []

while True:  # Take input until a negative number is entered

    mark = int(input("Enter lab mark (enter a negative number to finish): "))
    if mark < 0:
        break
    lab_marks.append(mark)

average_marks = average(lab_marks)
print("Average of lab marks:", average_marks)

# Question3

numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]
print(subset)
# justification the output is this because the subset element slices the numbers list starting from 1 and ending at 4

fruits = ["Apple", "Banana", "Orange"]
fruits[1] += "split"
print(fruits)
# since fruits[1] modifies  element at index 1  this will be the output

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")  # the codes use if num % 2 == 0: to check if it even or odd

fruits = ["Apple", "Banana", "Orange"]
fruits[1] = "Grapes"
print(fruits)
# since fruits[1] modifies  element at index 1  the output will be the ['Apple', 'Grapes', 'Orange'].


# Question 4

def series(n):
    if n == 0:  # when n is 0 return 0
        return 0
    elif n == 1:  # when n is 1 return 1
        return 1
    else:
        return series(n - 1) + 2 * series(n - 2)  # calculate nth term using this formula


try:
    n = int(input("Enter the value of n: "))  # Get input for the value of n
    if n < 0:
        raise ValueError("Please enter a non-negative integer.")

    result = series(n)  # Calculate the nth term using the series function
    print(f"The {n}th term of the series is: {result}")

except ValueError as e:
    print(f"Error: {e}")
