import random
print("==================WELCOME TO NUMBER GUESS GAME==================")

guess = 0
computerguess = 0
name = input("\nEnter Your Name: ")

print(f'''\nHey {name} , I am your Guess Number Artifical Intelligence\n
Let's Play a game where you think a number from 1 to 20 and I would try to guess it correctly!!'''"\n")

userguess = int(input(f"Well , {name} Give me a number to guess: " ))

while computerguess!=userguess: 

    computerguess = random.randint(1,20)
    print("\nComputer Guesses : ",computerguess)
    guess+=1   
    if computerguess<userguess:
        print("\nThink Higher than this.")
    elif computerguess>userguess:
        print("\nThink Lower than this.")
    elif computerguess==userguess:
        print("\nHurray ,You guess it correctly. You are a Genius!!")
        print(f"You have guessed it in {guess} guesses.")
        break
else:
    print(f"\nSorry, My friend !! You failed !! The correct guess number is : {userguess}")

exitinput = input("\nType exit to exit the game!! : ")   