"""class Rectangle:
    def __init__(self, length, width):
        self.length = length

        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()"""

"""class Student:

    def __init__(self, name, grade):

        self.name = name

        self.grade = grade

    def display_info(self):

        print("Name:", self.name)

        print("Grade:", self.grade)

student = Student("John Doe", 10)

student.display_info()"""


class BankAccount:

    def __init__(self, account_number, balance):

        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if self.balance >= amount:

            self.balance -= amount

        else:

            print("Insufficient funds. Withdrawal denied.")

    def display_balance(self):

        print("Account Number:", self.account_number)

        print("Balance:", self.balance)


account = BankAccount("1234567890", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(2000)
account.display_balance()
