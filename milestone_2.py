import random 

word_list = ["Watermelon", "Raspberries", "Pineapple", "Strawberries", "Oranges"]
print(word_list)

word = random.choice(word_list)

print(word)

guess = input(" Guess a single letter:")

if len(guess) < 2 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! Thats not a valid input.")


