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

#Write your code below this line 👇
import random

print("Welcome to rock paper scissors.")

player_input = input("Choose rock, paper or scissors, (r, p, s): ")
if player_input == "r":
  print(f"You chose rock \n{rock}")
  player_input = "rock"
elif player_input == "p":
  print(f"You chose paper \n{paper}")
  player_input = "paper"
elif player_input == "s":
  print(f"You chose scissors \n{scissors}")
  player_input = "scissors"
else:
  print("INVALID SELECTION")

computer_input = random.randint(0, 2)
if computer_input == 0:
  computer_choice = "rock"
  print(f"Computer chose rock \n{rock}")
elif computer_input == 1:
  computer_choice = "paper"
  print(f"Computer chose paper {paper}")
elif computer_input == 2:
  computer_choice = "scissors"
  print(f"Computer chose scissors \n{scissors}")

if computer_choice == player_input:
  print("DRAW")
elif computer_choice == "rock" and player_input == "paper":
  print("YOU WIN")
elif computer_choice == "rock" and player_input == "scissors":
  print("YOU LOSE")
elif computer_choice == "scissors" and player_input == "paper":
  print("YOU LOSE")
elif computer_choice == "scissors" and player_input == "rock":
  print("YOU WIN")
elif computer_choice == "paper" and player_input == "scissors":
  print("YOU WIN")
elif computer_choice == "paper" and player_input == "rock":
  print("YOU LOSE")