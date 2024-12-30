import random

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print("Python Program for Word Guessing Game")
print("\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

name = input("What is your name? ")
print("\n")
print("Good Luck ! ", name)
print("\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

words = ['rainbow', 'computer', 'science', 'programming','standard', 'charles', 'orange', 'goat','yam',
         'python', 'mathematics', 'player', 'condition', 'glory', 'jesus', 'error', 'mother', 'star',
         'reverse', 'water', 'board', 'geeks', 'curtain', 'phone','hundred', 'home', 'shoe']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 27

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")