import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list # list of words for computer to choose from
        self.num_lives = num_lives # no. of lives user has
        self.word = random.choice(self.word_list) # word randomly chosen by computer
        self.word_guessed = list('_' * len(self.word)) # word guessed by user
        self.num_letters = len(set(self.word)) # no. of unique letters left to guess
        self.list_of_guesses = [] # letters guessed

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter: ')
            if not(len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters <= 0:
            print('Congratulations. You won the game!')
            break

play_game(['apple', 'banana', 'orange', 'cherry', 'mango'])