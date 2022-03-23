#A
"""show _ base on letter numbers"""
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
lives = 3
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# B
"""replace with letters"""
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter
  
  #print(display)

#C 
  """control lose times"""
  if guess not in chosen_word:
    lives-=1
    print(f"\033[41mWrong! Now you have {lives} lives left\033[0m")
    if lives == 0:
      end_of_game = True
      print("\033[41mYou lose\033[0m")
   
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
    
  if "_" not in display:
    end_of_game = True
    #\033[xx;xxmSTRING\033[0m
    #\033[1;31;40m    --1-highlined 31-font color  40-bkg color--
    print("\033[1;42mYou Win\033[0m")