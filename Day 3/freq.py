def count_frequency(lst):
    f = {}
    for i in lst:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    return f

list1 = [1, 2, 3, 2, 3, 3, 4]
result = count_frequency(list1)
print(result)
