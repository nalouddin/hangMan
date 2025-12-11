import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")