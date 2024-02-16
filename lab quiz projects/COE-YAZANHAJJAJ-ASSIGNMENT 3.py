from collections import Counter


# Question 1 Letter a
def repeat_letters(i, n):
    results = ''  # make an empty string to store the result

    for letter in i:
        results += letter * n  # Repeat each letter 'n' times

    print(results)


repeat_letters("Yazan", 3)


# Letter B
def find_index(word, letter):
    first_occurrence = word.find(letter)  # Find the first occurrence of the letter

    second_occurrence = word.find(letter, first_occurrence + 1)

    return second_occurrence


result = find_index("goodbye", "o")
print(result)


# Letter c

def list_unique(in_str):
    unique_chars = set()

    for char in in_str:
        # Add the character to the set
        unique_chars.add(char)

    # Converts the set to a list for it to maintain the order
    unique_chars_list = list(unique_chars)

    return unique_chars_list


result = list_unique("Yazan")
print(result)


# Letter D
def ngrams_list(in_str, n):
    # Check if the input string length is less than n
    if len(in_str) < n:
        raise ValueError("String length should be greater than or equal to n.")

    ngrams = [in_str[i:i + n]
              for i in range(len(in_str) - n + 1)]

    return ngrams


result = ngrams_list("How are you", 2)
print(result)


# Letter e

def avg_cgpa_by_major(student_dict, major):
    total_cgpa = 0
    count = 0
    #     Calculates the average CGPA for students with a specific major
    for student_id, info in student_dict.items():
        student_major, cgpa = info
        if student_major == major:
            total_cgpa += cgpa
            count += 1

    if count == 0:
        return 0  # Return 0 if no student with the specified major is found

    avg_cgpa = total_cgpa / count
    return avg_cgpa


student_dictionary = {41251: ['CoE', 2.5], 42509: ['EEE', 3.1], 41713: ['CoE', 1.9], 41101: ['CoE', 2.7]}
result = avg_cgpa_by_major(student_dictionary, "CoE")
print(result)


# Letter F

def search_dict(input_dict, number):
    for value in input_dict.values():
        if str(value) == str(number):  # Searches through dictionary values to check if a number appears.

            return True

    return False


d1 = {'Ahmet': 10, 'Zeynep': '5', 'Mehmet': '2'}
result = search_dict(d1, 5)
print(result)


# Letter G

def hist_a(in_str):
    hist_dict = {}
    #  Creates a dictionary mapping each character to its frequency in the given string.
    for char in in_str:
        if char in hist_dict:
            hist_dict[char] += 1
        else:
            hist_dict[char] = 1

    return hist_dict


result = hist_a("kara murat kim")
print(result)


# LETTER H
def hist_b(hist_a_result):
    hist_freq_dict = {}
    #     Creates a new dictionary mapping frequencies to letters.
    for char, freq in hist_a_result.items():
        if freq in hist_freq_dict:
            hist_freq_dict[freq].append(char)
        else:
            hist_freq_dict[freq] = [char]

    return hist_freq_dict


res = hist_a("kara murat kim")
result = hist_b(res)
print(result)


# LETTER I

def get_top_elements(in_str):
    # Finds the most common three letters in the given string.
    character_count = Counter(in_str)
    most_common_chars = character_count.most_common(3)
    most_common_chars = sorted(most_common_chars, key=lambda x: (x[1], x[0]))

    return most_common_chars


result = get_top_elements("programming")
print(f"Most common three letters are: {', '.join([char for char, _ in result])}")


# letter J

def compress_dict(input_str):
    # Compresses the strings that have long sequences of equal characters.
    compressed_str = ""
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            compressed_str += str(count) + input_str[i - 1]
            count = 1

    compressed_str += str(count) + input_str[-1]

    return compressed_str


result = compress_dict("aaaabbaaabbbbbbcccd")
print(result)

# School was used to look up some things
