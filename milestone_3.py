import random 

word_list = ["watermelon", "raspberries", "pineapple", "strawberries", "oranges"]

word = random.choice(word_list)

print(word) 

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess!", guess, "is in the word.")
    else:
        print("Sorry, ", guess, "is not in the word.")

def ask_for_input():
    while True:
        guess = input("Guess a single letter: ")
        if len(guess) < 2 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()

