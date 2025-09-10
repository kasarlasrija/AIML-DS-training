def occ(s):
    f = {}
    for i in s:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    min_count = float('inf')
    min_char = ''
    for char, count in f.items():
        if count < min_count:
            min_count = count
            min_char = char

    print(min_char)

str1 = "aaabbca"
occ(str1)
