def values(data_vector, replacement_values):

    result = []
    replacement_index = 0

    for value in data_vector:
        if value == "NA":

            result.append(replacement_values[replacement_index])
            replacement_index += 1
        else:

            result.append(value)

    return result

data_vector = [1, "NA", 3, "NA", 5]
replacement_values = [2, 4]

result = values(data_vector, replacement_values)
print(result)
