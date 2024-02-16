# for loops
"""
for i in ["python", "yuan", "shin"]: # brackets are used for lists
    print(i)

for i2 in range(10): # the number written isn't included in
    print(i2)

for i3 in range(5, 10): # 5 is included, 10 is not included
    print(i3)

for i4 in range(5, 10, 2): # two take 2 steps every time 5, 7, 9
    print(i4)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f "total: {total}") """

# nested loops
"""
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})

numbers = [2, 2, 2, 2, 6]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "X"
    print(output)"""

# lists
"""
name = ["john", "bob", "mosh "]
name[0] = "jon" # it will update the the name in the index
print(name[-1:])  # an index in a list gives you the item in it the related one where 0 gives the first and -1 the last
''' a column without a number gives everything after the specified first num ,when a number is included the 
it will not be included  '''


numbers = [45, 44, 2, 3, 4, 5, 6]
max = numbers[0]
for number in numbers:
    if number > max:
        max =number
print(max) """

#  2d lists
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20 #  modifies the list 0 is the first list and 1 is the index in it
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item) """

# list methods
"""
# numbers = [5, 2, 1, 7, 4, 4]
# numbers.append(20)  #  appends adds the value you want at the end of the list
# numbers.remove(5) # self-explained
# numbers.clear() # it clears the list
# numbers.pop()  # removes the last item in the list
# numbers.insert(0, 4) # insert takes the index u need to put the value first then the value u want
# numbers.sort()  # sort the list
# numbers.reverse()  # it gives you it in a reverse order
# numbers2 = numbers.copy() # this doesnt affect the second list changes made will only happen to the first one
# numbers.append(4)
# print(numbers.index(5))  # shows the index where the value first appears
# print(50 in numbers)  # it gives u true or false
# print(numbers.count(4)) # it gives u how many values are there
# print(numbers)

numbers = [1, 1, 1, 3, 4, 5, 1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique) """""

# tuples
"""
# unlike list they are not changeable
numbers = (1, 2 ,3) # they parenthesis
print(numbers[0]) """

# un-packing
"""
# it work with both tuples and lists
coordinates = (1, 2, 3)


x = coordinates[0]
y = coordinates[1] # first way
z = coordinates[2]

x,y,z = coordinates # second way to make it shorter print x if you forget
print(x)"""

# dictionaries
"""
# each key should be unique means only one can be used its also case-sensitive
customer = {
    "name": "yazan hajjaj",
    "age": 19,
    "is_verified": True
}
customer["birthdate"] = "yn hajjaj"
print(customer["birthdate"])
# print(customer.get("birthdate,", "feb 18 2004"))
# get is used to by-base the error value in this case, we will get none since the value is not defined 


phone = (input("phone:"))
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}
output = ""
for char in phone:
    output += digits_mapping.get(char, "!")
print(output)"""""

# emoji converter
"""
message = input(">")
words = message.split(' ')
print(words)
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔"

}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)"""