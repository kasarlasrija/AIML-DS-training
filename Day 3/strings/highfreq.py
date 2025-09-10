def occ(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    max_count = -1
    max_char = ''
    for char, count in f.items():
        if count > max_count:
            max_count = count
            max_char = char

    print(max_char)

str1 = "aaabbca"
occ(str1)
