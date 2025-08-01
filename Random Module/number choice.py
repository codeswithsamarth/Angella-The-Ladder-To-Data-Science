import random

def number_choice():
        try:
            number = int(input("Enter The Number:"))
            computer_choice = random.randint(1,100)
            if number > 100:
                print("Invalid Choice Try Between 1-100!")

            if number <= 100 and number >= 1:
                print(f"Your choice is {number} and computer choice is {computer_choice}")
                if computer_choice > number:
                    print("Computer Wins")

                elif computer_choice < number:
                    print("You Win!")

                elif computer_choice == number:
                    print("Tie")

        except ValueError:
            print("Only Number as allowed")
        except TypeError:
            print("Type Error")

        except EOFError:
            print("The Execution Successfully completed")

if __name__ == "__main__":
    number_choice()

