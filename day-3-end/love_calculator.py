# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line

merge_name = (name1 + name2).lower()

true_count = 0
love_count = 0

#check for the number of times the letters in the word TRUE occurs
for name_one in set("true"):
    true_count += merge_name.count(name_one)

# check for the number of times the letters in the word LOVE occurs.
for name_two in set("love"):
    love_count += merge_name.count(name_two)

# combine these numbers to make a 2 digit number.
love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 >= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")










# For Love Scores less than 10 or greater than 90
#For Love Scores between 40 and 50
#Otherwise, the message will just be their score. e.g.: