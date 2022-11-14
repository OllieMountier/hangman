# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

In milestone 3, to define the check_guess function, using "def" to show I will be defining a function and then using "guess" as my parameters, I used the if condition to check if the guess was in the word and then returned a statmement back to the user for each outcome. 
To define the ask_for_input function I also used "def" but no parameters. I then used a while loop to continue the guessing until the inputted character was correct and an if condition to check if the guess had the right paramters.. e.g was a character not a number and was only one character long. If the guess was an acceptable input, the while loop would "break" otherwise it would return a statement to the user and letting them guess again. The ask_for_input function also contained the check_guess function so I would only have to print one function instead of both.
