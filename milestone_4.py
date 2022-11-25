import random

word_list = ["watermelon", "raspberries", "pineapple", "strawberries", "oranges"]
num_lives = 5

word = random.choice(word_list)
word_guessed = ["_,"] * len(word)
num_letters = len(set(word))
list_of_guesses = []



class Hangman():
    
    def __init__(self, word_list = ["watermelon", "raspberries", "pineapple", "strawberries", "oranges"] , num_lives = 5):
        self.word = word
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses

    def check_guess(self, guess):
        guess == guess.lower()
        if guess in word:
             print("Good guess!", guess, "is in the word.")
             for char in word:
                 if char == guess:
                     (word.rfind(guess))
                     word_guessed[word.rfind(guess)] = guess
                     word.replace(guess, '')
                     num_letters = len(set(word))
        else:
            global num_lives
            num_lives = num_lives - 1
            print("Sorry", guess, "is not in the word")
            print("You have", num_lives, "lives left")            
        list_of_guesses.append(guess)
                          
    
    def ask_for_input(self):
        while True:
            guess = (input("Guess a single character: "))
            if len(guess) >= 2 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                 Hangman.check_guess(self, guess)
            
    
h = Hangman()
h.ask_for_input()



            


                 

    

