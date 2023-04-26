# Life in weeks calculator
age = input("What is your current age? ")

#Write your code below this line
turning = 90 - int(age)
days = turning * int(365)
weeks = turning * int(52)
months = turning * int(12)

#output
print(f"You have {days} days, {weeks} weeks, and {months} months left.")



