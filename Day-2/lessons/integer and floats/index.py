# Numeric values, integers and floats
my_number = 1
print(my_number)
print(type(my_number)) # <class 'int'>

my_add = 1 + 6
print(my_add)
print(type(my_add)) # <class 'int >
print(my_number + my_add)

my_float_number = 5.8
print(my_float_number)
print(type(my_float_number)) # <class 'float'>

age = input("Tell me your age: ")
print("Your age is " + age)

# new_age = 1 + age # <- here we have an int (1) and a string (age) so it could not work
# print(type(age)) #  <class 'str' >
# print("yOU ARE GOING TO BE: " + new_age) # <TypeError: unsupported operand type(s) for +: 'int' and 'str' The value of an input is always a string !

