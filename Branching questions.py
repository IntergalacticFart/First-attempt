kilowatt_hours = int(input("enter the number of hours on your electric bill: "))
bill = ""
if kilowatt_hours <= 1000:
    bill = kilowatt_hours * 0.07633
elif kilowatt_hours > 1000:
    bill = (1000 * 0.07633) + (kilowatt_hours - 1000) * 0.09259
print("your bill cost is", bill)