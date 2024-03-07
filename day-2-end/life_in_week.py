# Life in weeks calculator
age = int(input("What is your current age? "))

# Write your code below this line
until = 90 - age
days = until * int(365)
weeks = until * int(52)
months = until * int(12)

# output
print(f"You have {days} days, {weeks} weeks, and {months} months left!.")
