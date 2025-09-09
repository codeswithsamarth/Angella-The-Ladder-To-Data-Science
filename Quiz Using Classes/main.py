import random
from allq import questions,programming_questions,film_questions,history_questions,mythology_questions,cartoon_questions,cs_questions
import webbrowser
import sys
def open_dev_manual():
    webbrowser.open("developermanual.tiiny.site")

def open_user_manual():
    webbrowser.open("usermanual.tiiny.site")


def survey_input():
    choice = input("Enter The choice \n1.User Survey \n2.Developer Survey\n")
    if choice == "1":
        webbrowser.open("https://www.surveymonkey.com/r/JGW2CRR")
        print("You can Also Contact Me On 📧 samarthp2727@gmail.com")
        sys.exit()
    elif choice == "2":
        webbrowser.open("https://www.surveymonkey.com/r/2HCYY7G")
        print("You can Also Contact Me On 📧 samarthp2727@gmail.com")
        sys.exit()
    else:
        pass
def manual_input():
    choices = input("Enter The Choice\n1.User Manual\n2.Developer Manual\n")
    if choices == "1":
        open_user_manual()
        sys.exit()
    elif choices == "2":
        open_dev_manual()
        sys.exit()
    else:
        sys.exit("Invalid Choice")

class TrueOrFalse:
    def __init__(self):
        self.manual()
        choice = int(input("Enter The Choice\n"))
        match choice:
            case 1:
                manual_input()
            case 2:
                pass
            case 3:
                survey_input()
            case _:
                print("Invalid choice")
        self.show()
        choice = int(input("Enter The Choice\n"))
        match choice:
            case 1:
                self.question = questions
            case 2:
                self.question = cs_questions
            case 3:
                self.question = history_questions
            case 4:
                self.question = mythology_questions
            case 5:
                self.question = cartoon_questions
            case 6:
                self.question = programming_questions
            case 7:
                self.question = film_questions
            case _:
                print("Invalid Choice")
        self.random_list = random.randint(0, 8)

    def show(self):
        print("Choices Of Question\n".rstrip())
        print("1.Gk\n2.Computer Science\n3.Indian History\n4.Indian Mythology\n5.Cartoon Question\n6.Programming Question".rstrip())

    def manual(self):
        print("1.Manual")
        print("2.Continue Game")
        print("3.Response")

    def start(self):
        score = 0
        run = 1
        i = 0
        print("----Welcome To True False Game----".center(100))
        random.shuffle(self.question)
        while run:
            i += 1
            for questions in self.question:
                if score == 50:
                    print("Your all answer is correct 🎉")
                    run = 0
                    break
                else:
                    print(questions[0])
                    choice = input("Enter True Or False:\n".lower())
                    if choice.lower() == questions[1].lower():
                        score += 1
                        print(f"Answer Is Correct Score = {score}")
                    elif choice != questions[1]:
                        print("Answer Is Wrong")
                        run = 0
                        break


if __name__ == "__main__":
    game = TrueOrFalse()
    game.start()