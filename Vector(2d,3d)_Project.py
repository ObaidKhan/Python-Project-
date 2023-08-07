
class Vector:

    def __init__(self):
        print("\n==============WELCOME TO VECTOR'S CALCULATOR==============" "\n")

    def choose(self):

        print("\nChoose from the below option: ""\n")
        print("1.  2D VECTOR")
        print("2.  3D VECTOR")
        confirm = int(input("\nEnter your option number: "))
        self.confirm = confirm
        if self.confirm == 1 or self.confirm == 2:
            Vector.option

    def option(self):

        if (self.confirm == 1 or self.confirm == 2):
            print("\nChoose the Function you want to perform: ""\n")
            print("\t1.  ADDITION OF VECTOR'S: ")
            print("\t2.  SUBTRACTION OF VECTOR'S: ")
            print("\t3.  MULTIPLICATION OF VECTOR'S: ")
            choice = int(input("\n\t    Enter your Option Number: "))
            self.choice = choice

            if (self.choice == 1) and (self.confirm == 1):
                Vector.v2dVector

            if (self.choice == 1) and (self.confirm == 2):
                Vector.v3dvector

            if (self.choice == 2 and self.confirm == 1):
                Vector.v2dVector

            if (self.choice == 2) and (self.confirm == 2):
                Vector.v3dvector

            if (self.choice == 3 and self.confirm == 1):
                Vector.v2dVector

            if (self.choice == 3) and (self.confirm == 2):
                Vector.v3dvector

    def v2dVector(self):

        if ((self.choice == 1 or self.choice == 2 or self.choice == 3) and (self.confirm == 1)):
            # split dont take integer it accepts as string
            i, j = input(
                "\nEnter the First Vector separated by a space : ").split()
            x, y = input(
                "Enter the Second Vector separated by a space : ").split()
            i, j = [int(i), int(j)]
            x, y = [int(x), int(y)]
            self.icap = i
            self.jcap = j
            self.xcap = x
            self.ycap = y
            print(f"\nFirst Vector is {i}i + {j}j")
            print(f"Second Vector is {x}i + {y}j""\n")

    def v3dvector(self):

        if (self.choice == 1 or self.choice == 2 or self.choice == 3) and (self.confirm == 2):
            # split dont take integer it accepts as string
            i, j, k = input("\nEnter the First Vector: ").split()
            x, y, z = input("Enter the Second Vector: ").split()
            i, j, k = [int(i), int(j), int(k)]
            x, y, z = [int(x), int(y), int(z)]
            self.icap = i
            self.jcap = j
            self.kcap = k
            self.xcap = x
            self.ycap = y
            self.zcap = z
            print(f"\nFirst Vector is {i}i + {j}j + {k}k")
            print(f"Second Vector is {x}i + {y}j + {z}k""\n")

    def __add__(self):

        if self.choice == 1 and self.confirm == 1:
            return(f"Resultant of the two given Vector's : {self.icap+self.xcap }i+{self.jcap+self.ycap}j")
        
        elif self.choice == 1 and self.confirm == 2:
            return( f"Resultant of the two given Vector's : {self.icap+self.xcap}i+{self.jcap+self.ycap}j+{self.kcap+self.zcap}k")
        
        # else:
        #     print("Returning None as Add function is not being executed ")

    def __sub__(self):

        if self.choice == 2 and self.confirm == 1:
            return (f"Subtraction of the two given Vector's : {self.icap-self.xcap }i-({self.jcap-self.ycap})j")

        if self.choice == 2 and self.confirm == 2:
            return(f"Subtraction of the two given Vector's : {self.icap-self.xcap}i-({self.jcap-self.ycap})j-({self.kcap+self.zcap})k")
    def __mul__(self):

        if self.choice == 3 and self.confirm == 1:
            return (f"Dot product of the two given Vector's : {self.icap*self.xcap + self.jcap*self.ycap}")
            
        if self.choice == 3 and self.confirm == 2:
            return(f"Dot Product of the two given Vector's : {self.icap*self.xcap+self.jcap*self.ycap+self.kcap*self.zcap}")

    
if __name__=="__main__":
    v = Vector()
    while(True):
        v.choose()
        v.option()
        v.v2dVector()
        v.v3dvector()
        print(v.__add__())
        print(v.__sub__())
        print(v.__mul__())
