rows = 6

for i in range(1, rows + 1):
    for j in range(rows, i, -1):
        print(" ", end="")

    for k in range(i, 0, -1):
        print(k, end=" ")

    print()

rows = 6

for i in range(rows, 0, -1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

rows = 6

for i in range(1, rows + 1):

    for j in range(rows, i, -1):
        print(" ", end="")

    for k in range(1, 2 * i):
        print("*", end="")

    print()