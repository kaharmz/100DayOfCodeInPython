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
    if computer_chose == computer_random[0]:
        print("Computer chose:")
        print(rock)
        results = "Draw!"
        print(results)
    elif computer_chose == computer_random[1]:
        print("Computer chose:")
        print(paper)
        result = "You lose!"
        print(result)
    else:
        print("Computer chose:")
        print(scissors)
        results = "You win!"
        print(results)

elif human_chose == 1:
    print(paper)
    if computer_chose == computer_random[0]:
        print("Computer chose:")
        print(rock)
        results = "You win!"
        print(results)
    elif computer_chose == computer_random[1]:
        print("Computer chose:")
        print(paper)
        result = "Draw!"
        print(result)
    else:
        print("Computer chose:")
        print(scissors)
        results = "You lose!"
        print(results)
else:
    print(scissors)
    if computer_chose == computer_random[0]:
        print("Computer chose:")
        print(rock)
        results = "You lose!"
        print(results)
    elif computer_chose == computer_random[1]:
        print("Computer chose:")
        print(paper)
        result = "You win!"
        print(result)
    else:
        print("Computer chose:")
        print(scissors)
        results = "Draw!"
        print(results)



