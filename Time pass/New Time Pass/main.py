import random

computer_score = []
user_score = []

while True:
    try:
        random_int = random.randint(1, 100)
        num = int(input("Enter a number between 1 and 100:\n"))

        if num < 1 or num > 100:
            print("Invalid number. Must be between 1 and 100.")
            continue

        print(f"Computer chose: {random_int}")

        if random_int > num:
            print("Computer Won.")
            computer_score.append(1)
        elif random_int < num:
            print("You won This Round 🎉")
            user_score.append(1)
        else:
            print("It's a tie!")

    except (ValueError, TypeError):
        print("\nInvalid input or command received. Exiting the game.")
        print(f"Computer Score = {sum(computer_score)}")
        print(f"User Score = {sum(user_score)}")

        if sum(computer_score) > sum(user_score):
            print("Computer Wins Overall.")
        elif sum(user_score) > sum(computer_score):
            print("You Win Overall! 🎉")
        else:
            print("It's a Tie Overall!")
        break
