import random
keep_playing = "yes"

while keep_playing =="yes":
    secret_number = random.randint(1, 100)
    print("Random number{secret_number}")



    guess_count = 0
    guess = -1

            
    while guess != secret_number:
        guess = int(input("What is your guess?"))
        guess_count = guess_count + 1

        
        

        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:
            print("You guessed it right!")
            
    print(f"It took you {guess_count} guesses")
    keep_playing=input("Would you like to play again(yes/no)?")






