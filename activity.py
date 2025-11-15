class VendingMachine:
    def __init__(self, beverage):
        self.beverage = beverage

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printMe(self):
        print(self.name, self.price)
        return self.name, self.price

lemonade = Beverage("Lemonade", 10)
iced_tea = Beverage("Iced Tea", 20)
orange_juice = Beverage("Orange Juice", 30)
hot_chocolate = Beverage("Hot Chocolate", 40)
strawberry_smoothie = Beverage("Strawberry Smoothie", 50)
cola = Beverage("Cola", 60)

beverages = {
    "Lemonade": lemonade,
    "Iced Tea": iced_tea,
    "Orange Juice": orange_juice,
    "Hot Chocolate": hot_chocolate,
    "Strawberry Smoothie": strawberry_smoothie,
    "Cola": cola,
}

vm = VendingMachine(beverages)
while True:
    print("Our beverages and prices:")
    print("Lemonade(10)")
    print("Iced Tea(20)")
    print("Orange Juice(30)")
    print("Hot Chocolate(40)")
    print("Strawberry Smoothie(50)")
    print("Cola(60)")

    while True:
        choice = input("Which beverage would you like to vending?\n")
        if choice in beverages:
            break
        else:
            print("Beverage does not exist! Please insert the correct beverage.\n")

    drink = beverages[choice]
    print("The price of", drink.name, "is", drink.price)

    money = int(input("How much money would you like to vending?\n"))
    if money < drink.price:
        print("Returning your money... Please insert at least", drink.price)
    else:
        print("You bought", drink.name, "Enjoy!")






   # if choice in beverages:
    #    drink = beverages[choice]
     #   print("The price of", drink.name, "is", drink.price)
      #  money = int(input("How much money would you like to vending?\n"))

       # if money < drink.price:
        #    money = input("Returning your money... Please insert the correct amount of money.\n")

        #else:
         #   print("You bought", drink.name,"Enjoy!")
    #else:
     #   input("Beverage does not exist! Please insert the correct beverage.\n")
