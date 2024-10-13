class Human:
    can_walk = "Fast"
    can_speak = "English"
    can_work = True
    can_sing = True
    
Ryan = Human()

print(Ryan.can_speak)

class Audi:
    def __init__(self,Name,ID,Salary):
    self.name = Name
    self.ID = ID
    self.Salary = Salary
    
    def getdetails(self):
        print(f"Name :{self.Name}, ID: {self.ID}, Salary: {self.Salary}")

emp1 = Audi("Raj",1234,180000)
emp2 = Audi("Jevin",4591,150000)
emp3 = Audi("Arijit",7039,165000)

emp2.getdetails()
emp3.getdetail()
