class fun:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def myFunction(self):
        print(f"My name is: {self.x}")
        print(f"My brother name is: {self.y}")

ob1= fun("Rakib", "RAZ")
ob1.myFunction()

# outPUT
# My name is: Rakib
# My brother name is: RAZ