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

if size == "S" and add_pepperoni == "Y":
    total = small_pizza + 2
    print(total)
elif size == "M" or "L" and add_pepperoni == "Y":
    total = medium_pizza + 3
    print(total)

