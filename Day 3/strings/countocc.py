def occ(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    result = ""
    for char, count in f.items():
        result += char + str(count)
    print(result)

str1 = "aaabbca"
occ(str1)
