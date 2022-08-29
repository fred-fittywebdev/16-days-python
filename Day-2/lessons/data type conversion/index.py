# type conversion -> casting implicit or explicits
# Implicits -> Python converts the data type to another data type automatically. In this process the user must do nothing.
# Explicits -> We ask python withh code to convert one data type to another ( for the input for example if we want a int or a float )

num_1 = 20
num_2 = 3.45

num_1 = num_1 + num_2 # here python will automatically convert num_1 into a float IMPLICIT

print(type(num_1)) # <class 'int'>
print(type(num_2)) # <class 'float'>

float_num = 5.10              # Results for the code above.
                              # 5.1
                              #<class 'float'>
                              #5
                              #<class 'int'>
print(float_num)
print(type(float_num)) 

num_3 = int(float_num)
print(num_3)
print(type(num_3)) 

age = input("Tell me your age: ")
print("Your age is " + age)

# new_age = 1 + age # <- here we have an int (1) and a string (age) so it could not work
# print(type(age)) #  <class 'str' >
# print("yOU ARE GOING TO BE: " + new_age) # <TypeError: unsupported operand type(s) for +: 'int' and 'str' The value of an input is always a string !

new_age = 1 + int(age) 
print(type(age)) 
print(new_age)
print("yOU ARE GOING TO BE: " + str(new_age))

