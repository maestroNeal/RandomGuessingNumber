# Random Guessing Number
import random
randomNum=random.randint(1,100)

# print(randomNum)
userinput=None
guess=0

while randomNum!=userinput:
    userinput=int(input("Guess any number ! \n"))
    guess+=1
    if randomNum==userinput:
        print("hye ! you guessed correct number")
    else:
        if userinput>randomNum:
            print("Opps ! you guessed too high ")
        else:
            print("Opps ! you guessed too low ")

print(f"wow! you guessed the number only in {guess} times ")

print("All most completed.\nNeeded file handling ?")
