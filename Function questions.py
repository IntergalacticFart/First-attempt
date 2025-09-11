def area_of_circle(radius, pi):
    first_calculation = pi * radius ** 2
    return first_calculation
def total_due(money, tax):
    second_calculation = money + (money * tax/100)
    return second_calculation
def conversion(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
pi = 3.14
radius = (float(input("enter the radius of the circle: ")))
first_answer = area_of_circle(radius, pi)
print("the area of the circle is:", first_answer)
money = float(input("enter your amount of money: "))
tax = float(input("enter the tax rate percentage: "))
second_answer = total_due(money, tax)
print("the total due is:", second_answer)
fahrenheit = float(input("enter the temperature in fahrenheit: "))
third_answer = conversion(fahrenheit)
print("this is the temperature in fahrenheit: ", third_answer)
