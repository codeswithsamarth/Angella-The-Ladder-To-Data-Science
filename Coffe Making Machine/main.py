water = 1000
milk = 1000
coffe = 1000


def Check_resources():
    print(f"Resources:\nwater = {water}\nMilk = {milk}\nCoffe = {coffe} \nMilk = {milk}")


MENU = [
    ["espresso",50,0,18,100],
    ["latte",200,150,24,150],
    ["cappuccino",250,100,24,180],
    ["mocha", 200, 100, 20, 170],
    ["americano", 150, 0, 18, 130],
    ["flat white", 180, 150, 20, 160],
    ["macchiato", 100, 50, 18, 140],
    ["ristretto", 30, 0, 15, 110],
    ["affogato", 60, 50, 20, 190],
    ["cortado", 100, 100, 20, 150],
    ["irish coffee", 150, 50, 22, 200],
    ["turkish coffee", 80, 0, 25, 160],
    ["frappe", 120, 100, 22, 175],
    ["vienna coffee", 200, 100, 24, 185],
    ["dalgona", 150, 120, 20, 180]

]

def Show_Menu():
    print("---Menu----")
    num = 0
    for i in MENU:
        num+=1
        print(f"{num}. {i[0]} Price = {i[4]}")


def deduct():
    resources_remain = []
    print("Enter The Water Milk Coffe\n")
    for i in range(0,3):
        value = int(input("Enter The Values\n"))
        resources_remain.append(abs(value))
        if (i == 0):
            if (value > water):
                print("Insufficient Resources")
                break
            else:
                print("Adding Resource Water ")
                value-= water

        if (i == 1):
            if (value > milk):
                print("Insufficient Resources")
                break
            else:
                print("Adding Resource Milk")
                value-= milk
        if (i == 2):
            if (value > coffe):
                print("Insufficient Resources")
                break
            else:
                print("Adding Resource Coffe")
                value-= coffe
    print(resources_remain)

def make_payment(price):
    total = 0
    total += int(input("Enter The Amount 🪙:"))
    if total < price:
        print(f"Insufficient amount. You entered {total}, required is {price}. Refunding money.")
        return False
    elif total > price:
        change = total - price
        print(f"Transaction Successful. Refunding Amount {change}")
        return True
    else:
        print("Transaction Successful. No change to refund.")
        return True

def main():
    run = 1
    while run!=0:
        Show_Menu()
        choice = int(input("Enter The Coffe 🥤:\n"))
        choice_struct = [f"Coffe Structure","coffe name","water","milk","coffe","price"]
        print(choice_struct)
        if choice > 0:
            print(f"{MENU[choice-1]}")
            print("Please Make Payment....")
            if not make_payment(MENU[choice-1][4]):
                print("Insufficient Payment Refunding....")
                break

        choice_reso = input("Enter Yes To Add own Resource:\n").lower()
        if choice_reso == "yes":
            Check_resources()
            deduct()

            print("The Resources Are Added Successfully")
            print("Order Of Coffe Successful 🥤")
            run = 0
            break
        else:
            print("Order Of Coffe Successful 🥤")
            print("Thanks For Visiting Our Python 🥤Coffe Machine")
            run = 0
            break
main()