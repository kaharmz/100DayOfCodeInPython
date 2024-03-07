# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above

# Write your code below this line
choice = random.randrange(len(names))
people_pay = names[choice]
print(f"{people_pay} is going to buy the meal today!")
