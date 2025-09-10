list1=[1,2,3,4,5,6]

list = list(set(list1))
list.sort()

if len(list) >= 2:
    print("Second largest:", list[-2])
else:
    print("Not enough")