# intiating a class
class Employee:
    # constructor method
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        
    # creating method for the obj
    def travel(self, destination):
        print(f"Now the employee is travelling to {destination}.")
        
# creating an object/instance of class
Sam = Employee()

# printing the attributes
print(Sam.salary)

# accessing method
Sam.travel("Kerala")