name = input("Hello, what is your name? ")
sales = float(input("What the amoount of your sale this month? "))

commission = sales * 13 / 100
commission_rounded = round(commission, 2)

print(f"{name} your commission this month is: {commission_rounded} €")