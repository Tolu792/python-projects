# Rock Paper Scissors
import random

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

games_images = [rock, paper, scissors]

player_choice = int(input("Select 0 for Rock, 1 for Paper and 2 for scissors\n"))

if player_choice < 0 or player_choice >= 3:
    print("Select a valid option, you lose!")

else:
    print("You chose:")
    print(games_images[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(games_images[computer_choice])

    if player_choice == computer_choice:
        print("It's a draw!")
    elif computer_choice == 2 and player_choice == 0:
        print("You win!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice > player_choice:
        print("You lose!")


