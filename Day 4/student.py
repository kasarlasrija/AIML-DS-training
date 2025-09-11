class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.roll_no = input("Enter roll number: ")
        self.marks = input("Enter marks: ")

    def display(self):
        print("Name:", self.name, "Rollno:", self.roll_no, "Marks:", self.marks)

s1 = Student()
s2 = Student()

s1.display()
s2.display()
