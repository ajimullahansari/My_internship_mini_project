import random
randNumber = random.randint(1,100)
print(randNumber)

userGuess = int(input("Enter your guess:"))
if(userGuess==randNumber):
    print("You guessed it right!")
else:
    print("You guessed it wrong!")
