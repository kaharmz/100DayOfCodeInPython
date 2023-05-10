import random

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

random_list = [rock, paper, scissors]

#Human chose
human_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


#Cek condition
if human_chose > 2:
    print("You typed an invalid number, you lose!")
else:
    print(random_list[human_chose])

    # Computer chose
    computer_chose = random.randint(0, 2)
    print("Computer chose:")
    print(random_list[computer_chose])

    if human_chose == 0:
        if computer_chose == 0:
            print("Its a draw!")
        elif computer_chose == 1:
            print("You lose!")
        else:
            print("You win!")
    elif human_chose == 1:
        if computer_chose == 0:
            print("You win!")
        elif computer_chose == 1:
            print("Its a draw!")
        else:
            print("You lose!")
    else:
        if computer_chose == 0:
            print("You lose!")
        elif computer_chose == 1:
            print("You win!")
        else:
            print("Its a draw!")





