def generalize(category, flights_dict):
    result_dict = {}  # Creates an empty dictionary so you can store the result

    for key, value in flights_dict.items():  # Repeats through key-value pairs in the input dictionary

        if category == "airport":  # Determines the categories value based on the parameter
            category_value = key[0]
        elif category == "city":
            category_value = key[1]
        elif category == "status":
            category_value = key[2]
        else:
            # Raise a ValueError for unsupported categories
            raise ValueError("Invalid category. Supported categories are 'airport', 'city', or 'status'.")

        result_dict[category_value] = result_dict.get(category_value, 0) + value
        # Update the result dictionary by adding the current value to the existing value

    return result_dict  # Return the final result dictionary


sample_dictionary = {
    ("IST", "Istanbul", "domestic"): 50000,
    ("IST", "Istanbul", "international"): 85000,
    ("ADB", "Izmir", "domestic"): 20000,
    ("ADB", "Izmir", "international"): 0,
}

result = generalize("city", sample_dictionary)
print(result)


def main():
    input_count = {}     # Dictionary to store the count of each input

    while True:
        user_input = input("Enter a line of text: ") # Get input from the user

        # Checks if you have put the input more than three times
        input_count[user_input] = input_count.get(user_input, 0) + 1

        # If you entered the input  more than three times, notifies you and exits the loop
        if input_count[user_input] > 3:
            print(f"You have entered '{user_input}' more than three times. Exiting.")
            break


if __name__ == "__main__":
    main()
1