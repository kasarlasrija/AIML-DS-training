class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Employee details:")
        print("Name:", self.name)
        print("Salary:", self.salary)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        super().display()
        print("Department:", self.department)
e = Employee('dimple',100000000)
m = Manager('srija',1000000,'hr')
e.display()
print()
m.display()