class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        today = 2020
        working_years = int(today) - int(self.employment_year) 
        return working_years
    def __str__(self):
        return "Name: %s, Age: %d, Salary: %d, Working Years: %d" % (self.name,self.age,self.salary,self.get_working_years())
# employee1 = Employee("Majed", 24, 2350, "2018")
# print(employee1.salary)
# print(employee1.get_working_years())

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        bonus = float(self.bonus_percentage) * int(self.salary)
        return bonus
    def __str__(self):
        return "Name: %s, Age: %d, Salary: %d, Working Years: %d, Bonus: %f" % (self.name,self.age,self.salary,self.get_working_years(), self.get_bonus())

manager1 = Manager("Majed", 24, 2350, 2018, 12.5)
# print(manager1.get_bonus())
# print(manager1.get_working_years)
employees = []
managers = [manager1]
def option():
    print ("""Options:
    1- Show Employee
    2- Show Manager
    3- Add Employee
    4- Add Manager""")
option()
user_input = int(input("What would you like to do? "))
while user_input!= 5:
    if user_input == 1:
        for employee in employees:
            print (employee)
        option()
        user_input = int(input("What would you like to do? "))
    elif user_input == 2:
        for manager in managers:
            print (manager)
        option()
        user_input = int(input("What would you like to do? "))
    elif user_input == 3:
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter Salary: ")
        employment = input("Enter working years: ")
        employee =  Employee(name,int(age),int(salary), int(employment))
        employees.append(employee)
        print ("employee added")
        option()
        user_input = int(input("What would you like to do? "))
    elif user_input == 4:
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter Salary: ")
        employment = input("Enter working years: ")
        bonus = input("Enter bonus: ")
        manager =  Manager(name,int(age),int(salary), int(employment), float(bonus))
        managers.append(manager)
        print("manager added")
        option()
        user_input = input("What would you like to do? ")
       
    else:
        user_input = int(input("Invalid input, What would you like to do? "))