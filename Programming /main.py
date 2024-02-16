"""name = input("What is your name? ")
color = input("What color do you like the most? ")
print(name + "" + " likes " + color)

birth_year = input("Birth year: ")
age = 2023 - int(birth_year) #birth year needs an operand to run
print(age)
weight_lbs = int(input("Weight (lbs): ")) # First way
weight_kgs = int(weight_lbs) * 0.45 # second way no need two do it twice
print(weight_kgs)

course = "Hi py"
another = course
# print(course[0:4]) # it will exclude the index at the last which is 4
# print(course[1:])  # it will exclude the index at the first which 0
# print(course[:4])  # the interpreter will assume 0 as the index
print(another)

first_name = "Yazan"
last_name = "Hajjaj"
message = f"{first_name} [{last_name}] is a coder"  # f is a formatted string
print(message)

course  "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find("f"))  # it is case-sensitive it gives the index
print(course.replace("Beginners", "Absolute Beginners"))
print(course)
print("Python" in course)  # it is case-sensitive it gives a boolean value

x = 10
# x = x + 3
#x += 3  # augmented assignment operator
x -= 3
print(x)

x = 10 + 3 * 2  # operator precedence exponentiation multiplication or division add or substra

x = 2.9
print(round(x))
print(abs(-2)) # Absolute value

is_hot = False
is_cold = False
is_humid = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm cloth")
elif is_humid:
    print("it is a humid day")
else:
    print("It's a lovely day")
print("Enjoy your day")

price_house = 1000000
good_credit = True

if good_credit:
   down_payment = 0.1 * price_house
   print(down_payment)
else:
   down_payment = 0.2 * price_house

print(f"Down payment : ${down_payment}")

high_income = True
good_credit = True
has_criminal_record = False
# if high_income and good_credit: # Logical operator "and" and "or" and need both conditions to be the same
#  print("Eligible for loan")
if good_credit and not has_criminal_record:  # it converts the boolean value true to false
    print("Eligible for loan")

temp = 30

if temp > 30: # >= greater than != not equal <= less than
    print("It's a hot day")
else:
    print("It's not a hot day")

name = input("enter your name : ")


if len(name) < 3:
    print("Name must be at least 3 characters ")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("looks good")

weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ") # the input function always returns a string

if unit.upper() == "K":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("done")

secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break

else:
    print("You lose!")

My car program works but isn't refined
help = input("..")
while help:
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit _to exit")
    break
start = True
stop = True
quits = True
if start or stop or quits:
    print(input("."))
    print("car started ...Ready to go !")
    print(input(".."))
    print("car stopped")
    print(input(".."))
    print("quits")
# Chatgpt refined it
while True:
    user_input = input("Enter a command (start/stop/help/quit): ").lower()

    if user_input == "start":
        print("Car started... Ready to go!")
    elif user_input == "stop":
        print("Car stopped.")
    elif user_input == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif user_input == "quit":
        print("Quitting the program.")
        break
    else:
        print("Invalid command. Please enter start, stop, help, or quit.")"""
"""
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car start")
    elif command == "stop":
        if not started:
            print("car is already stop")
        else:
            started = False
            print("car stop")
    elif command == "help":
        print('''
start- to start the car
stop  - to stop the car
quit - to quit ''')

    elif command == "quit":
        break
    else:
        print("Sorry") """
