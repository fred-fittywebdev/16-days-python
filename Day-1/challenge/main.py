# Ask two questions to the user to find an original name for a beer and display it to the screnn.

# Question 1:
print("Welcome to this amazing Beer name generator ! Answer with ONE WORD to the following questions ans let the magic happen !")
question_one = input("Please choose a color. ").title()
question_two = input("Please choose a planet. ").title()

beer_name = question_one + " " + question_two

print(f"The beer brand is \"{beer_name}\"")
