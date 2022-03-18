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
import time

print("Let's play together!!")
time.sleep(1)

while True:
  all_choice = ['Rock','Paper','Scissors',3]
  win_combination = [['rock','scrissor'],['scrissor','paper'],['paper','rock']]

#get user_choice
  whatuserpick = input("What do you choose? Type 0 for Rock, 1 for Paper ,2 for Scissors, 3 for Exit \n")
  int_userpick = int(whatuserpick)
  time.sleep(0.5)
#PC_choice,#randomly pick one from all_choice
  pc_choice =random.choice(all_choice[0:3])
#user_choice
  user_choice = all_choice[int_userpick]
#exercute

#try/except
  try:
    if user_choice == 3:
      print("You chose to exit.Game Over!")
      break
    else:
      if user_choice == pc_choice:
        print(f"You chose {user_choice} and company chose {pc_choice}, the game is a tie, do it again")### LOOP
      elif [user_choice,pc_choice] in win_combination:
        print(f"You chose {user_choice} and company chose {pc_choice},You are the winner!")
      else:
        print(f"You chose {user_choice} and company chose {pc_choice},Computer is the winner!")
  except:
    print("Wrong input, please pick 0/1/2/3")