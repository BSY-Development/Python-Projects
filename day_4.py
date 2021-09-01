from auxiliar import *
import random

possibilities = [rock, paper, scissors]

print('Rock, Paper and Scissor Game')
user_choice = int(input('Choose 0 for Rock, 1 for Paper and 2 for Scissor: \n'))
computer_choice = random.randint(0, 2)
print(f'Your choice: \n{possibilities[user_choice]}')
print(f'The computer choice \n{possibilities[computer_choice]}')

if user_choice == computer_choice:
  print('It was a draw!')
elif possible_result[user_choice]['win'] == computer_choice:
  print('You win')
else:
  print('You Lose')
