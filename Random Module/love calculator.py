import random
def love_calculator(name1,name2):
    combined = (name1.strip()+name2.strip())
    random.seed(combined)
    love_percentage = random.randint(20,100)
    print("This is Calculator Which Counts The Love Percentage")
    print(f"The Total percentage = {love_percentage}")

    if love_percentage > 80:
        print("You two are made for each other! 💍")
    elif love_percentage > 50:
        print("There's definitely 🌹")
    elif love_percentage > 80:
        print("Could work, but needs effort! 🤔")
    else:
        print("umm.. maybe better as friend? 😂")

name1 = input("Enter Your Name:")
name2 = input("Enter their Name:")


love_calculator(name1,name2)
