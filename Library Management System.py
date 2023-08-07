import string
import random

str = 4

class Library:

    def __init__(self,listofbooks):
       self.books =listofbooks

    def login(self):
    
        self.ID = input("Enter your Student ID: ")
        self.name = input("Enter your User Name: ")
        self.password = input("Enter Your Password: ")
        with open("StudentInfo.txt","r")as f:
            self.Info = f.read()
            if (self.ID in self.Info and self.password in self.Info and self.name in self.Info):
                print(f"\nWelcome {self.name} to our Library Management System!! ")
            else:
                print("User does not exist in System!!\nDo you want to create an Account?")
                self.input =input("Enter your Choice as Y or N: ")
                if self.input =="Y":
                    Library.create_account(self)
                elif self.input == "N":
                    print("\nThanks for using Our Library System""\n")
                    exit()
                else:
                    print("Invalid Input!!""\n")


    def create_account(self):
        if (self.input == "Y") or (userchoice == 1):
            self.name = input("Enter Your Name: ")
            self.password = input("Enter the Password: ")
            self.confirm_password = input ("Enter the Same Password for confirmation: ")
            self.ID = "".join(random.choices(string.ascii_uppercase+string.digits,k=str))
            print(f"Youe Student ID is : {self.ID}")
            with open("StudentInfo.txt","w")as f:
                self.Info =f.writelines(f"Username - {self.name}  Password - {self.confirm_password}  ID - {self.ID}")


    def display_book(self):
        print("\nBOOKS AVAIALABLE IN THIS LIBRARY ARE: ")
        index=0
        for item in (self.books):
            print(f"{index+1}",item)
            index+=1
                 

    def issue_book(self,bookname):
        if bookname in self.books:
            print(f'''You have been issued the Book {bookname}. Hope you enjoy reading it.\n***Please keep it safe and return within 30 days***''')
            self.books.remove(bookname)
            with open("StudentInfo.txt","a")as f:
                self.Info = f.write(f"   Book Issue - {bookname}")
            # return True
        else:
            print("Books not available now. Please wait utill the book is available!")
            # return False
        

    def add_book(self,addbook):
        self.books.append(addbook)
        print(f"The book {addbook} have been added in the Book List of our library Management System")

    def return_book(self,returnbook):

        if returnbook in self.books:
            self.books.append(returnbook)
            print(f"Thanks for using our Library Management System. Have a Good Day Ahead!!")
        else:
            print("Sorry!! We have no such book issued to any Student ID")

        with open("StudentInfo.txt","r")as f:
            self.Info = f.read()
            if returnbook in (self.Info):
                self.Info = self.Info.replace(f"   Book Issue - {returnbook}","")
                with open("StudentInfo.txt","w")as f:
                    f.write(self.Info)
            
        

    def student_history(self):
        self.studentid = input("Enter the Student ID: ")
        with open ("StudentInfo.txt")as f:
            if self.studentid in self.Info:
                print(f.read())
            else:
                print("YOU HAVE ENETERED AN INVALID STUDENT ID ")


class Student:

    def profile(self):
        self.verifyoldname = input("Enter your Old User Name: ")
        self.verifyoldpassword = input("Enter your Old Password: ")
        with open("StudentInfo.txt","r")as f:
            self.info =f.read()
            if (self.verifyoldname) and (self.verifyoldpassword) in self.info:
                self.changeusername = input("Enter New User Name: ")
                self.changepassword = input("Enter the New Password: ")
                self.confirmchangepassword = input("Re-Enter the Password: ")
                self.info = self.info.replace(self.verifyoldname,self.changeusername).replace(self.verifyoldpassword,self.confirmchangepassword)
                with open("StudentInfo.txt","w")as f:
                    f.write(self.info)
            else:
                print("Username not registered!!!")

    def request_book(self):
        self.requestbook = input("Enter The Book Name you want to Borrow : ")
        return self.requestbook

    def add_book(self):
        self.addbook = input("Enter The Book Name you want to Add to our Library System: ")
        return self.addbook

    def return_book(self):
        self.returnbook= input("Enter the Book Name that you want to Return: ")
        return self.returnbook


if __name__ =="__main__":

    L=Library(["Maths","Science","English","Hindi","Social Science"])
    S= Student()
    print('''=========================WELCOME TO LIBRARY MANAGEMENT SYSTEM=========================\n''')
    L.login()
    while(True):
        
        Maindomain_msg ='''\nPlease Choose an Option: \n 
        1. Create an Account.
        2. Display Book List.
        3. Issue a Book.
        4. Add a Book.
        5. Return a Book.
        6. Student Details.
        7. Update Profile.
        8. Exit'''"\n" 
        print(Maindomain_msg)
        userchoice = int(input("Enter Your Choice from the above Option: "))
        if (userchoice == 1):
            L.create_account()    
        elif (userchoice == 2):
            L.display_book()    
        elif (userchoice == 3):
            L.issue_book(S.request_book())
        elif (userchoice == 4):
            L.add_book(S.add_book())
        elif (userchoice == 5):
            L.return_book(S.return_book())
        elif (userchoice == 6):
            L.student_history()
        elif (userchoice == 7):
            S.profile()
        elif (userchoice == 8):
            exit()
        else:
            print("INVALID INPUT!!")