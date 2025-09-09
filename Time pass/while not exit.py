# run = 1
# sum = 0
# while run:
#     num = input("Enter The Number\n")
#     if num.isnumeric():
#         num2 = int(num)
#         sum += num2
#     if num == "exit":
#         print(sum)
#         run = 0
#         break
#
import random
computer_score = []
user_score = []
while True:
    try:
        random_int = random.randint(1,100)
        num = int(input("Enter The Number\n"))
        if num > 100 or num < 1:
            print("Invalid Number Number Must between 1-100")
            break
        if random_int > num:
            print("Computer wins")
            computer_score.append(1)
        elif random_int < num:
            user_score.append(1)
            print("You Win 🎉")

    except (ValueError,TypeError) as e:
        print(f"Computer Score = {sum(computer_score)}")
        print(f"User Score = {sum(user_score)}")
        if sum(computer_score) > sum(user_score):
            print(f"Computer Wins Score = {sum(computer_score)}")
            break
        elif sum(user_score) > sum(computer_score):
            print(f"User Wins Score = {sum({user_score})}")
            break
        import random

        computer_score = []
        user_score = []
        while True:
            try:
                random_int = random.randint(1, 100)
                num = int(input("Enter The Number\n"))
                if random_int > 100 or random_int < 1:
                    print("Invalid Number Number Must between 1-100")
                    break
                if random_int > num:
                    print("Computer wins")
                    computer_score.append(1)
                elif random_int < num:
                    user_score.append(1)
                    print("You Win 🎉")

            except ValueError or TypeError or ValueError as e:
                print(f"Computer Score = {sum(computer_score)}")
                print(f"User Score = {sum(user_score)}")
                if computer_score > user_score:
                    print(f"Computer Wins Score = {sum(computer_score)}")
                    break
                elif user_score > computer_score:
                    print(f"User Wins Score = {sum({user_score})}")
                    break
                else:
                    print("Its A Tie")
                break