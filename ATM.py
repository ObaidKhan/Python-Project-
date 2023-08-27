class ATM:

    def __init__(self):
        print("")
        print("WELCOME TO PYTHON ATM !\n".center(140))
        self.pin=None
        self.balance=0
        self.menu()
        
    def menu(self):
        while True:
            print('''\nChoose the following number for proceeding :

                1. CHECK BALANCE
                2. WITHDRAW MONEY
                3. DEPOSIT MONEY
                4. CREATE PIN
                5. CHANGE PIN
                6. EXIT
                ''')

            try:       
                self.user_input=int(input("Enter the choices : "))

                if self.user_input==1:
                    if self.pin==None:
                        print("\nYou have not created your ATM PIN yet.")
                        print("First Create a Pin.")
                        self.menu()
                    else:
                        self.check_pin()==self.pin
                        self.check_balance()
                elif self.user_input==2:
                    if self.pin==None:
                        print("\nYou have not created your ATM PIN yet.")
                        print("First Create a Pin.")
                        self.menu()
                    else:
                        self.check_pin()==self.pin
                        self.withdraw_money()
                elif self.user_input==3:
                    if self.pin==None:
                        print("\nYou have not created your ATM PIN yet.")
                        print("First Create a Pin.")
                        self.menu()
                    else:
                        self.deposit_money()
                elif self.user_input==4:
                    self.create_pin()
                elif self.user_input==5:
                    if self.pin==None:
                        print("First Generate a PIN !!")
                        self.menu()
                    else:
                        self.change_pin()    
                elif self.user_input==6:
                    exit()
                else:
                    print("Invalid Choice !")
            except ValueError:
                print("Invalid Choice")
        
    def create_pin(self):
    
        try:
            new_pin=int(input("\nEnter a 4 digit PIN to be created : "))
            if len(str(new_pin))==4:
                self.pin=new_pin
                print("PIN created Successfully.\n")
            else:
                print("Only 4 digit pin is allowed.\n")
                self.create_pin()
        except ValueError:
            print("Only digit is allowed !\n")
            self.create_pin()
        
        
    def change_pin(self):
        
        try:
            old_pin=int(input("\nEnter your old ATM PIN : "))
            
            if self.pin==old_pin:
                try:
                    while True:
                        new_pin=int(input("Enter your new pin : "))
                        if len(str(new_pin))==4:
                            self.pin=new_pin
                            print("New Pin created Successfully.\n")
                            break
                        else:
                            print("Give a 4 digit PIN only !!")
                except ValueError:
                    print("Only digit is allowed !!\n")
                    self.change_pin()
            else:
                print("INVALID PIN !!")
                self.change_pin()
        except ValueError:
            print("Only digit allowed")
            self.change_pin()


    def check_pin(self):
        
        try:
            check_pin=int(input("\nEnter your PIN : "))
            if check_pin==self.pin:
                return check_pin
            else:
                print("Invalid PIN !!\n")
                self.check_pin()
        except ValueError:
            print("Only digit is allowed !!\n")
            self.check_pin()
        

    def deposit_money(self):
        # without using check_pin method
            try:
                pin=int(input("\nEnter your ATM PIN : "))
                if self.pin==pin:
                    try:
                        while True:
                            amount=int(input("\nEnter the amount to be deposited : "))
                            self.balance=self.balance+amount
                            print("\nYour money has been deposited successfully.")
                            print("Now balance :Rupees",self.balance)
                            break
                    except ValueError:
                        print("Invalid Input ! ")
                        self.deposit_money() 
                else:
                    print("INVALID PIN !!")
                    self.deposit_money()            
            except ValueError:
                print("Only digit allowed !")
                self.deposit_money()

    def withdraw_money(self):
            #using check_pin method
            try:
                amount=int(input("\nEnter the amount to be withdrawed : "))
                if amount <= self.balance:
                    self.balance=self.balance-amount
                    print("\nTransaction Successfull.\n")
                    print("Now balance : Rupees",self.balance)
                elif self.balance==0:
                    print("\nTRANSACTION FAILED !! NO MONEY IN YOUR ACCOUNT !! ")
                else:
                    print("\nINSUFFICIENT FUND !!")
                    print("\nYour balance is Rupees",self.balance)
                    try:
                        while True:
                            confirmation=input("\nDo you want to withdraw money ?? Y or N : ")
                            if confirmation=='Y':
                                self.withdraw_money()
                                break
                            elif confirmation=='N':
                                self.menu()
                            else:
                                print("\nInvalid Choice !")
                                pass

                    except ValueError:
                        print("Invalid Choice!")
            except ValueError:
                print("Invalid Input !")
                self.withdraw_money()

    def check_balance(self):

        print("\nYOUR BALANCE IS RUPEES",self.balance)
       
sbi=ATM()
