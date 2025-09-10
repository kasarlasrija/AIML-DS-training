def unique(lst):
    f = {}
    for i in lst:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    for i in f:
        if f[i] == 1:
            print(i)

list1 = [1, 2, 3, 2, 3, 3, 4]
unique(list1)
