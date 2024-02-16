"""def average_first_exam(exam_dict):
    if not exam_dict:
        return 0

    first_exam_grades = [data["exam1"] for data in exam_dict.values()]
    average_first_exam = sum(first_exam_grades) / len(first_exam_grades)

    return average_first_exam


exam_dict = {
    "john": {"exam1": 40, "exam2": 70},
    "murat": {"exam1": 20, "exam2": 30},
    "faruk": {"exam1": 35, "exam2": 55},
    "sow": {"exam1": 80, "exam2": 90},
}

result = average_first_exam(exam_dict)
print("average of the first grades:", result)"""

"""
def compress_string(s):
    if not s:
        return ""

    compressed = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed += str(count) + current_char
            current_char = s[1]
            count = 1
    compressed += str(count) + current_char

    return compressed


# Prompt user for input
user_input = input("Enter a string: ")
result = compress_string(user_input)

print("Compressed string:", result)"""



