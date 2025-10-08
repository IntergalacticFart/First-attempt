def menu(items):
    choice = 0
    while (choice !=5):
        index = 1
        for item in items:
            print("{0}. {1}".format(index, item))
            index += 1
        choice = int(input("Enter the number that represents your selection:"))
        print("You have selected:", items[choice - 1])
        if choice !=5:
            chosen_items.append(items[choice - 1])
            chosen_prices.append(price_of_items[choice - 1])


def total_value(price_of_items):
    total = 0
    for item in price_of_items:
        total += item
    return total


print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection")
items = ["Al Pastor", "Crazy Dave's Taco", "Tamales", "Beast Boy's Burrito", "Quit"]
price_of_items = [0.01, 50000000, 2, 3500000]
chosen_items = []
chosen_prices = []

menu(items)
total_value(chosen_prices)

print("This is the total list of foods you bought",chosen_items, "and this is the total price due", total_value(chosen_prices), "dollars")

