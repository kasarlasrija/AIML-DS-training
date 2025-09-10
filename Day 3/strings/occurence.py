def occ(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    for char, count in f.items():
        print(char, count)

str1 = "hellohiii"
occ(str1)
