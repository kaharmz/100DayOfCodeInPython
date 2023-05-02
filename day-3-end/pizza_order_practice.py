# Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

"""
CLUE
    Small Pizza: $15
    Medium Pizza: $20
    Large Pizza: $25
    Pepperoni for Small Pizza: +$2
    Pepperoni for Medium or Large Pizza: +$3
    Extra cheese for any size pizza: + $1
"""

#Write your code below this line
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# Size small
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = small_pizza + 1 + 2
            print(f"Your final bill is: ${total}.")
        elif extra_cheese == "N":
            total = small_pizza + 2
            print(f"Your final bill is: ${total}.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            total = small_pizza + 1
            print(f"Your final bill is: ${total}.")
        elif extra_cheese == "N":
            total = small_pizza + 0
            print(f"Your final bill is: ${total}.")
# Size medium
if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = medium_pizza + 1 + 3
            print(f"Your final bill is: ${total}.")
        elif extra_cheese == "N":
            total = medium_pizza + 3
            print(f"Your final bill is: ${total}.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            total = medium_pizza + 1
            print(f"Your final bill is: ${total}.")
        elif extra_cheese == "N":
            total = medium_pizza + 0
            print(f"Your final bill is: ${total}.")

# Size large
if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total = large_pizza + 1 + 3
            print(f"Your final bill is: ${total}.")
        elif extra_cheese == "N":
            total = large_pizza + 3
            print(f"Your final bill is: ${total}.")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            total = large_pizza + 1
            print(f"Your final bill is: ${total}.")
        elif extra_cheese == "N":
            total = large_pizza + 0
            print(f"Your final bill is: ${total}.")
else:
    print("Please select size pizza :)")

