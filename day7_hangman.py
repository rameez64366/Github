import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
display=[]
for char in chosen_word:
  display.append("_")
print(chosen_word)
print(display)
lives=len(stages)
end_game=True
while end_game:
  user_guess=input("guess a letter: ").lower()
  if user_guess in display:
    print("already guessed")
  else:
    for i in range(len(chosen_word)):
      if chosen_word[i]==user_guess:
        display[i]=user_guess
    print(display)
    if user_guess not in chosen_word:
      lives-=1
      print(f"Your guess: {user_guess} is not in the word")
      print("wrong you lose a life")
      print(stages[lives])
      if lives==0:
        print("you are out of lives. Game over")
        end_game=False
if "_" not in display:
  end_game=False
  print("you win")