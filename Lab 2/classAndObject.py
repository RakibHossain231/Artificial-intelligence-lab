class Car:
    def __init__(self):
        self.company= "Toyota"
        self.model= "corolla"
        self.year= 2010
    def __str__(self):
        return f"Company: {self.company}\nmodel:{self.model}\nyear:{self.year}"
    def getCompany(self):
        return self.company
    def setCompany(self, company):
        self.company= company

# object create
myCar= Car()

x= myCar.getCompany()
print(x)

myCar.setCompany("Honda")
print(x) # Toyota
print(myCar.company) # Honda


# Address print
print(myCar)
print("\n")
print("\n")
# __str__ er jnno ja return korbe ta print hobe
print(myCar)