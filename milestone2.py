import random

word_list = ['apple', 'banana', 'orange', 'cherry', 'mango']
word = random.choice(word_list)
guess = input('Enter a single letter: ')
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
