import random
print("====================WELCOME TO NUMBER GUESS GAME====================")

guess = 0
name = input("\n""Hey ! What is your Name: ")
computerguess = random.randint(1,20)
print(f"\nWell {name} , I am thinking a number from 1 to 20. ")
        
while guess<6:
    userinput = int(input("\nTake a Guess: "))
    guess+= 1
    if userinput>0 and userinput<21:
        if userinput>computerguess:
            print("Your Guess is TOO HIGH!!")
        elif userinput<computerguess:
            print("Your guess is TOO LOW!!")
        elif userinput==computerguess:
            print(f"\nHURRAY !! YOU HAVE GUESS THE RIGHT NUMBER IN {guess} GUESSES !!")
            print("Thanks for playing this beautiful game""\n")  
            break           
    if userinput<0 or userinput>20:
        print("Please enter the guesses within the range 1 to 20 .")  
else:
     print(f"Well, {name} you tried your best but couldn't guess the right number..The Correct Guess number is {computerguess}")
      
exitinput = input("\nType exit to exit the game!! : ")              
