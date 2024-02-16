import datetime

# User data and credentials
users = {'ahmet': {'password': '1234', 'attempts': 0, 'blocked': False},
         'zeynep': {'password': '4444', 'attempts': 0, 'blocked': False},
         'admin': {'password': 'qwerty', 'attempts': 0, 'blocked': False}}

# Products inventory
inventory = {'Asparagus': {'stock': 10, 'price': 5},
             'Broccoli': {'stock': 15, 'price': 6},
             'Carrots': {'stock': 18, 'price': 7},
             'Apples': {'stock': 20, 'price': 5},
             'Banana': {'stock': 10, 'price': 8},
             'Berries': {'stock': 30, 'price': 3},
             'Eggs': {'stock': 50, 'price': 2},
             'Mixed fruit juice': {'stock': 0, 'price': 8},
             'Fish Sticks': {'stock': 25, 'price': 12},
             'Ice Cream': {'stock': 32, 'price': 6},
             'Apple Juice': {'stock': 40, 'price': 7},
             'Orange Juice': {'stock': 30, 'price': 8},
             'Grape Juice': {'stock': 10, 'price': 9}}

# User's shopping basket
basket = {}


def authenticate_user(usernames, passwords):
    user_data = users.get(usernames.lower())
    if user_data and not user_data['blocked'] and user_data['password'] == passwords.lower():
        user_data['attempts'] = 0
        print("Successfully logged in!")
        return True
    elif user_data and user_data['blocked']:
        print("Your account is currently blocked. Please contact the administrator.")
        return False
    elif user_data:
        user_data['attempts'] += 1
        print("Your user name and/or password is not correct. Please try again!")

        if user_data['attempts'] == 3:
            if usernames.lower() == 'admin':
                user_data['attempts'] = 0  # Reset attempts for the admin
                print("Admin account cannot be blocked.")
            else:
                user_data['blocked'] = True
                print(f"Your account has been blocked. Please contact the administrator.")
            return False
    return False


def activate_user_account():
    to_activate_user = input("Enter the username to activate: ")
    if to_activate_user in users and users[to_activate_user]['blocked']:
        users[to_activate_user]['blocked'] = False  # Activates a user account by unblocking it.
        print(f"{to_activate_user}'s account has been activated.")
    else:
        print("Invalid username or the account is not blocked.")


def deactivate_user_account():
    to_deactivate_user = input("Enter the username to deactivate: ")
    if to_deactivate_user in users and not users[to_deactivate_user]['blocked']:
        users[to_deactivate_user]['blocked'] = True  # Deactivates a user account by blocking it.
        print(f"{to_deactivate_user}'s account has been deactivated.")
    else:
        print("Invalid username or the account is already blocked.")


def add_user():  # Add a new user to the users dictionary.
    new_username = input("Enter the new username: ")
    if new_username not in users:  # Check if the username doesn't exist in the users dictionary
        new_password = input("Enter the new password: ")
        users[new_username] = {'password': new_password, 'attempts': 0, 'blocked': False}
        print(f"User {new_username} has been added.")
    else:
        print("Username already exists. Please choose another username.")


def remove_user():
    to_remove_user = input("Enter the username to remove: ")
    if to_remove_user in users:
        del users[to_remove_user]  # Removes a user from the users dictionary.
        print(f"User {to_remove_user} has been removed.")
    else:
        print("Invalid username.")


def admin_menu():  # Displays the admin menu and handles admin choices.
    while True:
        print("Welcome, admin! Please choose one of the following options by entering the corresponding menu number.")
        print("1. Activate User Account")
        print("2. Deactivate User Account")
        print("3. Add User")
        print("4. Remove User")
        print("5. Logout")
        print("6. Exit")

        try:
            admin_choice = int(input("Your Choice: "))
        except ValueError:
            print("Invalid input. Please provide a valid menu number.")
            continue

        if admin_choice == 1:
            activate_user_account()
        elif admin_choice == 2:
            deactivate_user_account()
        elif admin_choice == 3:
            add_user()
        elif admin_choice == 4:
            remove_user()
        elif admin_choice == 5:
            break  # Logout
        elif admin_choice == 6:
            exit()  # Exit the program
        else:
            print("Invalid menu entry. Please provide a valid menu number.")


def get_current_date_and_time():
    now = datetime.datetime.now()  # Returns the current date and time in the format: "YYYY/MM/DD HH:MM"
    return now.strftime("%Y/%m/%d %H:%M")  # str: Current date and time formatted as a string.


def search_product():  # Searches for products in the inventory based on user input.
    search_for_term = input("What are you searching for? ").lower()
    matching_items = [(name, details['price']) for name, details in inventory.items()
                      if search_for_term in name.lower() and details['stock'] > 0]
    # Returns a list of matching items (name, price) if found; otherwise, prints a message and returns None.
    if not matching_items:
        print("Your search did not match any items. Please try something else.")
        return None

    print(f"Found {len(matching_items)} similar items:")
    for i, (name, price) in enumerate(matching_items, start=1):
        print(f"{i}.{name} {price}$")

    return matching_items


