class Complex():
    @staticmethod
    def welcome():
        print("--------------------------Welcome To Complex Number World--------------------------""\n")

    def complexnum1(self):

        print("ADDITION AND MULTIPLICATION OF COMPLEX NUMBER""\n")
        real = int(input("Enter the real parts of first Complex Number: "))
        imaginary = int(input("Enter the imaginary parts of First Complex Numbers: "))
        self.real = real
        self.imaginary =imaginary

    def complexnum2(self):
        real1 = int(input("Enter the real parts of Second Complex Numbers: "))
        imaginary1 =int(input("Enter the imaginary parts of Second Imaginary Numbers: "))
        self.real1 = real1
        self.imaginary1 =imaginary1

    def __add__(self):
        return f"\nComplex Number Addition: {self.real+self.real1}+{self.imaginary+self.imaginary1}i"

    def __mul__(self):
        mulReal = (self.real*self.real1)-(self.imaginary*self.imaginary1)
        mulImaginary = (self.real*self.imaginary1)+(self.imaginary*self.real1)
        return (f"Complex Number Multiplication: {mulReal}+{mulImaginary}i\n")

    
c=Complex()
c.welcome()
c.complexnum1()
c.complexnum2()
print(c.__add__())
print(c.__mul__())