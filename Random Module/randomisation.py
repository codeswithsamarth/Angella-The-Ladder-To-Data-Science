import time

def time_total(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        total = (f"{end-start:.4f}")
        print(f"You Took this {total} Time For Executing this game")
    return wrapper


def response():
    print("Thanks For Your Response This Will Help us better For Improvement")
    username = input("Enter Username:\n")
    contents = input("Enter The Response:\n")
    with open("response.txt",'a') as f:
        f.write(f"{username}:"+contents+"\n")

import random

@time_total
def main():
    """
    About This is a function named randomisation which uses random module
    function randint to generate number between 1 to 10
    It takes the number as input
    it runs continuous until the input matches the number
    if number is greater its display message Too high!
    if number is lower it display too low
    if number is greater than 10 or less than 1 print number out of range
    the code is coded with some feature such as
    exception handling if user input anything instead of number it display message
    try to handle error
    """
    random_integer = random.randint(1,10)
    while True:
        try:
            choice = int(input("Guess the number:"))
            if choice == random_integer:
                print("The Guess is correct")
                break
            if choice > 10 or choice < 1:
                print("Out of range")

            elif choice < random_integer:
                print("Too Low!")

            elif choice > random_integer:
                print("Too High!")

        except ValueError:
            print("Only Number are allowed ")

def play_game():
    main()
    contents = input("Enter The Choice: \n1.Give Response About Function\n2.Exit\n")
    if contents == "1":
        response()
    else:
        print("Thanks For Visiting Our Project!")


if __name__ == "__main__":
    play_game()

