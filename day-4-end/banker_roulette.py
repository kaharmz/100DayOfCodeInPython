# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above

#Write your code below this line
result = random.randrange(len(names))
random_people = names[result]
print(f"{random_people} is going to buy the meal today!")