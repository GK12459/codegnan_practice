import random

print("\n-------GUESS THE NUMBER (1-100)-------\n")
random_number = random.randint(1,100)

def game_logic():
    count = 0
    while (True):

        try:
            guess_number = int(input("Your guess? "))
        except(ValueError):
            print("Value Error: Invalid input.\n")
            continue

        count += 1
        print("Result:")
        match (guess_number):
            case _ if (guess_number < random_number):
                print("Your guess is less than the actual number!")
                print("Guess again...\n")
                
            case _ if (guess_number > random_number):
                print("Your guess is more than the actual number!")
                print("Guess again...\n")
                
            case _ if (guess_number == random_number):
                print("Hurray! Your guess is correct!")
                break
    print(f"\nYou've taken {count} attempts.\n")

game_logic()