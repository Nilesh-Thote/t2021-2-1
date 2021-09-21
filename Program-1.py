"""Problem-1: Create a small calculator which performs operations
 such as Addition, Subtraction, Multiplication and Division using class.
"""
class Calculator:
    def Addition(self,a,b):
        """Method to add two numbers"""
        sum=a+b
        print(a,"+",b," = ",sum)
    def Subtraction(self,a,b):
        """Method to subtract two numbers."""
        dif=a-b
        print(a,"-",b," = ",dif)
    def Multiplication(self,a,b):
        """Method to multiply two number"""
        mul=a*b
        print(a,"*",b," = ",mul)
    def Division(self,a,b):
        """Method to divide one number by other"""
        try:
            div=a/b
            print(a,"/",b," = ",div)
        except ZeroDivisionError:
            print("You cannot divide by Zero")
a=float(input("Enter the value of a: "))           #Asking user for input
b=float(input("Enter the value of b: "))           #Asking user for input
op=input("type of operation: ")                    #Asking user for type of operation
Cal=Calculator()                                   #instance of class calculator
if op=="+":
  Cal.Addition(a,b)                                
elif op=="-":
  Cal.Subtraction(a,b)
elif op=="*":
  Cal.Multiplication(a,b)
elif op=="/":
  Cal.Division(a,b)
else:
  print("Invalid Option")