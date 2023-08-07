import random
choices = ["Rock", "Paper", "Scissors"]
userscore = 0
computerscore = 0
Draw = 0


class Game:

    def __init__(self):

        print(
            "\n-------------------WELCOME TO ROCK,PAPER,SCISSOR GAME---------------------\n")


class Game_rule:

    def input(self):

        if option == 1:

            print("Enter the Choice as : Rock , Paper , Scissors\n")
            self.userinput = input("User Choice : ")
            try:
                if self.userinput!="Rock" and self.userinput!="Paper" and self.userinput!="Scissors":
                    print("\nPlease enter the choices correctly !!")
                else:
                    self.computerguess = random.choice(choices)
                    print("\nComputer Guess : ", self.computerguess)
            except Exception as e:
                print(e)               
            
                    
    def rule(self):
        global Draw
        global userscore
        global computerscore  
           
        if self.userinput == self.computerguess:
            print("\nResult : It's a Draw !!")
            Draw += 1
          
        
        if (self.userinput == "Rock" or self.computerguess == "Rock") and (self.userinput == "Paper" or self.computerguess == "Paper"):
            print("\nPaper covered Rock")
            if self.userinput == "Paper":
                print("\nResult : User Won !")
                userscore += 1
            else:
                print("\nResult : Computer Won !")
                computerscore += 1
                
        if (self.userinput == "Rock" or self.computerguess == "Rock") and (self.userinput == "Scissors" or self.computerguess == "Scissors"):
            print("\nRock blunt Scissors")
            if self.userinput == "Rock":
                print("\nResult : User Won !")
                userscore += 1
            else:
                print("\nResult : Computer Won !")
                computerscore += 1

        if (self.userinput == "Paper" or self.computerguess == "Paper") and (self.userinput == "Scissors" or self.computerguess == "Scissors"):
            print("\nScissor cuts Paper")
            if self.userinput == "Scissors":
                print("\nResult : User Won !")
                userscore += 1
            else:
                print("\nResult : Computer Won !")
                computerscore += 1

    def score(self):
        print("\nUserScore : ", userscore)
        print("\nComputerScore : ", computerscore)
        print("\nNo Result : ", Draw)


if __name__ == "__main__":

    G = Game()
    Gr = Game_rule()

    while True:
        try:
            print('''\nChoose the Option :\n
                    1.  Play the Game.
                    2.  Score.
                    3.  Quit.\n''')
            option = int(input("Enter the option : "))
            print()
            
            if (option == 1):
                Gr.input()
                Gr.rule()
            elif option == 2:
                Gr.score()
            elif (option == 3):
                if userscore > computerscore:
                    print("User has won maximum times !")
                elif userscore == computerscore:
                    print("No one's win !! Its a Draw betwwen User and Computer !")
                else:
                    print("Computer have won maximum times !")
                print("\nThanks for playing the Game.\n")
                input("Enter any key to exit. ")
                exit()
            else:
                print("Invalid Choice !!")
        except Exception as e:
            print("\nInvalid Choice")