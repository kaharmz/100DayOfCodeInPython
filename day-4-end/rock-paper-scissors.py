import random

human_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


#Computer chose
computer_random = [rock, paper, scissors]
computer_chose = random.choice(computer_random)

#Human chose
if human_chose == 0:
    print(rock)
    print("Computer chose:")
    if computer_chose == computer_random[0]:
        print(rock)
        print("Draw!")
    elif computer_chose == computer_random[1]:
        print(paper)
        print("You lose!")
    else:
        print(scissors)
        print("You win!")

elif human_chose == 1:
    print(paper)
    print("Computer chose:")
    if computer_chose == computer_random[0]:
        print(rock)
        print("You win!")
    elif computer_chose == computer_random[1]:
        print(paper)
        print("Draw!")
    else:
        print(scissors)
        print("You lose!")
else:
    print(scissors)
    print("Computer chose:")
    if computer_chose == computer_random[0]:
        print(rock)
        print("You lose!")
    elif computer_chose == computer_random[1]:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("Draw!")



