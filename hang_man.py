import random

# list of words to choose from
words = ["apple", "banana", "cherry", "orange", "pear", "kiwi", "mango"]

# choose a random word from the list
word = random.choice(words)

# create a string with underscores to represent the unknown letters
unknown = "_" * len(word)

# list to store guessed letters
guessed = []

# number of chances the player has to guess the word
chances = 6

# while loop to continue game until the player has run out of chances or has guessed the word
while chances > 0 and unknown != word:
    print(unknown)
    print("Chances remaining: ", chances)
    guess = input("Guess a letter: ")

    # if the player has already guessed the letter, tell them
    if guess in guessed:
        print("You've already guessed that letter! Try again.")
    # if the letter is in the word, replace the corresponding underscores in the unknown string
    elif guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                unknown = unknown[:i] + guess + unknown[i+1:]
    # if the letter is not in the word, decrement chances
    else:
        print("Incorrect!")
        chances -= 1

    # add the guess to the list of guessed letters
    guessed.append(guess)

# game over - print the word and whether the player won or lost
print("The word was:", word)
if unknown == word:
    print("Congratulations, you won!")
else:
    print("Sorry, you lost. Better luck next time!")
