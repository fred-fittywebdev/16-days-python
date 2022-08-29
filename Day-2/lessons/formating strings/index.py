# String formating
# 1 - Format. -> print("My car is {} and its plate is {}".format(car_color, plate)) -> Not more readable. 
# 2 - Literal strings -> print(f"My car is {car_color} and its plate is {plate}") -> More readable.

# Before python 3 all dev use format method so it is interesting to know it.

x = 10
y = 5

# concatenation
print("My numbers are " + str(x) + " and " + str(y))
# format
print("My numbers are {} and {}".format(x, y))
# f strings
print(f"My numbers are {x} and {y}")