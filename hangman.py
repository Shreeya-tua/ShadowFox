import random

words = {
    "python": "Programming Language",
    "apple": "A fruit",
    "computer": "Electronic device",
    "tiger": "Wild animal",
    "india": "Country"
}

word = random.choice(list(words.keys()))
hint = words[word]

guessed = []
attempts = 6

print("===== HANGMAN GAME =====")
print("Hint:", hint)

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        print("Correct!")
        guessed.append(guess)

    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

 
if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)