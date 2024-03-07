print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Choice One
choice_one = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice_one == 'left':
    # if choice left go to choice two
    choice_two = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice_two == 'wait':
        # if choice wait go to choice three
        choice_three = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        # If choice 'yellow' You found the treasure! You Win!
        if choice_three == 'yellow':
            print('You found the treasure! You Win!')
        # If choice 'red' It's a room full of fire. Game Over.
        elif choice_three == 'red':
            print("It's a room full of fire. Game Over.")
        # If choice 'blue' You enter a room of beasts. Game Over.
        elif choice_three == 'blue':
            print('You enter a room of beasts. Game Over.')
        # If you choose a door that is not in the options
        else:
            print('You choose a dor that doesnt exist. Game Over.')
    # If choice 'swim' You get attacked by an angry trout. Game Over.
    else:
        print('You get attacked by an angry trout. Game Over.')
# If choice 'right' Fall into a hole.Game Over.
else:
    print('Fall into a hole.Game Over.')
