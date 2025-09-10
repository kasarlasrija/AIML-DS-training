students = []
def data(roll, name, marks):
    students.append((roll, name, marks))
    
data(1, "srija", 100)
data(2, "dimple", 99)
data(3, "deethu", 75)
data(4, "chinni", 98)
data(5, "naani", 99)

print(students)

high = -1
for i in students:
    if i[2] > high:
        high= i[2]
        n= i[1]
print("Student with highest marks:",n)

print("Students who scored more than 75:")
for i in students:
    if i[2] > 75:
        print(i[1])