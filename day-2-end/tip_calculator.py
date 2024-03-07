print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill?"))
percent = tip / 100
tip_amount = bill * percent
total = bill + tip_amount
bill_person = total / people
rounded = round(bill_person, 2)
print(f"Each person should pay: ${bill_person:.2f}")
