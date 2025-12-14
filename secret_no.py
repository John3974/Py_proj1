# Secret word (change to anything you want)
secret_word = "mosiah"
word_length = len(secret_word)

# Display starting underscores
print("_" * word_length)

guesses = 0  # Count number of guesses

while True:
    guess = input("Enter your guess: ").lower()
    guesses += 1

    # Check if guess length is correct
    if len(guess) != word_length:
        print(f"Your guess must be exactly {word_length} letters long.")
        guesses -= 1   # Do not count this as a valid guess
        continue

    # If correct guess, break out and win
    if guess == secret_word:
        print(f"{secret_word.upper()}  ✓ Correct!")
        print(f"You guessed the word in {guesses} tries.")
        break

    # Otherwise, generate the hint
    hint = ""
    for i in range(word_length):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()  # Correct spot
        elif guess[i] in secret_word:
            hint += guess[i].lower()  # Right letter, wrong spot
        else:
            hint += "_"               # Not in the word at all

    print("Hint:", hint)
