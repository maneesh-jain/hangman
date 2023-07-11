# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

Set up Git and GitHub.

## Milestone 2

Built a *list* of 5 words and chose a random word for the user to try and guess.
Updated this Readme file with Milestones 1 & 2.

## Milestone 3

Defined two separate *functions* to aid code readability: 
- ask_for_input - to request input from the user and check it's a valid letter of the alphabet; this largely reused code from Milestone 2 
- check_guess - to see if the user's letter is in the word to be guessed

## Milestone 4

Created a Hangman *class* with the following *attributes*:
- word_list - list of words for computer to choose from
- num_lives - no. of lives user has
- word - word randomly chosen by computer
- word_guessed - word guessed by user
- num_letters - no. of unique letters left to guess
- list_of_guesses - letters guessed

The two existing functions were coded as *methods* and extended:
- ask_for_input - now checks if the user has already guessed that letter
- check_guess - now updates attributes *word_guessed* if the guess is right, and *num_lives* if the guess is wrong

## Milestone 5

Added a *function* called *play_game* to run all the code of the game:
- checks if user still has *num_lives* left to play
- checks if there are still *num_letters* left to be guessed
- checks if user still has *num_lives* and there are zero *num_letters* left to guess, the user has won!

Bug fix:
- formula for *num_lives* corrected