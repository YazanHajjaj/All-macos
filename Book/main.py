import random


def display_health(player, health):
    print(f"{player}\nHP[{health}]: {'I' * (health // 2)}")


def get_hero_names(player):
    hero_names = []
    for _ in range(2):
        while True:
            hero_name = input(f"----- {player}'s Hero -----\nPlease type your hero's name: ")
            if hero_name and hero_name not in hero_names:
                hero_names.append(hero_name)
                break
            else:
                print(f"{hero_name} is taken or invalid, please choose another name!")
    return hero_names


def perform_attack(attacker, defender, player_health):
    attack_magnitude = int(input(f"----- {attacker}'s Attacks !! -----\n"
                                 f"Choose your attack magnitude between 1 and 50: "))
    if attack_magnitude < 1 or attack_magnitude > 50:
        print("The attack magnitude must be between 1 and 50. Try again.")
        return False

    success_rate = random.randint(1, 100)
    if success_rate > (100 - attack_magnitude):
        print(f"{attacker} missed the attack!")
    else:
        print(f"{attacker} hits {attack_magnitude} damage!!!")
        player_health[defender] -= attack_magnitude

    return True


def main():
    print("Welcome to the Turn-Based Hero Battle Game!")

    while True:
        players = ["Player 1", "Player 2"]
        random.shuffle(players)
        current_player = players[0]

        hero_names = get_hero_names(current_player)

        print(f"\nCoin toss result: {current_player} starts first!\n")
        player_health = {hero_names[0]: 100, hero_names[1]: 100}

        while True:
            second_player = hero_names[1] if current_player == hero_names[0] else hero_names[0]
            display_health(hero_names[0], player_health[hero_names[0]])
            display_health(hero_names[1], player_health[hero_names[1]])

            if not perform_attack(current_player, second_player, player_health):
                continue

            if player_health[second_player] <= 0:
                print("\n####################################################################")
                print(f"######################### {current_player} Wins !!! #########################")
                print("####################################################################\n")
                break

            current_player = second_player

        play_again = input("Do you want to play another round? (Yes or No): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! See you again!")
            break


if __name__ == "__main__":
    main()
