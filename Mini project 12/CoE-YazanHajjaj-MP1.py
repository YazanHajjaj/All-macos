import random


def health_bar(name, health):  # Function to show health bar
    print(f"{name}\nHP[{health}]:{'I' * (health // 2)}")


def get_valid_name(player):  # Function to get hero's name
    hero_names = []
    for i in range(2):
        while True:
            hero_name = input(f"--- {player[i]}'s Hero --- \nPlease type your hero's name: ")
            if hero_name and hero_name not in hero_names:
                hero_names.append(hero_name)
                break
            else:
                print(f"{hero_name} the name is taken or invalid, please choose another name!")
    return hero_names


def initiate_attack(attacking, defending, player_hp):  # Function for preforming the attack
    attack_magnitude = input_attack_magnitude(attacking)
    success_times = random.randint(1, 100)

    if success_times > (100 - attack_magnitude):
        print(f"{attacking} missed the attack!")
    else:
        print(f"{attacking} hits {defending} with {attack_magnitude} damage!")
        player_hp[defending] -= attack_magnitude


def input_attack_magnitude(attacker):  # Function for the attacker to input the attack magnitude
    while True:
        try:
            attack_magnitude = int(
                input(f"----- {attacker}'s Attacks !! -----\nChoose your attack magnitude between 1 and 50: "))
            if 1 <= attack_magnitude <= 50:
                return attack_magnitude
            else:
                print("The attack magnitude must be between 1 and 50. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main_game():  # Function that defines the main entry point of the game
    print("Welcome to the Turn-Based Hero Game!")


while True:
    players = ["Player1", "Player2"] # Coin toss to choose first player
    random.shuffle(players)
    current_player = players[0]
    hero_names = get_valid_name(players)

    print(f"\nCoin toss result: {current_player} starts first!\n")
    player_health = {hero_names[0]: 100, hero_names[1]: 100}

    while True:
        second_player = hero_names[1] if current_player == hero_names[0] else hero_names[0]
        health_bar(hero_names[0], player_health[hero_names[0]])
        health_bar(hero_names[1], player_health[hero_names[1]])

        initiate_attack(current_player, second_player, player_health)

        if player_health[second_player] <= 0: # it ends the game when one player reaches 0
            print(f"#### {current_player} is the Winner! ####")
            break

        current_player = second_player

    another_game = input("Would you like to play another round?  (Yes or No): ")
    if another_game.lower() != 'yes':
        print("Thanks for playing! See you again!")
        break

if __name__ == "__main__":
    main_game()

# w3schools and book were used as a reference
