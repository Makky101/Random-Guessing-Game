import random

while True:
    print("====Guess the Number Game====")
    print()
    print("I'm thinking of a number (between 1 and 10) can you guess it?")
    print()
    print("You have 3 Tries")

    the_random_number = random.randint(1, 10)
    tries = 0
    max_tries = 3
    guessed_correctly = False

    while tries < max_tries:
        while True:
            try:
                guess = int(input("Guess the number: "))
                if 1 <= guess <= 10:
                    break
                else:
                    print("Invalid number. It should be between 1 and 10.")
            except ValueError:
                print("Please put in a number!!!")
        if guess == the_random_number:
            print("You are correct! I was thinking about", the_random_number)
            guessed_correctly = True
            break
        else:
            print("Wrong guess.")
            tries += 1

    if not guessed_correctly:
        print("Sorry! The number was", the_random_number)
        diff = abs(the_random_number - guess)
        if guess < the_random_number:
            print(f"You were {diff} digits below the number I was thinking about which was {the_random_number}")
        else:
            print(f"You were {diff} digits above the number I was thinking about which was {the_random_number}")

    retry = input("Do you want to play again? (yes/no): ").strip().lower()
    if retry == "no":
        break
