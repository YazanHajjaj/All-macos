def digits(num):
    return [int(digit) for digit in str(num)]

input = 182389
result_list = digits(input)
print(result_list)


def stats(list):

    sum_val = sum(list)
    mean_val = sum_val / len(list)

    if len(list) % 2 == 0:

        median_val = (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
    else:

        median_val = list[len(list) // 2]

    print("Sum:", sum_val)
    print("Mean:", mean_val)
    print("Median:", median_val)

numbers = [1, 2, 3, 4]
stats(numbers)
