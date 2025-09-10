def length(s):
    count = 0
    for i in s:
        count += 1
    return count
def compare(s1, s2):
    if s1 == s2:
        return "Equal"
    else:
        return "Not equal"

def concatenate(s1, s2):
    return s1 + s2

str1 = input()
str2 = input()

print("L1", length(str1))
print("L2", length(str2))
print(compare(str1, str2))
print("Concatenated", concatenate(str1, str2))
