"""def create_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary


keys = ["a", "b", "c"]
values = [1, 2, 3]
result = create_dictionary(keys,values)
print(result)"""


"""def find_values_in_dicetionary(lst, dictionary):
    result = []
    for item in lst:
        if item in dictionary.values():
            result.append(item)
    return result


lst = [1, 2, 3, 4]
dictionary = {1: "apple", 2: "banana", 3: "orange", 4: "grape"}
result = find_values_in_dicetionary(lst, dictionary)
print(result)
"""

"""def search_number_in_dictionary(dictionary,number):
    for value in dictionary.values():
        if str(number) == str(value):
            return True
    return False

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4,}
number = 2
result = search_number_in_dictionary(dictionary,number)
print(result)"""


def reverse_sort_list(lst):
    return sorted(lst, reverse = True)

my_list = [5,2,8,1,9]
sorted_list = reverse_sort_list(my_list)
print(sorted_list)