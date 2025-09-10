def delete(lst, ele):
    list = []
    for i in range(len(lst)):
        if(i!=ele):
            list.append(lst[i])
    print(list)
list1 = [1, 2, 3, 4, 3, 5]
result = delete(list1, 3)
print(result)