def update_basket():
    matching_items = search_product()  # Calls the search_product function to find matching items based on user input.
    if matching_items:
        try:
            # asks the user to select an item to add to the basket.
            choice = int(input("Please select which item you want to add to your basket (Enter 0 for the main menu): "))
        except ValueError:
            print("Invalid input. Please enter a valid item number.")
            return

        if choice == 0:
            return
        # If matching items are found, prompts the user to select an item to add to the basket.
        elif 1 <= choice <= len(matching_items):
            selected_item = matching_items[choice - 1]
            item_name, item_price = selected_item[0], selected_item[1]
            try:
                # Asks for the amount to add to the basket.
                amount = int(input(f"Adding {item_name}. Enter Amount: "))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
                return

            # Checks if the requested amount is over the stock amount.
            while amount > inventory[item_name]['stock']:
                print(f"Sorry! The requested amount exceeds the stock amount for {item_name}.")
                try:
                    amount = int(input("Please enter a different amount (Enter 0 to go back to the main menu): "))
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
                    return

                if amount == 0:
                    return

            if amount > 0:
                # Update the inventory stock in real-time
                inventory[item_name]['stock'] -= amount

                if item_name in basket:
                    basket[item_name]['amount'] += amount
                else:
                    basket[item_name] = {'price': item_price, 'amount': amount}

                print(f"Added {item_name} into your Basket. Going back to the main menu...")

                # Notify that the basket has been modified
                print("Your basket now contains:")
                display_basket()
        else:
            print("Invalid choice. Please provide a valid item number.")


def display_basket():  # Displays the contents of the basket and calculates the total price
    total_price = 0  # Initialize the total price variable
    if not basket:  # If the basket is empty, it prints a message indicating that.
        print("Your basket is empty. Total 0$")
    else:
        print("Your basket contains:")
        # Goes through items in the basket and displays details for each item
        for i, (item_name, details) in enumerate(basket.items(), start=1):
            item_price, amount = details['price'], details['amount']
            total_item_price = item_price * amount
            total_price += total_item_price
            print(f"{i}.{item_name} price={item_price}$ amount={amount} total={total_item_price}$")

        print(f"Total {total_price}$")

    return total_price


def basket_submenu():
    while True:
        print("Please Choose an option:")
        print("1. Update amount")
        print("2. Remove an item")
        print("3. Check out")
        print("4. Go back to the main menu")

        selection = input("Your selection: ")

        if selection == '1':
            update_basket_amount()
        elif selection == '2':
            remove_item_from_basket()
        elif selection == '3':
            checkout()
        elif selection == '4':
            return  # Go back to the main menu
        else:
            print("Invalid selection. Please provide a valid option.")


def checkout():
    total_price = display_basket()
    if total_price > 0:
        print("Processing your receipt...")
        receipt_lines = []  # initialize an empty list to store lines for the receipt
        # goes through items in the basket to generate receipt lines
        for item_name, details in basket.items():
            item_price, amount = details['price'], details['amount']
            total_item_price = item_price * amount
            # Create a receipt line for each item with its details
            receipt_lines.append(f"{item_name} {item_price}$ amount={amount} total={total_item_price}$")

            # Decrease the stock of the item by the purchased amount
            inventory[item_name]['stock'] -= amount

        receipt_lines.append(f"Total {total_price}$")  # Add a total line to the receipt
        receipt_lines.append(f"Date: {get_current_date_and_time()}")  # Add the date to the receipt

        # Display the receipt
        print("\n******* Medipol Online Market ********")
        print("**************************************")
        for line in receipt_lines:
            print(line)
        print("Thank You for using our Market!")

        # Clear the basket after checkout
        basket.clear()
        print("Your basket has been cleared.")


def main_menu(user_name):  # Displays the main menu for the logged-in user and handles user input.
    while True:
        print(
            f"Welcome, {user_name}! Please choose one of the following options by "
            f"entering the corresponding menu number.")
        print("Please choose one of the following services:")
        print("1. Search for a product")
        print("2. See Basket")
        print("3. Check Out")
        print("4. Logout")
        print("5. Exit")

        choice = input("Your Choice: ")

        if choice == '1':
            update_basket()
        elif choice == '2':
            display_basket()  # Display basket contents
            basket_submenu()  # Direct to basket submenu
        elif choice == '3':
            checkout()
        elif choice == '4':
            return  # Logout
        elif choice == '5':
            exit()  # Exit the program
        else:
            print("Invalid menu entry. Please provide a valid menu number.")


def update_basket_amount():
    display_basket()  # Display the current items in the basket

    try:
        item_number = int(input("Please select which item to change its amount: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a valid item number.")
        return

    # Check if the selected item number is within the valid range
    if 0 <= item_number < len(basket):
        item_name = list(basket.keys())[item_number]  # Get the name of the selected item
        try:
            new_amount = int(input("Please type the new amount: "))  # Prompt user for a new amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if new_amount <= inventory[item_name]['stock']:  # Check if the new amount is within the stock limit
            basket[item_name]['amount'] = new_amount  # Update the basket with the new amount
            display_basket()  # Display the updated basket
        else:
            print("Sorry! The amount exceeds the limit. Please try again with a smaller amount.")
    else:
        print("Invalid item number. Please provide a valid item number.")


def remove_item_from_basket():
    display_basket()  # Display the current items in the basket
    try:
        item_number = int(input("Please select which item to remove: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a valid item number.")
        return

    # Check if the selected item number is within the valid range
    if 0 <= item_number < len(basket):
        item_name = list(basket.keys())[item_number]  # Get the name of the selected item
        del basket[item_name]  # Remove the selected item from the basket
        print(f"{item_name} has been removed from your basket.")
        display_basket()
    else:
        print("Invalid item number. Please provide a valid item number.")


# Main program loop
while True:
    print("****Welcome to Medipol Online Market****")

    # Prompt the user for login credentials
    username, password = input("Please log in by providing your user credentials:\nUser Name: "), input("Password: ")

    if username.lower() == 'admin' and authenticate_user(username, password):
        # Admin login successful, redirect to admin menu
        admin_menu()
    elif authenticate_user(username, password):
        # Regular user login successful, redirect to main menu
        main_menu(username)
    else:
        continue
