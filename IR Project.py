
import string
import random


S=10

class IndianRailway:

    def __init__(self, train):
        self.train = train
        print(
            "\n"f"---------------------------------------WELCOME TO {self.train}---------------------------------------", "\n")


class Train:

    fare = int(500)

    def option(self):

        self.confirmation = input("Choose the Following Option: \n"
        "\n""    1. Type B to Book a Ticket\n"
        "    2. Type C for Cancellation: \n"
        "    3. Type P for PNR Status: \n"
        "    4. Type S for Seat Availability: \n"          
        "\n""       Option = ")

        if (self.confirmation == "B"):
            Obaid.seat_availability
        
        while self.confirmation != "B" and self.confirmation != "C" and self.confirmation != "P" and self.confirmation != "S":
                self.confirmation = input("Please Enter the Correct Input to continue: ")
        # else:
        #      print("    Wrong Input")

        if (self.confirmation=="C"):
            checkpnr=input("Enter the 10 Digit PNR for cancellation: ")
            self.checkpnr=checkpnr
            with open("CheckPnr.txt")as file:
                if self.checkpnr in file:
                    print(f"Valid PNR number!!""\n")
                    Obaid.cancellation
                else:
                    print("INVALID PNR NUMBER!!! PLEASE CHECK AGAIN !!")


        if (self.confirmation == "P"):
            checkpnr=input("ENTER PNR NUMBER: ")
            self.checkpnr=checkpnr
            with open("CheckPnr.txt")as file:
                if self.checkpnr in file:
                    Obaid.Pnrstatus
                else:
                    print("INVALID PNR")
                    

        if (self.confirmation=="S"):
            Obaid.seat_availability


    def seat_availability(self):

        if (self.confirmation == "B" or self.confirmation == "S"):
            Seats = random.randint(1, 300)
            trainname = input("\n""Enter the Train name or Train number: ")
            boarding = input("Enter the Boarding Station: ")
            Destination = input("Enter the Arrival Station : ")
            DOJ = input("Enter The Journey Date: ")
            NumberofPassenger = int(input("Enter The Number of Passengers: "))
            classAC = input("Enter the Class of Reservation: ")

            self.trainname = trainname
            self.Destination = Destination
            self.boarding = boarding
            self.DOJ = DOJ
            self.Seats = Seats
            self.NumberofPassenger = NumberofPassenger
            self.classAC = classAC

            print("\n"f"Total {self.Seats} SEATS available in {self.trainname} in {self.classAC} class for reservation upto  {self.Destination} Junction from {self.boarding} on {self.DOJ}" "\n")

    def fare_information(self):

        #self.fare = fare

        if (self.confirmation == "B") and int(self.NumberofPassenger) <= (self.Seats):
            print(
                f"Total Fare for {int(self.NumberofPassenger)} Passengers is: {int(self.NumberofPassenger)*(self.fare)}" "\n")
        else:
            print()

    def get_status(self):

        if (self.confirmation == "B") and (self.Seats) < int(self.NumberofPassenger):
            print(
                f"SORRY!!! Number of {self.NumberofPassenger} Seats you required are not available in {self.trainname}" "\n")
            print("Thanks for using Indian Railway. See you Soon!!" "\n")
        else:
            Obaid.confirm

    def confirm(self):

        if (self.confirmation == "B") and (self.Seats) >= int(self.NumberofPassenger):

            confirmation = input("Do you want to Book your Ticket: Y/N:  ")
            self.confirmation = confirmation

            if (confirmation == "Y") and int(self.NumberofPassenger) <= (self.Seats):
                Obaid.get_details

            elif(confirmation == ""):
                print("\n" "            Wrong Input!!!")
                while (self.confirmation != "Y" and self.confirmation != "N"):
                    confirmation = input("\n""Please type the Correct Input: Type Y or N : ")
                    self.confirmation=confirmation
                    Obaid.get_details
                else:
                    print("\n""Thanks for using Indian Railway. See you Soon!!" "\n")

    def book_a_ticket(self, name, age, sex):
        if (self.confirmation) == "Y" and int(self.NumberofPassenger) <= (self.Seats):
            # self.PNR
            # self.trainname
            # self.boarding
            # self.Destination
            # self.DOJ
            # self.classAC
            # self.NumberofPassenger
            self.name = name
            self.age = age
            self.sex = sex

    def generate_Pnr(self):
        if(self.confirmation == "Y") and int(self.NumberofPassenger) <= (self.Seats):
            PNR="".join(random.choices(string.ascii_uppercase + string.digits,k=S))
            self.PNR=PNR
            with open("CheckPnr.txt","w")as file:
                file.write(PNR)
                
    
    def Pnrstatus(self):
         if (self.confirmation == "P"):
            with open("CheckPnr.txt")as file:
                if self.checkpnr in file:
                    with open("getdetails.txt")as file:
                        print(file.read())

    def cancellation(self):
        if (self.confirmation == "C"):
            with open("CheckPnr.txt")as file:
                if self.checkpnr in file:
                    with open("getdetails.txt")as file:
                        print(file.read())
                        print("YOUR TICKET HAS BEEN CANCELLED!!" )


    def get_details(self):

        if(self.confirmation == "Y" or self.confirmation=="B") and int(self.NumberofPassenger) <= (self.Seats):
            print("\n""PNR NUMBER: ",self.PNR)
            print("TRAIN NAME: ", self.trainname)
            print("BOARDING STATION: ", self.boarding)
            print("RESERVATION UPTO: ", self.Destination)
            print("DATE OF JOURNEY: ", self.DOJ)
            print("CLASS: ", self.classAC)
            print("NUMBER OF PASSENGERS: ", self.NumberofPassenger)
            print("NAME: ", self.name)
            print("AGE: ", self.age)
            print("SEX: ", self.sex, "\n")

            with open("getdetails.txt","w") as file:
                file.write(f"PNR NO. ---> {self.PNR}\n" )
                file.write(f"TRAIN NAME ---> { self.trainname}\n")
                file.write(f"BOARDING ---> {self.boarding}\n")
                file.write(f"RESERVATION ---> {self.Destination}\n")
                file.write(f"DATE ---> {self.DOJ}\n")
                file.write(f"CLASS ---> {self.classAC}\n")
                file.write(f"NAME ---> {self.name}\n")
                file.write(f"AGE ---> {self.age}\n")
                file.write(f"SEX ---> {self.sex}\n")
                file.write(f"Total seats available now : {(int(self.Seats)-int(self.NumberofPassenger))+int(self.NumberofPassenger)}")
                
    def greet(self):

        if (self.confirmation) == "Y" and int(self.NumberofPassenger) <= (self.Seats):

            print("Yor ticket have been booked.")
            print(f"Total seats available now is : {int(self.Seats)-int(self.NumberofPassenger)}")
            print("Wish you a very Happy Journey on behalf of Indian Railway.""\n")

if __name__=="__main__":

    while(True):
        Obaid = IndianRailway("INDIAN RAILWAY")
        Obaid = Train()
        Obaid.option()
        Obaid.seat_availability()
        Obaid.fare_information()
        Obaid.get_status()
        Obaid.cancellation()
        Obaid.confirm()
        Obaid.generate_Pnr()
        Obaid.Pnrstatus()
        Obaid.book_a_ticket(["OBAID", "TEHSEEN", "HARISH", "TEHZEEB", "HABEEB"], [29, 5, 1, 15, 13], ["M", "F", "M", "F", "M"])
        Obaid.get_details()
        Obaid.greet()
