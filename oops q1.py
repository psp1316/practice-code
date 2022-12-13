class Calculator:
    def __init__(self,a):
        self.square=a*a
        self.cube=a*a*a

    def getsquare(self):
        print(f"the square of given no is {self.square}")
       
    def getcube(self):
         print(f"the cube of given no is {self.cube}")

a=Calculator(2)
a.getsquare()
    