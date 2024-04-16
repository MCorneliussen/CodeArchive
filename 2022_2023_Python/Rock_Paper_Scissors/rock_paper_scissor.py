rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

image = [rock, paper, scissors]

print("Welcome to my Rock, Paper and scissors game.")

player = int(input("Please type in your guess. Rock, Paper or Scissors?\n 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player >= 3 or player < 0:
    print(f"Invalid answer. You lose.")
    
else:
    print("Player chose: ")
    print(image[player])

    computer = random.randint(0, 2)
    print("Computer chose: ")
    print(image[computer])


    if player == 0 and computer == 2:
        print(f"You win.")
    elif computer == 0 and player == 2:
        print(f"You lose.")
    elif player > computer:
        print(f"You win.")
    elif computer > player:
        print(f"you lose.")
    elif computer == player:
        print(f"It's a draw!")
        
